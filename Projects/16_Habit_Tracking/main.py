import requests
from pixela_api import get_pixela_api

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "ppalmeros"
GRAPHID = "pgraph1"

user_params = {
    "token": get_pixela_api(),
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

#---This can be run only once to create the user if we run it again it will show an error
#---since the user exists
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":GRAPHID,
    "name": "Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":get_pixela_api(),
}

response = requests.post(url=graph_endpoint,json=graph_params, headers=headers)
print(response.text)

pixel_params = {
    "date":"20240324",
    "quantity":"100",
}

pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"
response = requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
print("-----------------------------------------------")
print("RESPONSE OF THE PIXEL POST")
print(response.text)
print("-----------------------------------------------")
