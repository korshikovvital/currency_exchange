from django.http import JsonResponse
import requests
import time

latest_requests = []


def get_current_usd(request):
    response = requests.get(
        'https://v6.exchangerate-api.com/v6/2a2aecdf12571818d98bc2ff/latest/USD'
    )
    data = response.json()

    latest_requests.append({
        'rate': data['conversion_rates']['RUB']
    })

    if len(latest_requests) > 10:
        latest_requests.pop(0)

    time.sleep(10)

    return JsonResponse({
        'current_usd_to_rub': data['conversion_rates']['RUB'],
        'latest_requests': latest_requests
    })
