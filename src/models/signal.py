from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dataclasses import field

@dataclass
class TradingSignal:
    """Modèle de signal de trading"""
    actif: str
    direction: str
    entre: datetime
    mg1: datetime
    mg2: datetime
    mg3: datetime
    expiration: int = 60
    created_at: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Validation après initialisation"""
        if self.direction not in ["CALL", "PUT"]:
            raise ValueError("Direction doit être CALL ou PUT")
        
        if self.expiration <= 0:
            raise ValueError("Expiration doit être positive")
    
    @classmethod
    def create_from_times(cls, actif: str, direction: str, 
                          entry_time: datetime, 
                          martingale_interval: int = 1,
                          expiration: int = 60) -> "TradingSignal":
        """Crée un signal à partir des temps"""
        return cls(
            actif=actif,
            direction=direction,
            entre=entry_time,
            mg1=entry_time + timedelta(minutes=martingale_interval),
            mg2=entry_time + timedelta(minutes=martingale_interval * 2),
            mg3=entry_time + timedelta(minutes=martingale_interval * 3),
            expiration=expiration
        )
    
    def to_dict(self) -> dict:
        """Convertit en dictionnaire"""
        return {
            "actif": self.actif,
            "direction": self.direction,
            "entre": self.entre.strftime("%H:%M"),
            "mg1": self.mg1.strftime("%H:%M"),
            "mg2": self.mg2.strftime("%H:%M"),
            "mg3": self.mg3.strftime("%H:%M"),
            "expiration": f"{self.expiration}s (1min)",
            "created_at": self.created_at.isoformat()
        }

# Import nécessaire pour le timedelta
from datetime import timedelta
