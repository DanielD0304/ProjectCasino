from django.shortcuts import render
from .supabase_client import fetch_data_from_table

def data_view(request):
    data = fetch_data_from_table("Games")
    return render(request, 'testing.html', {'data': data})

# Create your views here.
