from telegram import Update
from telegram.ext import ContextTypes
import logging
from src.utils.constants import MESSAGES, COMMANDS
from src.handlers.signal_sender import SignalSender
from src.services.signal_generator import signal_generator

logger = logging.getLogger(__name__)

class CommandHandler:
    """Gestionnaire des commandes Telegram"""
    
    def __init__(self, signal_sender: SignalSender):
        self.signal_sender = signal_sender
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Commande /start"""
        chat_id = update.effective_chat.id
        
        # Ajouter le chat
        self.signal_sender.active_chats.add(chat_id)
        
        # Si l'envoi n'est pas démarré, le démarrer
        if not self.signal_sender.is_running:
            await self.signal_sender.start()
        
        # Envoyer un signal immédiat
        try:
            signal_message = await self.signal_sender.send_immediate_signal(chat_id)
            welcome_message = MESSAGES["welcome"].format(
                interval=self.signal_sender.interval // 60
            )
            await update.message.reply_text(f"{welcome_message}\n\n{signal_message}")
        except Exception as e:
            logger.error(f"Erreur lors du démarrage pour {chat_id}: {e}")
            await update.message.reply_text(MESSAGES["error"])
        
        logger.info(f"Chat {chat_id} a démarré le bot")
    
    async def stop(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Commande /stop"""
        chat_id = update.effective_chat.id
        
        # Retirer le chat
        self.signal_sender.active_chats.discard(chat_id)
        
        # Si plus de chats actifs, arrêter l'envoi
        if not self.signal_sender.active_chats and self.signal_sender.is_running:
            await self.signal_sender.stop()
        
        await update.message.reply_text(MESSAGES["stopped"])
        logger.info(f"Chat {chat_id} a arrêté le bot")
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Commande /help"""
        await update.message.reply_text(MESSAGES["help"], parse_mode="Markdown")
    
    async def signal(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Commande /signal"""
        chat_id = update.effective_chat.id
        
        try:
            message = await self.signal_sender.send_immediate_signal(chat_id)
            await update.message.reply_text(message)
        except Exception as e:
            logger.error(f"Erreur lors du signal immédiat pour {chat_id}: {e}")
            await update.message.reply_text(MESSAGES["error"])
    
    async def stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Commande /stats"""
        stats = signal_generator.get_stats()
        active_chats = len(self.signal_sender.active_chats)
        
        stats_message = f"""
📊 **Statistiques du Bot**

👥 **Chats actifs:** {active_chats}
📈 **Paires disponibles:** {stats['total_actifs']}
🎯 **Directions:** {', '.join(stats['directions'])}
⏰ **Délai d'entrée:** {stats['entry_delay']} min
🔄 **Intervalle martingale:** {stats['martingale_interval']} min
⏱️ **Expiration:** {stats['expiration']}s

🔄 **Statut:** {'🟢 Actif' if self.signal_sender.is_running else '🔴 Inactif'}
"""
        await update.message.reply_text(stats_message, parse_mode="Markdown")
