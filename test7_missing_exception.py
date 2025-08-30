import requests


def fetch_data():
    data = requests.get("https://api.example.com").json()
    return data
