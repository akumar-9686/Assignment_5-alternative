import requests
import os
import time

def get_exchange_rate():
    
    url = "https://v6.exchangerate-api.com/v6/APIKEY/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']['EUR']

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        amounts = [float(line.strip()) for line in file.readlines()]
    return amounts

def write_output_file(file_path, amounts):
    with open(file_path, 'w') as file:
        for amount in amounts:
            file.write(f"{amount:.2f}\n")

def convert_dollars_to_euros(input_file, output_file):
    exchange_rate = get_exchange_rate()
    dollar_amounts = read_input_file(input_file)
    euro_amounts = [amount * exchange_rate for amount in dollar_amounts]
    write_output_file(output_file, euro_amounts)

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    
    while True:
  
        if os.path.exists(input_file) and os.path.getsize(input_file) > 0:
            
            if not os.path.exists(output_file):
                open(output_file, 'w').close()

            convert_dollars_to_euros(input_file, output_file)
            print("Conversion complete. Check the output file for results.")
            
        
            open(input_file, 'w').close()
        
 
        time.sleep(15)