from django.shortcuts import render
import requests

# Create your views here.
def index(request):

        # URL vašeg API-ja
    api_url = 'http://127.0.0.1:8000/api/properties/'
    
    try:
        # Slanje GET zahteva ka API-ju
        response = requests.get(api_url)
        response.raise_for_status()  # Provera da li je zahtev uspešan
        api_data = response.json()  # Preuzimanje JSON podataka
    except requests.exceptions.RequestException as e:
        api_data = None  # U slučaju greške

    # Prosleđivanje podataka ka template-u
    context = {
        'api_data': api_data
    }
    

    return render(request, 'index.html', context)