from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_KEY or not SUPABASE_URL:
    raise ValueError("SUPABASE_KEY or SUPABASE_URL not found in .env file")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)