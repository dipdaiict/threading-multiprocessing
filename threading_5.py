import threading
import time

# Create a global Event object
start_event = threading.Event()

def worker(name):
    print(f"{name} is waiting for the signal to start...")
    start_event.wait()  # Blocks until .set() is called
    print(f"{name} started working!")
    time.sleep(1)
    print(f"{name} finished working.")


# Create multiple threads
threads = [threading.Thread(target=worker, args=(f"Worker-{i}",)) for i in range(3)]

# Start threads (they will wait)
for t in threads:
    t.start()

print("Main thread is preparing something before starting workers...")
time.sleep(3)

print("\n[Main] All systems ready. Sending signal to all workers...\n")
start_event.set()  # Unblocks all waiting threads

# Wait for all to complete
for t in threads:
    t.join()

print("\n[Main] All worker threads have completed.")
