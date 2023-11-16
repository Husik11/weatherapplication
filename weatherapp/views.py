import requests
from datetime import datetime
from django.shortcuts import render

def index(request):
    try:
        city_weather_app = {}
        if request.method == 'POST':
            API_KEY = 'e9ac6db454c47111ab518fd5c3c536f8'
            city_name = request.POST.get('city')
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            response = requests.get(url).json()
            current_time = datetime.now()
            formatted_time = current_time.strftime("%A, %B %d, %Y, %H:%M:%S %p")
            city_weather_app = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + ' km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
        context = {'city_weather_app': city_weather_app}
        return render(request, 'weatherapp/home.html', context)
    except:
        return render(request, 'weatherapp/404.html')


