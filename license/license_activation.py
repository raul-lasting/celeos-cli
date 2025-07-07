import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import json
import global_params


def license_key_activation():
    
    lic_key = str(input("License key: "))
    
    payload = json.dumps({
        "lic_key": lic_key
    })
    
    with open("License_keys/lic_key.txt", 'w') as f:
        f.write(lic_key)
    
    response = requests.post(f"{global_params.get_url()}/license/key", headers=global_params.get_user_hader(), data=payload)
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get("message"))
        sys.exit()
    else:
        print(data_response.get("message") + ".")
    
    hw_id = data_response.get("hw_id")
    with open("License_keys/hw_id.txt", 'w') as f:
        f.write(hw_id)


def generate_hw_key():
    
    user_id = str(input("User ID: "))
    
    with open("License_keys/hw_id.txt", 'r') as f:
        hw_id = f.read()
    
    with open("License_keys/lic_key.txt", 'r') as f:
        lic_key = f.read()

    payload = json.dumps({
        "hw_id":hw_id,
        "lic_key":lic_key,
        "user-id":user_id
    })
    
    response = requests.post("https://lic.lasting.space/license/activation", headers=global_params.get_header(), data=payload)
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get("message"))
        sys.exit()
    else:
        print("Hardware key was generated.")
    
    hw_key = data_response.get("hw_key")
    with open("License_keys/hw_key", 'w') as file:
        file.write(hw_key)
    


def hardware_key_activation():
    
    with open("License_keys/hw_key", 'r') as f:
        hw_key = f.read()
    
    payload = json.dumps({
        "hw_key":hw_key
    })
    
    response = requests.post(f"{global_params.get_url()}/license/activation", headers=global_params.get_user_hader(), data=payload)
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get("message"))
        sys.exit()
    else:
        print("Hardware key is valid. License is activated!")
    
    
if __name__ == "__main__":
    license_key_activation()
    generate_hw_key()
    hardware_key_activation()
