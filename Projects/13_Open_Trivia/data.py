import requests


question_data = []

question_type = "boolean"
number_questions = "10"
url = f'https://opentdb.com/api.php?amount={number_questions}&type={question_type}'
response = requests.get(url)
response.raise_for_status()
data = response.json()
question_data = data["results"]