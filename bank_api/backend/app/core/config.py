import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = (Path(__file__) / ".." / ".." / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PROJECT_PORT: int

    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    REDIS_PORT: int
    REDIS_HOST: str
    REDIS_PASS: str

    TOKEN_BOT: str

    INIT_USER: dict = {
        "user_name": "Artemio",
        "email": "mvamvп2h@gmail.com",
        "password": "s4gF3dsg45D#$"
    }

    INIT_ALPHA_BELKA: dict = {
        "sell_currency": "TEST_BYN",
        "buy_currency": "TEST_USD",
        "bank_sell": 2.89,
        "bank_buy": 2.84
    }

    INIT_NB_BELAPB: dict = {
        "sell_currency": "TEST_BYN",
        "buy_currency": "TEST_USD",
        "convert": 2.89

    }

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)-7s %(asctime)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, 'logs', 'api.log'),
            "formatter": "standard",
            "encoding": "UTF-8",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 1000
        }
    },
    "loggers": {
        "bank_aggregator": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        }
    }
}
