import os
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# --- API Configuration ---
API_KEY = os.environ.get("TMDB_API_KEY")
if not API_KEY:
    raise ValueError("CRITICAL: TMDB_API_KEY is missing. Check your .env file.")
BASE_URL = "https://api.themoviedb.org/3"

# --- File Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = BASE_DIR / "cache"
DATA_DIR = BASE_DIR / "data"

# Fix: Use parents=True to create parent directories if they don't exist
CACHE_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

# --- Business Logic Constants ---
WINDOW_CUTOFF_YEAR = 2000
MIN_BUNDLE_SIZE = 2
MIN_TALENT_FILMS = 3
MAX_LEAD_ACTOR_ORDER = 2

# --- Security Guard ---
# Prevent accidental logging of the API key if someone prints the config dict
def get_safe_config():
    return {
        "BASE_URL": BASE_URL,
        "WINDOW_CUTOFF_YEAR": WINDOW_CUTOFF_YEAR,
        "API_KEY": "***HIDDEN***"
    }