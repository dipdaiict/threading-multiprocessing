import threading
import time
from threading import Timer, Semaphore, Condition
from queue import Queue

# Shared queue between producer and consumer
task_queue = Queue()

# Semaphore to limit concurrent consumers (e.g., only 3 threads allowed to process at a time)
sem = Semaphore(3)

# Condition object to coordinate between producer and consumers
condition = Condition()


def say_hello():
    print("\n[Timer] Hello! Timer executed after 5 seconds.\n")


def producer():
    """Produces 5 tasks with a delay and notifies consumers."""
    for i in range(5):
        time.sleep(1)
        item = f"Task-{i}"
        with condition:
            print(f"[Producer] Produced: {item}")
            task_queue.put(item)
            condition.notify()  # Notify a waiting consumer # Wake up a waiting consumer


def consumer(name):
    """Consumes tasks only when available, using semaphore and condition."""
    while True:
        with condition:
            while task_queue.empty(): 
                print(f"[{name}] No task yet. Waiting...")
                condition.wait()  # Wait until producer adds an item

            item = task_queue.get()

        # Limit concurrency using semaphore
        with sem:
            print(f"[{name}] Processing: {item}")
            time.sleep(2)  # Simulate I/O or compute work
            print(f"[{name}] Finished: {item}")
            task_queue.task_done()


if __name__ == "__main__":
    print("[Main] Starting threading demo...\n")

    # 1. Start timer to call say_hello after 5 seconds
    timer = Timer(5.0, say_hello)
    timer.start()

    # 2. Start consumers
    consumer_threads = [
        threading.Thread(target=consumer, args=(f"Consumer-{i}",), daemon=True)
        for i in range(3)
    ]
    for t in consumer_threads:
        t.start()

    # 3. Start the producer thread
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    # Wait for producer to finish
    producer_thread.join()

    # Wait for all tasks to be processed
    task_queue.join()

    print("\n[Main] All tasks completed. Exiting.\n")
