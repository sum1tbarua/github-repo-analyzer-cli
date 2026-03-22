# utils/config.py
import os

BASE_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
DEFAULT_TIMEOUT = 5
USER_AGENT = "auth-inspector-cli"
MAX_RETRIES = 3