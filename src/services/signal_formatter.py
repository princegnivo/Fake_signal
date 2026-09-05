from typing import Dict, Any
from src.models.signal import TradingSignal

class SignalFormatter:
    """Formateur de signaux pour Telegram"""
    
    @staticmethod
    def format(signal: TradingSignal) -> str:
        """Formate un signal en message Telegram"""
        signal_dict = signal.to_dict()
        
        lines = [
            "______________________________",
            f"📊 ACTIF: {signal_dict['actif']}",
            f"🕘 HEURE D'ENTRÉE: {signal_dict['entre']}",
            f"⏳ EXPIRATION: {signal_dict['expiration']}",
            "",
            f"🔮 Direction: {signal_dict['direction']}",
            "",
            "🔘 Martingales",
            f"1️⃣MG1: {signal_dict['mg1']}",
            f"2️⃣MG2: {signal_dict['mg2']}",
            f"3️⃣MG3: {signal_dict['mg3']}",
            "———————————————"
        ]
        
        return "\n".join(lines)
    
    @staticmethod
    def format_compact(signal: TradingSignal) -> str:
        """Format compact pour les logs"""
        signal_dict = signal.to_dict()
        return f"{signal_dict['actif']} - {signal_dict['direction']} - {signal_dict['entre']}"

# Singleton
signal_formatter = SignalFormatter()
