import os

class Config:
    # Clé secrète pour Flask (sessions, etc.)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key_NYOTA_2026")
    
    # --- CONFIGURATION JWT (Indispensable pour corriger ton erreur) ---
    # Cette clé sert à encoder et décoder tes jetons d'accès
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_super_secret_key_NYOTA")
    # Optionnel : durée de validité du token (ex: 24 heures)
    # JWT_ACCESS_TOKEN_EXPIRES = 86400 

    # Configuration Base de données
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:Admin123!@localhost:5432/NYOTA_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuration Emails (Resend ou SMTP Gmail)
    RESEND_API_KEY = os.getenv("RESEND_API_KEY")
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "tonemail@gmail.com")
    # Utilise de préférence une variable d'environnement pour le mot de passe d'application
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "onzb xnat ifew svwc")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "tonemail@gmail.com")