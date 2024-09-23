from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'bb0fd32a3dcf9b68b4d96e62af87cdc9' # Replace with your actual API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an error for bad responses
            weather_data = response.json()
        except requests.exceptions.RequestException as e:
            error_message = str(e)

    return render(request, 'weatheTracker/index.html', {'weather_data': weather_data, 'error_message': error_message})
