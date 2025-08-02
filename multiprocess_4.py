import multiprocessing
import time


def worker(name: str, result_queue: multiprocessing.Queue):
    """
    Simulates a time-consuming task and puts the result into the queue.
    Each worker will send its result back to the main process via the queue.
    """
    print(f"[{name}] started.")
    time.sleep(2)  # Simulate some processing time
    result = f"{name} completed at {time.ctime()}"
    result_queue.put(result)  # Send result to the main process
    print(f"[{name}] finished and sent result.")


if __name__ == '__main__':
    # Create a Queue for inter-process communication (IPC)
    result_queue = multiprocessing.Queue()

    processes = []
    names = ['Worker-A', 'Worker-B', 'Worker-C']

    # Spawn a process for each worker
    for name in names:
        p = multiprocessing.Process(target=worker, args=(name, result_queue))
        p.start()
        processes.append(p)

    # Collect results from the queue
    for _ in names:
        # Blocks until a result is available
        result = result_queue.get()
        print(f"[Main Process] Received result: {result}")

    # Ensure all worker processes have completed
    for p in processes:
        p.join()

    print("✅ All worker processes are complete.")
