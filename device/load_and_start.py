import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import json
import global_params
import datetime
import time


def load_profile_from_file(profile_path):
    
    payload = global_params.read_from_file(file_path=profile_path)
    profile_name = load_profile(payload)
    return profile_name


def load_profile(payload: json):
    
    #Write the profile name you want to load
    # payload = json.dumps({
    #     "name": profile_name
    # })
    
    response = requests.post(f"{global_params.get_url()}/device", headers=global_params.get_user_hader(), data=payload)
    data_response = response.json()
    
    if response.status_code != 200:
        print(f"Scenario was not loaded. {data_response.get('message')}. Try again.")
        response.raise_for_status()
    else:
        print("Scenario loaded on the emulator.")
        
    return payload


def load_profile_as_string(profile_name: str):
    
    #Write the profile name you want to load
    payload = json.dumps({
        "name": profile_name
    })
    
    response = requests.post(f"{global_params.get_url()}/device", headers=global_params.get_user_hader(), data=payload)
    data_response = response.json()
    
    if response.status_code != 200:
        print(f"Scenario was not loaded. {data_response.get('message')}. Try again.")
        response.raise_for_status()
    else:
        print("Scenario loaded on the emulator.")
        
    return payload
        

def start_emulation(tenMHz: bool = False, pps: bool =  False, gps: bool = False, timestamp: str = "1970-01-01T00:00:00.000Z"):
    
    #Optional external syncronization settingg
    current_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    payload = json.dumps({"10mhz": tenMHz,
                            "pps": pps,
                            "gps": gps,
                            "timestamp": timestamp})
    
    response = requests.put(f"{global_params.get_url()}/device", headers=global_params.get_user_hader(), data=payload)
    data_response = response.json()
    
    if response.status_code != 200:
        print(f"{data_response.get('message')}")
        response.raise_for_status()
    else:
        print("Process is starting...")
        

def start_emulation_from_file(sync_file):
    
    syncronization = global_params.read_from_file(sync_file)
    start_emulation(syncronization)
    

#This function will turn true eve if the emulation crashes after starting
def check_if_starts(start_time, timeout):
    
    has_started = False
    while not has_started:
        response_logs = requests.get(f'{global_params.get_url()}/status/log', headers = global_params.get_user_hader())
        logs = response_logs.json()
            
        if time.time() - start_time > timeout:
            raise TimeoutError(f"The expected message 'Emulation ongoing.' was not received within the timeout period. Logs: {logs['list'][-1]['message']}")
        
        for message_json in logs['list']:
            #print(message_json)
            if message_json.get("message") == "Emulation ongoing.":
                
                print("Emulation has started.")
                has_started = True
        
        time.sleep(1)  
    

if __name__ == "__main__":
    start_time = time.time()
    timeout = 25
    load_profile_from_file("device/load_profile.json")
    #You can optionally add external syncronization as function arguments
    # start_emulation(tenMHz = <True | False>, pps = <True | False>, gps = <True | False>, timestamp = <timestamp_as_string>)
    start_emulation()
    check_if_starts(start_time, timeout)