import multiprocessing
import time
from datetime import datetime


def current_time():
    """Returns the current time as a formatted string with seconds."""
    return datetime.now().strftime('%H:%M:%S')


def long_running_task():
    print(f"⏳ Task started at {current_time()}")
    time.sleep(25)  # This takes too long!
    print(f"✅ Task finished at {current_time()}")


if __name__ == '__main__':
    print(f"🚀 Main process started at {current_time()}")
    
    process = multiprocessing.Process(target=long_running_task)
    process.start()

    # Wait for 15 seconds max
    process.join(timeout=15)

    if process.is_alive():
        print(f"❌ Task is taking too long at {current_time()}! Terminating it...")
        process.terminate()
        process.join()
    else:
        print(f"✅ Task completed in time at {current_time()}")

    print(f"🔚 Main process exiting at {current_time()}")
