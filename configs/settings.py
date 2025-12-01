import os
import dotenv

dotenv.load_dotenv(".env")

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
TWITCH_AUTHORIZATION_BASE_URL = "https://id.twitch.tv/oauth2/authorize"
TWITCH_TOKEN_URL = "https://id.twitch.tv/oauth2/token"
TWITCH_USER_URL = "https://api.twitch.tv/helix/users"

REDIRECT_URI = os.getenv("REDIRECT_URI")

DB_URI = os.getenv("DB_URI")