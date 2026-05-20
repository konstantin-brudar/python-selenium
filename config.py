import os

from dotenv import load_dotenv


load_dotenv()

USER_EMAIL = os.getenv("USER_EMAIL", "")
USER_PASSWORD = os.getenv("USER_PASSWORD", "")

MAIN_PAGE_URL = "https://skyrexio.com/"
LOGIN_PAGE_URL = "https://app.skyrexio.com/login"

BROWSER_WIDTH = 1280
BROWSER_HEIGHT = 1024

DEFAULT_TIMEOUT = 10
