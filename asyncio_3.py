import asyncio

# -------------------------------
# Simulates an async worker that sets a value into a Future after some delay
# -------------------------------
async def set_future_result(future, value):
    # Simulate some delay before the result is ready
    await asyncio.sleep(2)
    
    # Set the result in the Future object (like filling a box that someone else is waiting to open)
    future.set_result(value)
    
    print(f"[Setter] Future is now ready with value: {value}")


# -------------------------------
# Main async function where we wait for a result from another task
# -------------------------------
async def main():
    # Get the current event loop (the brain of asyncio that runs tasks)
    loop = asyncio.get_running_loop()

    # Create a new empty Future object (like an empty box to be filled later)
    future = loop.create_future()

    # Start a background task that will "fill" the future box after 2 seconds
    asyncio.create_task(set_future_result(future, "✅ This is the result!"))

    print("[Main] Waiting for the result...")

    # This line pauses until the Future gets a result (someone fills the box)
    result = await future

    print(f"[Main] Got the result from Future: {result}")


# -------------------------------
# Entry point: Run the main coroutine using asyncio's event loop
# -------------------------------
asyncio.run(main())
