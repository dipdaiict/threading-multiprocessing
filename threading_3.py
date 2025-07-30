import time
import threading


# ------------------------------------------------------------------------------
# Task: Print current thread info including name, thread ID, and native ID
# ------------------------------------------------------------------------------
def do_task(task_name: str):
    time.sleep(1)
    current_thread = threading.current_thread()
    print(f"\n[THREAD: {current_thread.name}]")
    print(f" -> Task: {task_name}")
    print(f" -> thread.ident       = {threading.get_ident()}")
    print(f" -> thread.native_id   = {threading.get_native_id()}")

# ------------------------------------------------------------------------------
# Creating threads using lambda to pass arguments dynamically
# ------------------------------------------------------------------------------

# Create and start two named threads with custom task names
th_foo = threading.Thread(name="Worker-1", target=lambda: do_task("Process Data"))
th_bar = threading.Thread(name="Worker-2", target=lambda: do_task("Fetch API"))

th_foo.start()
th_bar.start()

# Print thread metadata from main thread after start
print("\n[MAIN THREAD]")
print(f"foo's name:        {th_foo.name}")
print(f"foo's ident:       {th_foo.ident}")
print(f"foo's native_id:   {th_foo.native_id}")

print(f"bar's name:        {th_bar.name}")
print(f"bar's ident:       {th_bar.ident}")
print(f"bar's native_id:   {th_bar.native_id}")

# Wait for both threads to finish
th_foo.join()
th_bar.join()

print("\n[INFO] Both threads have completed.")
