def get_sheety_data(data:str): 
    with open('./sheety_api.txt','r') as sheety_file:
        sheety_data = sheety_file.read().splitlines() 
    if data=="API":
        return sheety_data[0].split(' = ')[1]
    if data=="TOKEN":
        return sheety_data[1].split(' = ')[1]

