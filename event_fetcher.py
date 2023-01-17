from typing import Any

import requests

URL = "https://eonet.gsfc.nasa.gov/api/v2.1/events?days=5"


def get_data_for_5_days() -> dict[str, Any]:
    response = requests.get(url=URL)
    return response.json()



