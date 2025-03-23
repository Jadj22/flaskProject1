from datetime import timedelta
import os

class Config:
    # 🔑 Sécurité : Utilisation des variables d'environnement avec des valeurs par défaut
    SECRET_KEY = os.getenv("SECRET_KEY", "b3e3b0e4-8180-4b27-8f26-bb9173c2fa45")
    
    # 🛠 Correction du format PostgreSQL pour éviter les erreurs sur Render
    database_url = os.getenv("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/data_recettes")
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 🔐 JWT Configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "f4c5a682-d96b-4c24-bcdb-4fe6d927ff58")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)

    # 🌐 Configuration CORS (Accès API)
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000,http://192.168.110.1:3000').split(',')
    CORS_HEADERS = ["Content-Type", "Authorization"]

    CORS_RESOURCES = {
        r"/*": {
            "origins": CORS_ORIGINS,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "supports_credentials": True,
            "allow_headers": CORS_HEADERS
        }
    }
