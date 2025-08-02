# Sharing data:

import time
import multiprocessing


def worker(task_id: int, shared_list):
    """
    Simulates a worker that appends its result to a shared list.
    """
    print(f"Worker {task_id} started.")
    time.sleep(1)  # Simulate some work
    shared_list.append(f"Task-{task_id} done at {time.ctime()}")
    print(f"Worker {task_id} appended result.")


if __name__ == '__main__':
    # Create a manager to handle shared state
    with multiprocessing.Manager() as manager:
        # Create a shared list using the manager
        shared_results = manager.list()

        processes = []

        # Spawn multiple worker processes
        for i in range(5):
            p = multiprocessing.Process(target=worker, args=(i, shared_results))
            p.start()
            processes.append(p)

        # Wait for all processes to complete
        for p in processes:
            p.join()

        # Print the final shared results list
        print("\n✅ Final shared results collected by main process:")
        for result in shared_results:
            print(result)
