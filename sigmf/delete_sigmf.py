import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import global_params


def delete_sigmf_from_keyboard():
    
    file = str(input("Insert sigMF file you want to delete: "))
    delete_sigmf(file)
    

def delete_sigmf(file):
    
    response = requests.delete(f"{global_params.get_url()}/sigmf/{file}", headers=global_params.get_user_hader())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(f"Did not delete sigMF file. {data_response.get('message')}")
        # response.raise_for_status()
        return False

    else:
        print(data_response["message"])
    
    
if __name__ == "__main__":
    delete_sigmf_from_keyboard()