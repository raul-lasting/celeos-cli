import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import json
import global_params


def update_scenario_from_file(update_file):
    
    updated_profile = global_params.read_from_file(file_path=update_file)
    name = update_scenario(updated_profile)
    return name


def update_scenario(update_profile: json):
    
    response = requests.put(f"{global_params.get_url()}/scenario", headers=global_params.get_user_hader(), data=update_profile)
    
    data_response = response.json()
    
    profile_py = json.loads(update_profile)
    
    if response.status_code != 200:
        print(f"Could not update scenario. {data_response.get('message')}")
        response.raise_for_status()
    else:
        print("Profile has been updated.")
    
    if "new_name" in profile_py:
        return profile_py["new_name"]

    return profile_py["name"]
    
    
if __name__ == "__main__":
    update_scenario_from_file("scenario/updated_profile.json")