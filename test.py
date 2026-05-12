import requests

API_KEY = "n92xLG6VhQ3MP1YHyQIFcV57RTac5uQbwxgHBYYd"
url = "https://api.api-ninjas.com/v1/animals"

response = requests.get(
    url,
    headers={"X-Api-Key": API_KEY},
    params={"name": "uzht"}
)

print(response.status_code)
print(response.json())