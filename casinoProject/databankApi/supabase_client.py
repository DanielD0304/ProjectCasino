import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

#Check if URL and Key are retrieved correctly
if not url or not key:
    raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY in environment variables")

supabase_client: Client = create_client(url, key)

def fetch_data_from_table(table_name: str):
    response =  supabase_client.table(table_name).select("*").execute()
    return response.data

def test_connection():
    try:
        response = supabase_client.table("Games").select("*").execute()
        print("Full response: ", response)
        if response.data:
            print("Connection succesfull")
            print("Data: ", response.data)
        else:
            print("Connection failed")
    except Exception as e:
        print("Exception: ", e)

test_connection()        