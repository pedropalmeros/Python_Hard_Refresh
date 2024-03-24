def get_stock_api():
    with open('./Trade_Stock.txt','r') as stock_api_file:
        api_data = stock_api_file.readline().rstrip().split(' = ')[1]
        
    return api_data