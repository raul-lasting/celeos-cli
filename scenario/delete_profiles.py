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

def choose_scenarios_from_list(scenarios):
    """
    Shows scenario names clearly and lets user choose by index.
    """

    if not scenarios:
        print("No scenarios found for this user.")
        sys.exit()

    print("\n======================")
    print("      YOUR SCENARIOS  ")
    print("======================")

    for i, item in enumerate(scenarios, start=1):
        name = item.get("name", "<no name>")
        print(f"{i}.  {name}")

    print("======================\n")

    raw = input("Enter scenario numbers to delete (example: 1 3 5): ")
    indexes = raw.strip().split()

    selected = []
    for idx in indexes:
        if not idx.isdigit():
            print(f"Ignoring invalid entry: {idx}")
            continue

        i = int(idx)
        if 1 <= i <= len(scenarios):
            selected.append(scenarios[i - 1]["name"])
        else:
            print(f"Index out of range: {i}")

    print("You selected:")
    for name in selected:
        print(" - " + name)

    print()
    return selected


def fetch_user_scenarios():
    response = requests.get(
        f"{global_params.get_url()}/scenario/list",
        headers=global_params.get_user_hader()
    )

    data = response.json()

    if isinstance(data, dict) and "items" in data:
        return data["items"]

    if isinstance(data, list):
        return data

    raise RuntimeError("Unexpected response format from /scenario/list")


def delete_scenario_list(profile_list: list):
    
    payload = {
        "items": profile_list
    }
    
    #print(payload)
    response = requests.delete(f"{global_params.get_url()}/scenario/many", headers=global_params.get_user_hader(), json = payload)
    
    try:
        data_response = response.json()
    except Exception:
        print("Server returned non-JSON response:")
        print(response.text)
        response.raise_for_status()

    if response.status_code != 200:
        print(f"Could not delete scenarios. Server response: {data_response}")
        response.raise_for_status()
    else:
        print(data_response["message"])
    return profile_list
    
    
if __name__ == "__main__":
    scenarios = fetch_user_scenarios()
    selected = choose_scenarios_from_list(scenarios)
    delete_scenario_list(selected)
