import multiprocessing
import time


def worker(name: str, start_event: multiprocessing.Event):
    """
    Worker waits until the event is set.
    """
    print(f"{name} is ready and waiting for the signal to start.")
    start_event.wait()  # Blocks here until event is set
    print(f"🚀 {name} started working at {time.ctime()}")
    time.sleep(2)
    print(f"✅ {name} finished.")


if __name__ == '__main__':
    # Create a shared event object
    start_event = multiprocessing.Event()

    processes = []

    # Create 3 worker processes
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(f"Worker-{i}", start_event))
        p.start()
        processes.append(p)

    # Simulate a delay before giving the go signal
    print("\n⏳ Main process is preparing something before giving the signal...")
    time.sleep(10)

    print("\n✅ Signal given! All workers can start.")
    start_event.set()  # Signal all waiting workers to continue

    # Wait for all workers to finish
    for p in processes:
        p.join()

    print("🎉 All workers finished.")
