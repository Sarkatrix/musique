FROM python:3.10-slim

# Crée le répertoire de travail
WORKDIR /app

# Copie les dépendances et les installe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code
COPY . .

# Commande de démarrage du bot
CMD ["python", "bot.py"]
