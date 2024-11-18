from django.shortcuts import render
from .supabase_client import fetch_data_from_table

# Create your views here.
def my_view(request):
    data = fetch_data_from_table("Games")
    return render(request, "my_template.html", {"data": data})