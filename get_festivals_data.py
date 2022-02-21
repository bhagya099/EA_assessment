import requests


def get_festivals_data():
    BASE_URL = 'https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals'
    response = requests.get(BASE_URL)
    return response


# print(get_festivals_data())