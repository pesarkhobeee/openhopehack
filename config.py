import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "SUPER_SECRET_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    BIND_ADDRESS = os.getenv("BIND_ADDRESS", "0.0.0.0")
    PORT = os.getenv("PORT", 8080)
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv(
        "TELEGRAM_CHAT_ID", "-4560142138"
    )  # @openhopehack telegram group
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv("OAUTHLIB_INSECURE_TRANSPORT", "0")
    GOOGLE_SPREADSHEET_ID = os.getenv(
        "GOOGLE_SPREADSHEET_ID", "1TeWnmfktQbqBIIeNk9lkv5vdzD0Innt9LI37Xg0pAMI"
    )  # https://docs.google.com/spreadsheets/d/1TeWnmfktQbqBIIeNk9lkv5vdzD0Innt9LI37Xg0pAMI/edit?usp=sharing
    SERVICE_ACCOUNT_FILE_NAME = os.getenv("SERVICE_ACCOUNT_FILE_NAME")
    GOOGLE_SHEET_RANGE = os.getenv("GOOGLE_SHEET_RANGE", "Sheet1!A:C")
