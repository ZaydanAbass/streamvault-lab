import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- API Configuration ---
API_KEY = os.environ.get("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

# --- File Paths ---
# Resolve paths relative to the pipeline directory to prevent CWD bugs
BASE_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = BASE_DIR / "cache"
DATA_DIR = BASE_DIR / "data"

# Ensure directories exist
CACHE_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

# --- Business Logic Constants ---
# The year cutoff for the "recent" time window
WINDOW_CUTOFF_YEAR = 2000

# Minimum number of films in a collection to be considered a "bundle"
MIN_BUNDLE_SIZE = 2

# Minimum number of films for a director/actor to be included in talent analysis
MIN_TALENT_FILMS = 3

# Number of top billing actors to consider as "leads"
MAX_LEAD_ACTOR_ORDER = 2