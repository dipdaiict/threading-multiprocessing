import multiprocessing
import time
import os


def queue_worker(q: multiprocessing.Queue):
    """
    🧵 Worker that puts data into a multiprocessing.Queue.
    Queue is useful for sharing data safely between processes.
    The main process will read items from the queue.
    """
    for i in range(5):
        msg = f"[Queue Worker PID {os.getpid()}] -> Sending: {i}"
        print(msg)
        q.put(msg)  # ✅ Putting message into Queue
        time.sleep(1)  # Simulate some work
    q.put(None)  # ✅ Sentinel value to signal completion


def pipe_worker(conn):
    """
    🧵 Worker that communicates using a multiprocessing.Pipe.
    Pipe is used for two-way communication between two processes.
    The main process will read from the other end of the pipe.
    """
    for i in range(3):
        msg = f"[Pipe Worker PID {os.getpid()}] -> Sending: Hello {i}"
        print(msg)
        conn.send(msg)  # ✅ Sending message via Pipe
        time.sleep(2)
    conn.send("DONE")  # ✅ Signal end of messages
    conn.close()       # ✅ Always close the pipe


if __name__ == '__main__':
    # === Queue setup ===
    # Queue allows multiple producers/consumers; safe to use with multiple processes
    queue = multiprocessing.Queue()
    q_process = multiprocessing.Process(target=queue_worker, args=(queue,))

    # === Pipe setup ===
    # Pipe is a two-way communication channel between two processes
    parent_conn, child_conn = multiprocessing.Pipe()
    p_process = multiprocessing.Process(target=pipe_worker, args=(child_conn,))

    # Start both worker processes
    q_process.start()
    p_process.start()

    # --- Handle Queue messages ---
    print("\n🔄 Listening to Queue (from Queue Worker)...")
    while True:
        item = queue.get()  # ⬅️ Receiving data from the queue
        if item is None:    # Sentinel value
            break
        print(f"🟩 Received from Queue: {item}")

    # --- Handle Pipe messages ---
    print("\n🔄 Listening to Pipe (from Pipe Worker)...")
    while True:
        if parent_conn.poll():          # Check if there's data in the pipe
            msg = parent_conn.recv()    # ⬅️ Receiving data from the pipe
            if msg == "DONE":           # End of communication
                break
            print(f"🟦 Received from Pipe: {msg}")
        time.sleep(0.1)

    # Wait for both workers to finish
    q_process.join()
    p_process.join()

    print("\n✅ All communications done. Main process exiting.")
