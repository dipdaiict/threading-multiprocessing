import time
from multiprocessing import Process

def task(name):
    print(f"Process {name} is starting")
    result = 1
    for i in range(1, 50000):
        result *= i
    print(f"Process {name} is done. Result ends")

if __name__ == '__main__':
    start_time = time.perf_counter()

    p1 = Process(target=task, args=('A',))
    p2 = Process(target=task, args=('B',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.perf_counter()
    print(f"Both processes are complete. Total time: {round(end_time - start_time, 2)} seconds")
