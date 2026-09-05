import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional

load_dotenv()

@dataclass
class Config:
    """Configuration du bot"""
    telegram_token: str
    signal_interval: int = 120  # Secondes
    entry_delay: int = 3  # Minutes
    martingale_interval: int = 1  # Minutes
    expiration_time: int = 60  # Secondes
    max_retries: int = 3
    log_level: str = "INFO"
    
    @classmethod
    def from_env(cls) -> "Config":
        """Charge la configuration depuis les variables d'environnement"""
        token = os.getenv("TELEGRAM_TOKEN")
        if not token:
            raise ValueError("TELEGRAM_TOKEN est requis dans .env")
        
        return cls(
            telegram_token=token,
            signal_interval=int(os.getenv("SIGNAL_INTERVAL", "120")),
            entry_delay=int(os.getenv("ENTRY_DELAY", "3")),
            martingale_interval=int(os.getenv("MARTINGALE_INTERVAL", "1")),
            expiration_time=int(os.getenv("EXPIRATION_TIME", "60")),
            max_retries=int(os.getenv("MAX_RETRIES", "3")),
            log_level=os.getenv("LOG_LEVEL", "INFO")
        )

# Singleton
config = Config.from_env()
