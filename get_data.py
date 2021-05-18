import os
import requests


DATA_PATH = r'datasets'
BASE_URL = r'https://web.stanford.edu/~yyye/yyye/Gset/G'

if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)
    
    for data_num in range(1, 82):
        response = requests.get(f'{BASE_URL}/{data_num}')
    
        if response.status_code == requests.codes.ok:
            filename = f'{DATA_PATH}/G{data_num}.txt'
            print(f'Downloaded G{data_num}.txt')
            
            with open(filename, 'w') as file:
                file.write(response.text)