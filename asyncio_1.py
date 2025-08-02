import time
import asyncio


# ---------------------------------------------
# Coroutine function that simulates a task with non-blocking sleep
# This function does not block the main thread during sleep
# ---------------------------------------------
async def do_something_async(name: str, sleep_time: int):
    print(f"{name} started (sleeping {sleep_time} seconds)...")
    await asyncio.sleep(sleep_time)  # Non-blocking sleep
    print(f"{name} finished after {sleep_time} seconds")
    return name


# ---------------------------------------------
# Synchronous function that simulates a blocking task
# This will block the main thread completely during sleep
# ---------------------------------------------
def do_something_sync(name: str, sleep_time: int):
    print(f"{name} started (sleeping {sleep_time} seconds)...")
    time.sleep(sleep_time)  # Blocking sleep
    print(f"{name} finished after {sleep_time} seconds")
    return name


# ---------------------------------------------
# Main async function to demonstrate both:
#   1. Sequential async execution (same as sync but non-blocking)
#   2. Concurrent async execution using asyncio.create_task()
# ---------------------------------------------
async def main():
    print("\nStep 1: Sequential Async Execution (like synchronous behavior)")
    
    # Tasks run one after another (total time ~8 seconds)
    # These are still non-blocking from an OS perspective but executed sequentially
    result1 = await do_something_async("Task-A", 5)
    result2 = await do_something_async("Task-B", 3)
    print(f"[Sequential Execution] Results: {result1}, {result2}")

    print("\nStep 2: Concurrent Async Execution using asyncio.create_task()")

    # Tasks start concurrently and run on the same thread
    # Each coroutine yields control during sleep, enabling smart context switching
    task1 = asyncio.create_task(do_something_async("Task-A", 5))
    task2 = asyncio.create_task(do_something_async("Task-B", 3))

    print("Both tasks are now scheduled concurrently...\n")

    # Wait for both tasks to complete and collect their results
    result1 = await task1
    result2 = await task2
    print(f"[Concurrent Execution] Results: {result1}, {result2}")

    # Optional: You can also use asyncio.gather() as a cleaner alternative
    # Uncomment the following lines to use gather instead of create_task

    # print("\nStep 3: Multiple Concurrent Execution using asyncio.gather()")
    # results = await asyncio.gather(
    #     do_something_async("Task-A", 5),
    #     do_something_async("Task-B", 3)
    # )
    # print(f"[Using gather] Results: {results}")

# ---------------------------------------------
# Entry point of the program
# The event loop is started here
# ---------------------------------------------
if __name__ == "__main__":
    asyncio.run(main())
