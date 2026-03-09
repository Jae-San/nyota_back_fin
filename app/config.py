import os

class Config:
    # Clé secrète pour Flask (sessions, etc.)
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Configuration JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    # Configuration Base de données — MySQL via phpMyAdmin
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1
        )


    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuration Emails (Resend ou SMTP Gmail)
    RESEND_API_KEY = os.getenv("RESEND_API_KEY")
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
