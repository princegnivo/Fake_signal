import asyncio
import logging
import sys
from src.bot import TradingBot
from src.config import config

def setup_logging():
    """Configure le logging"""
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=getattr(logging, config.log_level),
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('bot.log')
        ]
    )

async def main():
    """Point d'entrée principal"""
    try:
        setup_logging()
        logger = logging.getLogger(__name__)
        logger.info("Démarrage du bot de signaux de trading...")
        
        bot = TradingBot()
        await bot.run()
        
    except KeyboardInterrupt:
        logger.info("Bot arrêté par l'utilisateur")
    except Exception as e:
        logger.error(f"Erreur fatale: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
