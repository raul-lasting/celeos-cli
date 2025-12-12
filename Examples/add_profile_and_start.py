import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time, signal
import scenario 
import device 
import signal_handler


signal_handler.signal_handler.received_stop_signal = False
signal.signal(signal.SIGINT, signal_handler.signal_handler)
signal.signal(signal.SIGTERM, signal_handler.signal_handler)    
    

if __name__ == "__main__":
    start_time = time.time()
    timeout = 30
    profile_name = scenario.add_scenario_from_file("Examples/add_profile.json")
    time.sleep(5)
    print("The selected profile is ", profile_name)
    device.load_profile_as_string(profile_name)
    device.start_emulation()
    device.check_if_starts(start_time, timeout)
    print("\nEmulation is running. Press Ctrl+C to stop.")
    time.sleep(3600)