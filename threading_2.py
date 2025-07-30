import time
import random
import threading
import concurrent.futures

start_time = time.perf_counter()


# def do_something(seconds: float = 1.5):
#     print(f" -> Simulating I/O-bound work: sleeping for {seconds} s...")
#     time.sleep(seconds)
#     print("[✓] Task Completed.")


# threads = []

# for _ in range(10):
#     thread = threading.Thread(target=do_something, args=(2.0,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

def do_something(seconds: float = 1.5):
    print(f" -> Simulating I/O-bound work: sleeping for {seconds} s...")
    time.sleep(seconds)
    return random.randint(1, 10)


# # Using Built ion Library:
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # f1 = executor.submit(do_something, 2.0)
#     # print(f1.result())
#     threads = [executor.submit(do_something, 1.5) for _ in range(10)]
    
#     # Now collection result:
#     for thread in threads:
#         print(thread.result())

# Mapping:
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [2.5, 4, 1, 7, 5]
    results = executor.map(do_something, secs)

    # Now collection result:
    for result in results:
        print(result)


end_time = time.perf_counter()
print(f"\n[INFO] All tasks completed in {round(end_time - start_time, 4)} seconds.")
