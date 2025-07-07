import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import global_params
import json


def get_profiles_from_keyboard():
    
    profiles = input("Profiles: ")
    profile_list = profiles.split()
    if isinstance(profile_list, list) and all(isinstance(item, str) for item in profile_list):
        pass
    else:
        print("Please enter a valid list of profiles.")
        sys.exit()
    return profile_list


def delete_scenarios_from_file(delete_file):
    
    req_body = global_params.read_from_file(file_path=delete_file)
    profile_list = json.loads(req_body)
    delete_scenario_list(profile_list["items"])


def delete_scenario_list(profile_list: list):
    
    payload = {
        "items": profile_list
    }
    
    #print(payload)
    response = requests.delete(f"{global_params.get_url()}/scenario/many", headers=global_params.get_user_hader(), json = payload)
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(f"Could not delete scenarios. Ignored profiles: {data_response.get('Ignored')}")
        response.raise_for_status()
    else:
        print(data_response["message"])
    return profile_list
    
    
if __name__ == "__main__":
    list = get_profiles_from_keyboard()
    delete_scenario_list(list)
    