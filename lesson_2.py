import requests
from requests.auth import HTTPBasicAuth

# response = requests.get(
#     url="https://petstore.swagger.io/v2/store/inventory",  # Endpoint
#     # auth=HTTPBasicAuth(username="username", password="password")
#     headers={
#         "api_key": "special-key"
#     },
#     # params={},
#     # verify=False
# )
#
# print(response.json()["placed"])
# print(response.status_code)


# username = "string"
# response = requests.get(
#     url=f"https://petstore.swagger.io/v2/user/{username}",  # Endpoint
#     headers={
#         "api_key": "special-key"
#     }
# )
#
# print(response.json())


response = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",  # Endpoint
    headers={
        "api_key": "special-key"
    },
    params={
        "status": "available"
    }
)

print(response.json())

