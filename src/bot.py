import logging
from telegram.ext import Application, CommandHandler
from src.config import config
from src.handlers.commands import CommandHandler as TelegramCommandHandler
from src.handlers.signal_sender import SignalSender

logger = logging.getLogger(__name__)

class TradingBot:
    """Bot Telegram principal"""
    
    def __init__(self):
        self.config = config
        self.application = Application.builder().token(self.config.telegram_token).build()
        self.signal_sender = SignalSender(self.application.bot)
        self.command_handler = TelegramCommandHandler(self.signal_sender)
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Configure les handlers"""
        self.application.add_handler(CommandHandler("start", self.command_handler.start))
        self.application.add_handler(CommandHandler("stop", self.command_handler.stop))
        self.application.add_handler(CommandHandler("help", self.command_handler.help))
        self.application.add_handler(CommandHandler("signal", self.command_handler.signal))
        self.application.add_handler(CommandHandler("stats", self.command_handler.stats))
        
        # Handler pour les erreurs
        self.application.add_error_handler(self._error_handler)
    
    async def _error_handler(self, update, context):
        """Gestionnaire d'erreurs"""
        logger.error(f"Erreur: {context.error}")
        if update and update.effective_chat:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="❌ Une erreur est survenue. Veuillez réessayer."
            )
    
    async def run(self):
        """Démarre le bot"""
        logger.info("Bot démarrage...")
        
        # Démarrer l'envoi des signaux
        await self.signal_sender.start()
        
        # Démarrer l'application
        try:
            await self.application.run_polling()
        except KeyboardInterrupt:
            logger.info("Arrêt demandé par l'utilisateur")
        finally:
            await self.signal_sender.stop()
