import requests
from datetime import datetime
from nutritionix import get_nutritionix_data
from sheety import get_sheety_data


NUTRITIONIX_API = get_nutritionix_data("API")
NUTRITIONIX_ID = get_nutritionix_data("ID")

GENDER = "Masculine"
WEIGHT_KG = "110"
HEIGHT_CM = "180"
AGE = "35"

SHEETY_TOKEN = get_sheety_data("TOKEN")
SHEETY_API = get_sheety_data('API')


ENDPOINT = f"https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

PARAMS = {
    "query":exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

HEADER = {
    "x-app-id":NUTRITIONIX_ID,
    "x-app-key":NUTRITIONIX_API
}

nutritionix_response = requests.post(url=ENDPOINT,json=PARAMS, headers=HEADER)
result = nutritionix_response.json()
print(nutritionix_response.text)


SHEETY_ENDPOING = f"https://api.sheety.co/{SHEETY_API}/myWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    SHEETY_PARAMS = {
        'workout': {
            "date":today_date,
            "time":now_time,
            "exercise":"swimming",
            "duration":"60",
            "calories":"2500"
            }
    }

#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {SHEETY_TOKEN}"
}

sheety_response = requests.post(url=SHEETY_ENDPOING,json=SHEETY_PARAMS, headers=SHEETY_TOKEN)

print(sheety_response.text)
