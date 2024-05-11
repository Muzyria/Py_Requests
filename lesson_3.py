import requests


# response = requests.post(
#     url="https://petstore.swagger.io/v2/pet",  # Endpoint
#     headers={
#         "api_key": "special-key"
#     },
#     json={
#           "id": 100,
#           "category": {
#             "id": 0,
#             "name": "string"
#           },
#           "name": "Doggie",
#           "photoUrls": [
#             "string"
#           ],
#           "tags": [
#             {
#               "id": 0,
#               "name": "dogs"
#             }
#           ],
#           "status": "available"
#         }
# )
#
# print(response.json())
#
# get_pet_by_id = requests.get(
#     url="https://petstore.swagger.io/v2/pet/100",
#     headers={
#         "api_key": "special-key"
#     },
# )
#
# print(get_pet_by_id.json())


response = requests.post(
    url="https://petstore.swagger.io/v2/pet/100/uploadImage",  # Endpoint
    headers={
        "api_key": "special-key"
    },
    files={
        "file": ("screenshot.png", open("screenshot.png", "rb"), "image/png")
    }
)

print(response.status_code)
print(response.json())
