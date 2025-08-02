import asyncio

## Semaphore

# # Allow max 3 tasks to run concurrently
# semaphore = asyncio.Semaphore(2)

# # Simulate a limited resource like a downloader or API call
# async def limited_worker(name):
#     print(f"[{name}] Waiting for permission...")
    
#     # Only 3 tasks can enter this block at a time
#     async with semaphore:
#         print(f"[{name}] Got access! Working...")
#         await asyncio.sleep(5)  # Simulate I/O work
#         print(f"[{name}] Done!")

# # Main coroutine that launches multiple tasks
# async def main():
#     tasks = [limited_worker(f"Worker-{i}") for i in range(1, 7)]
#     await asyncio.gather(*tasks)

# # Run the asyncio program
# asyncio.run(main())


## Event:

# Create an event — initially unset (like a red light)
event = asyncio.Event()


# A task that waits for the event to be set (green light)
async def waiting_task():
    print("[Waiter] Waiting for the event to be set...")
    await event.wait()  # Pause until the event is set
    print("[Waiter] Event is set! Resuming work...")


# A task that sets the event after a delay
async def trigger_task():
    await asyncio.sleep(3)  # Simulate some delay or condition
    print("[Trigger] Setting the event now!")
    event.set()  # Signal others to proceed


# Main function to run both tasks
async def main():
    await asyncio.gather(waiting_task(), trigger_task())


# Start the asyncio program
asyncio.run(main())
