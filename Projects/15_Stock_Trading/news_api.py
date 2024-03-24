def get_new_api():
    with open('./new_api.txt','r') as stock_api_file:
        api_data = stock_api_file.readline().rstrip().split(' = ')[1]
        
    return api_data