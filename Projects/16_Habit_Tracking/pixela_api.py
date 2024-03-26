def get_pixela_api():
    with open('./pixela_api.txt','r') as pixela_api_file:
        pixela_api_key = pixela_api_file.readline().split(' = ')[1]
    
    return pixela_api_key