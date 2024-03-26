def get_nutritionix_data(data:str): 
    with open('./nutritionix_api.txt','r') as nutrtionix_file:
        nutritionix_data = nutrtionix_file.read().splitlines() 
    if data=="API":
        return nutritionix_data[1].split(' = ')[1]
    if data=="ID":
        return nutritionix_data[0].split(' = ')[1]

