# Utilise une image officielle Python 3 légère
FROM python:3.12-slim

# Empêche Python de bufferiser la sortie (utile pour voir les logs immédiatement)
ENV PYTHONUNBUFFERED=1

# Crée un répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers nécessaires dans le conteneur
COPY requirements.txt .
COPY app.py .

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Commande exécutée au lancement du conteneur
CMD ["python", "app.py"]
