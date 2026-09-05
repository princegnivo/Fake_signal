FROM python:3.10-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY src/ ./src/
COPY .env ./

# Créer un utilisateur non-root
RUN useradd -m -u 1000 botuser && chown -R botuser:botuser /app
USER botuser

# Démarrer le bot
CMD ["python", "-m", "src.main"]
