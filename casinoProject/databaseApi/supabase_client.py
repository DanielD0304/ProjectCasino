import os
from supabase import create_client, Client
from dotenv import load_dotenv

#Load enviroment variables from .env file
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Check if the URL and key are retrieved correctly
if not url or not key:
    raise ValueError("Supabase URL and key must be set in environment variables")

supabase_client: Client = create_client(url, key)


def fetch_data_from_table(table_name: str):
    response = supabase_client.table(table_name).select("*").execute()
    return response.data