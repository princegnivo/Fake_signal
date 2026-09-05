import random
from datetime import datetime, timedelta
from typing import Optional
import logging
from src.utils.constants import ACTIFS, DIRECTIONS
from src.models.signal import TradingSignal
from src.config import config

logger = logging.getLogger(__name__)

class SignalGenerator:
    """Générateur de signaux de trading"""
    
    def __init__(self):
        self.actifs = ACTIFS
        self.directions = DIRECTIONS
        self.entry_delay = config.entry_delay
        self.martingale_interval = config.martingale_interval
        self.expiration = config.expiration_time
    
    def generate(self) -> TradingSignal:
        """Génère un signal aléatoire"""
        try:
            # Sélection aléatoire
            actif_with_market = random.choice(self.actifs)
            actif = f"{actif_with_market[0]} {actif_with_market[1]}"
            direction = random.choice(self.directions)
            
            # Calcul des temps
            now = datetime.now()
            entry_time = self._round_to_minute(now + timedelta(minutes=self.entry_delay))
            
            # Création du signal
            signal = TradingSignal.create_from_times(
                actif=actif,
                direction=direction,
                entry_time=entry_time,
                martingale_interval=self.martingale_interval,
                expiration=self.expiration
            )
            
            logger.debug(f"Signal généré: {signal.to_dict()}")
            return signal
            
        except Exception as e:
            logger.error(f"Erreur lors de la génération du signal: {e}")
            raise
    
    def _round_to_minute(self, dt: datetime) -> datetime:
        """Arrondit à la minute supérieure"""
        return dt.replace(second=0, microsecond=0)
    
    def get_stats(self) -> dict:
        """Retourne les statistiques du générateur"""
        return {
            "total_actifs": len(self.actifs),
            "directions": self.directions,
            "entry_delay": self.entry_delay,
            "martingale_interval": self.martingale_interval,
            "expiration": self.expiration
        }

# Singleton
signal_generator = SignalGenerator()
