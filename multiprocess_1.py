import time
import multiprocessing
from typing import List


def task(name):
    print(f"Process {name} is starting")
    time.sleep(3)
    print(f"Process {name} is done. Result ends")


if __name__ == '__main__':
    start_time = time.perf_counter()

    # p1 = multiprocessing.Process(target=task, args=('A',))
    # p2 = multiprocessing.Process(target=task, args=('B',))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    task_list: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    process_list: List = []
    for task_name in task_list:
        process = multiprocessing.Process(target=task, args=(task_name,))
        process.start()
        process_list.append(process)

    for task_l in process_list:
        task_l.join()

    end_time = time.perf_counter()
    print(f"Both processes are complete. Total time: {round(end_time - start_time, 2)} seconds")
