# This will help during shared resource handling writing files and db connection like that so with lock at a single coroutine work on it.
import asyncio

# Shared counter variable
counter = 0

# Lock to prevent simultaneous access
lock = asyncio.Lock()


# Simulates some async work that increments a shared counter
async def increment(name: str, use_lock: bool):
    global counter
    for _ in range(1000):
        if use_lock:
            async with lock:
                temp = counter
                await asyncio.sleep(0.0001)  # Simulate delay
                counter = temp + 1
        else:
            temp = counter
            await asyncio.sleep(0.0001)  # Simulate delay
            counter = temp + 1

    print(f"{name} finished incrementing.")


async def main():
    global counter

    print("🚫 Running without lock:")
    counter = 0
    await asyncio.gather(
        increment("Task-1", use_lock=False),
        increment("Task-2", use_lock=False)
    )
    print("Final Counter (no lock):", counter)  # ❌ Should be 2000

    print("\n✅ Running with lock:")
    counter = 0
    await asyncio.gather(
        increment("Task-1", use_lock=True),
        increment("Task-2", use_lock=True)
    )
    print("Final Counter (with lock):", counter)  # ✅ Will be 2000


# Run the main function
asyncio.run(main())
