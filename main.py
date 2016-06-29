import requests

username = input("Username? ")
password = input("Password? ")

post_data = {
    "username": username,
    "password": password,

}

response = requests.post('http://localhost:8000/api-token-auth/', post_data).json()

token = response['token']

headers = {
    "Authorization": "Token {}".format(token)  # need EXACTLY

}

response = requests.get('http://localhost:8000/beagle_farms/', headers=headers).json()

for farm in response:
    print(farm['owner'], farm['dog_beds'])
