import asyncio
import logging
from typing import Set
from telegram import Bot
from src.services.signal_generator import signal_generator
from src.services.signal_formatter import signal_formatter
from src.config import config

logger = logging.getLogger(__name__)

class SignalSender:
    """Gestionnaire d'envoi des signaux"""
    
    def __init__(self, bot: Bot):
        self.bot = bot
        self.active_chats: Set[int] = set()
        self.is_running = False
        self.interval = config.signal_interval
        self._task: Optional[asyncio.Task] = None
    
    async def start(self):
        """Démarre l'envoi des signaux"""
        if self.is_running:
            return
        
        self.is_running = True
        self._task = asyncio.create_task(self._send_loop())
        logger.info("Envoi des signaux démarré")
    
    async def stop(self):
        """Arrête l'envoi des signaux"""
        self.is_running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None
        logger.info("Envoi des signaux arrêté")
    
    async def _send_loop(self):
        """Boucle d'envoi des signaux"""
        while self.is_running:
            try:
                await self._send_signal_to_all()
                await asyncio.sleep(self.interval)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Erreur dans la boucle d'envoi: {e}")
                await asyncio.sleep(5)  # Attendre avant de réessayer
    
    async def _send_signal_to_all(self):
        """Envoie un signal à tous les chats actifs"""
        if not self.active_chats:
            logger.debug("Aucun chat actif")
            return
        
        try:
            signal = signal_generator.generate()
            message = signal_formatter.format(signal)
            
            # Envoi en parallèle
            tasks = []
            for chat_id in self.active_chats.copy():
                tasks.append(self._send_to_chat(chat_id, message))
            
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)
                logger.info(f"Signal envoyé à {len(tasks)} chats")
                
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi du signal: {e}")
    
    async def _send_to_chat(self, chat_id: int, message: str):
        """Envoie un message à un chat spécifique"""
        try:
            await self.bot.send_message(
                chat_id=chat_id,
                text=message,
                parse_mode="HTML"
            )
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi à {chat_id}: {e}")
            self.active_chats.discard(chat_id)
    
    async def send_immediate_signal(self, chat_id: int) -> str:
        """Envoie un signal immédiat à un chat"""
        try:
            signal = signal_generator.generate()
            message = signal_formatter.format(signal)
            await self._send_to_chat(chat_id, message)
            return message
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi immédiat à {chat_id}: {e}")
            raise
