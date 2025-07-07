import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import signal
from device import stop_emulation, force_stop_emulation

def signal_handler(sig, frame):
    print(f"\nSignal {sig} received.")
    if signal_handler.received_stop_signal:
        print("Force stopping emulation...")
        force_stop_emulation()
        sys.exit(3)
    else:
        signal_handler.received_stop_signal = True
        print("Attempting graceful shutdown...")
        stop_emulation()
        exit()
        # time.sleep(5)
        # if not check_status_state():
        #     print("Emulation stopped gracefully.")
        #     sys.exit(0)
        # else:
        #     print("Graceful shutdown failed. Forcing stop...")
        #     force_stop_emulation()
        #     sys.exit(2)

signal_handler.received_stop_signal = False
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)   