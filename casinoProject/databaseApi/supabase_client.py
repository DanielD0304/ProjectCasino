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

# Test function to verify database connection
def test_connection():
    try:
        response = supabase_client.table("Games").select("*").limit(1).execute()
        print("Full response:", response)
        if response.data:
            print("Database connection successful!")
            print("Sample data:", response.data)
        else:
            print(f"Error occurred: {response}")
    except Exception as e:
        print(f"Exception occurred: {e}")

# Uncomment the following line to test the connection when running this script directly
test_connection()