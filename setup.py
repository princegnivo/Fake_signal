from setuptools import setup, find_packages

setup(
    name="trading-signal-bot",
    version="1.0.0",
    description="Telegram bot for trading signal generation",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot>=20.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "trading-bot=src.main:main",
        ],
    },
    python_requires=">=3.8",
)
