# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TELEGRAM_API_KEY = os.environ.get("TELEGRAM_API_KEY")
OPENAI_API_SECRET_KEY = os.environ.get("OPENAI_API_SECRET_KEY")