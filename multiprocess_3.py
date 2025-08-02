import os
import time
import multiprocessing
from multiprocessing import Lock

data_diir = os.path.join(os.getcwd(), "data")


def write_to_file(task_name: str, lock: Lock):
    """
    Each process tries to write its name to a shared file.
    The lock ensures only one process writes at a time.
    """
    print(f"{task_name} wants to write")
    with lock:
        print(f"{task_name} is writing...")
        with open(os.path.join(data_diir, "output.txt"), "a") as f:
            f.write(f"{task_name} started at {time.ctime()}\n")
        time.sleep(1)  # simulate delay in writing
        print(f"{task_name} finished writing")


if __name__ == '__main__':
    lock = Lock()

    processes = []
    task_names = ['Task-A', 'Task-B', 'Task-C', 'Task-D']

    for name in task_names:
        p = multiprocessing.Process(target=write_to_file, args=(name, lock))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("All processes finished.")
