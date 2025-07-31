import time
import threading

# ------------------------------------------------------------------------------
# Python Threading Demonstration with GIL Considerations
# ------------------------------------------------------------------------------

# Start high-precision timer to measure execution duration
start_time = time.perf_counter()

def running_task(task_name: str = "Default Task"):
    """
    Simulates a time-consuming task using time.sleep(),
    which is an I/O-bound operation.

    Args:
        task_name (str): Description of the task for tracking.
    """
    print(f"[START] Task: {task_name}")
    print(" -> Simulating I/O-bound work: sleeping for 1 second...")
    time.sleep(1)
    print(f"[END] Task: {task_name}")

# ------------------------------------------------------------------------------
# Python Threading Notes:
#
# 1. Threads in Python run *concurrently*, not in true *parallel* due to the GIL.
# 2. The Global Interpreter Lock (GIL) ensures that only one thread executes
#    Python bytecode at a time, even on multi-core systems.
# 3. Threads are ideal for I/O-bound tasks (e.g., waiting on file/network/disk),
#    because the GIL is released during such operations (like time.sleep()).
# 4. For CPU-bound tasks (e.g., heavy computation), use multiprocessing instead.
# ------------------------------------------------------------------------------

# --- Sequential Execution Example ---
# Uncomment below to compare synchronous behavior
# running_task("Walking")
# running_task("Testing")

# --- Concurrent Execution Using Threads ---
# Each thread will simulate an independent task
thread1 = threading.Thread(target=running_task, args=("Walking",))
thread2 = threading.Thread(target=running_task, args=("Testing",))

# Start both threads — tasks begin execution concurrently
thread1.start()
thread2.start()

# Block main thread until both threads complete execution
thread1.join()
thread2.join()

# Measure total time taken
end_time = time.perf_counter()
print(f"\n[INFO] All tasks completed in {round(end_time - start_time, 4)} seconds.")

# Threading Result Store:
# Shared results # Shared dictionary to hold results
results = {}

def my_task(name, x):
    time.sleep(2)
    result = x * 2
    results[name] = result  # Store result using thread name

# Create threads with custom names
t1 = threading.Thread(target=my_task, args=("Thread-1", 10), name="Thread-1")
t2 = threading.Thread(target=my_task, args=("Thread-2", 20), name="Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()

# Fetch result by thread name
print("Result from Thread-1:", results["Thread-1"])
print("Result from Thread-2:", results["Thread-2"])


# Thread Termination:

# Create a termination signal (shared between main and thread)
stop_event = threading.Event()

def long_running_task():
    print("Thread started.")
    while not stop_event.is_set():
        print("Working...")
        time.sleep(1)
    print("Thread received stop signal. Exiting...")

# Start thread
worker = threading.Thread(target=long_running_task)
worker.start()

# Let it run for 5 seconds
time.sleep(5)

# Signal the thread to stop
print("Sending stop signal...")
stop_event.set()

# Wait for thread to exit
worker.join()
print("Thread terminated.")


# Another Method: Using Flag
# Shared flag
should_stop = False

def long_running_task():
    global should_stop
    print("Thread started.")
    while not should_stop:
        print("Working...")
        time.sleep(1)
    print("Thread received stop signal. Exiting...")

# Start the thread
worker = threading.Thread(target=long_running_task)
worker.start()

# Let it run for 5 seconds
time.sleep(5)

# Set the flag to stop the thread
print("Sending stop signal...")
should_stop = True

# Wait for the thread to finish
worker.join()
print("Thread terminated.")
