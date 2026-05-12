import requests

API_KEY = "n92xLG6VhQ3MP1YHyQIFcV57RTac5uQbwxgHBYYd"
API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name}
    )

    return response.json()