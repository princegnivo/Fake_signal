"""Constantes du bot"""

ACTIFS = [
    # Paires Standard & Cross
    ("🇪🇺 EUR/USD 🇺🇸", "OTC"),
    ("🇺🇸 USD/JPY 🇯🇵", "OTC"),
    ("🇬🇧 GBP/USD 🇺🇸", "OTC"),
    ("🇺🇸 USD/CAD 🇨🇦", "OTC"),
    ("🇺🇸 USD/CHF 🇨🇭", "OTC"),
    ("🇦🇺 AUD/USD 🇺🇸", "OTC"),
    ("🇳🇿 NZD/USD 🇺🇸", "OTC"),
    ("🇪🇺 EUR/GBP 🇬🇧", "OTC"),
    ("🇪🇺 EUR/JPY 🇯🇵", "OTC"),
    ("🇪🇺 EUR/CAD 🇨🇦", "OTC"),
    ("🇪🇺 EUR/CHF 🇨🇭", "OTC"),
    ("🇪🇺 EUR/NZD 🇳🇿", "OTC"),
    ("🇪🇺 EUR/HUF 🇭🇺", "OTC"),
    ("🇪🇺 EUR/TRY 🇹🇷", "OTC"),
    ("🇪🇺 EUR/RUB 🇷🇺", "OTC"),
    ("🇬🇧 GBP/JPY 🇯🇵", "OTC"),
    ("🇬🇧 GBP/CAD 🇨🇦", "OTC"),
    ("🇬🇧 GBP/CHF 🇨🇭", "OTC"),
    ("🇬🇧 GBP/AUD 🇦🇺", "OTC"),
    ("🇦🇺 AUD/CAD 🇨🇦", "OTC"),
    ("🇦🇺 AUD/CHF 🇨🇭", "OTC"),
    ("🇦🇺 AUD/JPY 🇯🇵", "OTC"),
    ("🇦🇺 AUD/NZD 🇳🇿", "OTC"),
    ("🇨🇦 CAD/CHF 🇨🇭", "OTC"),
    ("🇨🇦 CAD/JPY 🇯🇵", "OTC"),
    ("🇨🇭 CHF/JPY 🇯🇵", "OTC"),
    ("🇨🇭 CHF/NOK 🇳🇴", "OTC"),
    ("🇳🇿 NZD/JPY 🇯🇵", "OTC"),
    # Paires Exotiques
    ("🇺🇸 USD/CNH 🇨🇳", "OTC"),
    ("🇺🇸 USD/INR 🇮🇳", "OTC"),
    ("🇺🇸 USD/BRL 🇧🇷", "OTC"),
    ("🇺🇸 USD/RUB 🇷🇺", "OTC"),
    ("🇺🇸 USD/TRY 🇹🇷", "OTC"),
    ("🇺🇸 USD/MXN 🇲🇽", "OTC"),
    ("🇺🇸 USD/EGP 🇪🇬", "OTC"),
    ("🇺🇸 USD/PHP 🇵🇭", "OTC"),
    ("🇺🇸 USD/PKR 🇵🇰", "OTC"),
    ("🇺🇸 USD/IDR 🇮🇩", "OTC"),
    ("🇺🇸 USD/MYR 🇲🇾", "OTC"),
    ("🇺🇸 USD/THB 🇹🇭", "OTC"),
    ("🇺🇸 USD/ZAR 🇿🇦", "OTC"),
    ("🇺🇸 USD/ARS 🇦🇷", "OTC"),
    ("🇺🇸 USD/COP 🇨🇴", "OTC"),
    ("🇺🇸 USD/CLP 🇨🇱", "OTC"),
    ("🇺🇸 USD/BDT 🇧🇩", "OTC"),
    ("🇺🇸 USD/VND 🇻🇳", "OTC"),
    ("🇺🇸 USD/DZD 🇩🇿", "OTC"),
    ("🇺🇸 USD/SGD 🇸🇬", "OTC"),
    # Paires Inversées
    ("🇺🇦 UAH/USD 🇺🇸", "OTC"),
    ("🇳🇬 NGN/USD 🇳🇬", "OTC"),
    ("🇲🇦 MAD/USD 🇺🇸", "OTC"),
    ("🇿🇦 ZAR/USD 🇺🇸", "OTC"),
    ("🇾🇪 YER/USD 🇺🇸", "OTC"),
    ("🇱🇧 LBP/USD 🇺🇸", "OTC"),
    ("🇰🇪 KES/USD 🇺🇸", "OTC"),
    ("🇹🇳 TND/USD 🇺🇸", "OTC"),
    # Paires Asiatiques
    ("🇦🇪 AED/CNY 🇨🇳", "OTC"),
    ("🇴🇲 OMR/CNY 🇨🇳", "OTC"),
    ("🇸🇦 SAR/CNY 🇨🇳", "OTC"),
    ("🇶🇦 QAR/CNY 🇨🇳", "OTC"),
    ("🇯🇴 JOD/CNY 🇨🇳", "OTC"),
    ("🇧🇭 BHD/CNY 🇨🇳", "OTC")
]

DIRECTIONS = ["CALL", "PUT"]

COMMANDS = {
    "start": "Démarrer les signaux",
    "stop": "Arrêter les signaux",
    "signal": "Signal immédiat",
    "help": "Aide",
    "stats": "Statistiques",
    "settings": "Paramètres"
}

MESSAGES = {
    "welcome": "🤖 Bot de signaux de trading activé !\n\nLes signaux seront envoyés toutes les {interval} minutes.",
    "stopped": "🛑 Bot désactivé. Les signaux ne seront plus envoyés.\nPour réactiver, utilisez /start",
    "help": """
📈 **Bot de Signaux de Trading**

**Commandes disponibles:**
/start - Démarrer la réception des signaux
/stop - Arrêter la réception des signaux
/help - Afficher cette aide
/signal - Obtenir un signal immédiat
/stats - Voir les statistiques
/settings - Configurer le bot

**Fonctionnalités:**
- Signaux aléatoires toutes les 2 minutes
- Plus de 60 paires de devises différentes
- Direction aléatoire (CALL/PUT)
- Système de martingales intégré
""",
    "error": "❌ Une erreur est survenue. Veuillez réessayer."
}
