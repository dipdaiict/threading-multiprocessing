# Thread Saftey:

import os
import threading
import concurrent.futures

data = os.path.join(os.getcwd(), "data")
os.makedirs(data, exist_ok=True)
lock = threading.Lock()


def thread_safe_write(task_name):
    with lock:  # This ensure that only one thread can do this at a time
        with open(os.path.join(data, "output.log"), "a") as f:
            f.write(f"{task_name} writing from thread {threading.current_thread().name}\n")


threads = [
    threading.Thread(target=thread_safe_write, args=(f"Task-{i}",), name=f"Worker-{i}")
    for i in range(5)]


for t in threads: 
    t.start()
for t in threads: 
    t.join()