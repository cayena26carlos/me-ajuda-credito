import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SECRET_KEY = os.getenv("SUPABASE_SECRET_KEY")


if not SUPABASE_URL:
    raise RuntimeError("SUPABASE_URL não configurada.")


if not SUPABASE_SECRET_KEY:
    raise RuntimeError("SUPABASE_SECRET_KEY não configurada.")


supabase_client: Client = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY,
)
