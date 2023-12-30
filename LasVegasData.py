import requests
import json
from datetime import datetime

url = "https://zillow56.p.rapidapi.com/search"

querystring = {"location":"Las Vegas, NV"}

with open('config.json', 'r') as config_file: 
	api_key = json.load(config_file)
print('API & HOST KEY',  api_key)

# response = requests.get(url, headers=api_key, params=querystring)

# print(response.json()['results'])

now = datetime.now()
dt_now_string = now.strftime("%d%m%Y%H%M%S")


def extract_zillow_data(url, api_key, queryString): 
    dt_string = dt_now_string
    # return api_key
    response = requests.get(url, headers=api_key, params=querystring)
    response_data = response.json()
    

    # Specify the output file path
    output_file_path = f"response_data_{dt_string}.json"
    file_str = f'response_data_{dt_string}.csv'

    # Write the JSON response to a file
    with open(output_file_path, "w") as output_file:
        json.dump(response_data, output_file, indent=4)  # indent for pretty formatting
    output_list = [output_file_path, file_str]
    return output_list  


extract_zillow_data(url, api_key, querystring)

