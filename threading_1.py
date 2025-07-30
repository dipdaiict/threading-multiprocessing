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
