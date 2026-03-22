# utils/config.py
import os

BASE_URL = "https://api.github.com"
DEFAULT_TIMEOUT = 5
DEFAULT_PER_PAGE = 100
MAX_RETRIES = 3
USER_AGENT = "auth-inspector-cli"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")