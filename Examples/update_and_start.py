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
    name = scenario.update_scenario_from_file("Examples/updated_profile.json")
    device.load_profile_as_string(name)
    device.start_emulation()
    device.check_if_starts(start_time, timeout)
    print("\nEmulation is running. Press Ctrl+C to stop.")
    time.sleep(3600)