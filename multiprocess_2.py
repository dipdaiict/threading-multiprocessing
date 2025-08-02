import time
import concurrent.futures
from typing import List


def task(name: str) -> str:
    """
    Simulates a CPU-bound or IO-bound task by sleeping for 3 seconds.
    """
    print(f"Process {name} is starting")
    time.sleep(3)
    return f"Process {name} is done. Result ends"


if __name__ == '__main__':
    start_time = time.perf_counter()

    # List of task names to process in parallel
    task_list: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    # Create a process pool with a maximum of 3 workers.
    # Only 3 tasks will run in parallel at any time.
    # If max_workers is not set, it uses the number of CPU cores by default.
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # Submit all tasks to the process pool
        future_results = [executor.submit(task, task_name) for task_name in task_list]

        # Process the results as they are completed (not in submission order)
        for future in concurrent.futures.as_completed(future_results):
            print(f"Result: {future.result()}")

    end_time = time.perf_counter()
    print(f"All processes are complete. Total time: {round(end_time - start_time, 2)} seconds")
