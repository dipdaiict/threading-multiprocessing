import multiprocessing
import time


def limited_worker(worker_id: int, semaphore: multiprocessing.Semaphore):
    """
    Each worker tries to access a limited shared resource.
    Semaphore ensures that only a limited number of workers
    can be inside the critical section at a time.
    """
    print(f"Worker-{worker_id} is waiting to acquire access...")

    # Acquire semaphore (blocks if limit is reached)
    with semaphore:
        # Only 2 workers can be inside this block at any time
        print(f"✅ Worker-{worker_id} entered the critical section (e.g., DB connection).")
        time.sleep(2)  # Simulating work with the shared resource
        print(f"⏹️ Worker-{worker_id} is leaving the critical section.")


if __name__ == '__main__':
    # Create a Semaphore with a limit of 2 concurrent accesses
    # Example: Only 2 DB connections allowed at a time
    sem = multiprocessing.Semaphore(2)

    processes = []

    # Start 5 worker processes
    for i in range(5):
        p = multiprocessing.Process(target=limited_worker, args=(i, sem))
        p.start()
        processes.append(p)

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print("🚀 All workers have finished their tasks.")
