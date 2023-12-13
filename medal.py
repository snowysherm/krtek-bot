import requests
import os
from dotenv import load_dotenv

load_dotenv()
MEDAL_API = os.getenv("MEDAL_API")


def medal_api(id=None):
    global r
    headers = {"Authorization": MEDAL_API}
    if id:
        r = requests.get(
            f'https://developers.medal.tv/v1/latest?userId=50766636&limit=1000&categoryId={id}',
            headers=headers)
    elif not id:
        r = requests.get(
            f'https://developers.medal.tv/v1/latest?userId=50766636&limit=1000',
            headers=headers)

    return r.json()
