import asyncio
import random

# Shared queue between producers and consumers
queue = asyncio.Queue()


# Producer coroutine: puts items into the queue
async def producer(name: str, count: int):
    for i in range(count):
        # Simulate making some item
        await asyncio.sleep(random.uniform(0.1, 0.5))
        item = f"{name}-item-{i}"
        await queue.put(item)  # put item in queue (non-blocking if space available)
        print(f"✅ [Producer {name}] Produced: {item}")
    
    print(f"🛑 [Producer {name}] Done producing.")


# Consumer coroutine: takes items from the queue
async def consumer(name: str):
    while True:
        item = await queue.get()  # wait until item available
        print(f"🍽️ [Consumer {name}] Consumed: {item}")
        await asyncio.sleep(random.uniform(0.2, 0.6))  # simulate processing time
        queue.task_done()  # mark task as completed


# Main coroutine to run everything
async def main():
    # Launch producers and consumers
    producers = [asyncio.create_task(producer(f"P{i}", count=5)) for i in range(2)]
    consumers = [asyncio.create_task(consumer(f"C{i}")) for i in range(2)]

    # Wait for all producers to finish
    await asyncio.gather(*producers)

    # Wait for the queue to become empty (all items processed)
    await queue.join()

    # Cancel consumer tasks gracefully
    for c in consumers:
        c.cancel()

    print("✅ All items processed. Program complete.")

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
