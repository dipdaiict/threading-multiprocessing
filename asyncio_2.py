import asyncio


# Simulate an async task that may raise an exception
async def risky_task(name: str, delay: int, fail: bool = False):
    print(f"Starting {name} (delay={delay}, fail={fail})")
    await asyncio.sleep(delay)

    if fail:
        raise RuntimeError(f"{name} failed due to an error!")

    print(f"Completed {name}")
    return f"{name} result"


# Main coroutine using TaskGroup
async def main():
    print("Starting multiple tasks in a TaskGroup...\n")

    results = []  # To collect results from successful tasks

    try:
        async with asyncio.TaskGroup() as tg:
            # Dictionary to track task names with actual asyncio Tasks
            task_map = {
                "task_a": tg.create_task(risky_task("Task-A", delay=3)),
                "task_b": tg.create_task(risky_task("Task-B", delay=2)),
                "task_c": tg.create_task(risky_task("Task-C", delay=1, fail=True)),  # This will fail early then all other task failed.
            }

        # If we reach here, all tasks succeeded
        for name, task in task_map.items():
            results.append((name, task.result()))

        print("\nAll tasks completed successfully!")
        print("Results:")
        for name, res in results:
            print(f"{name}: {res}")

    except* Exception as group_errors:
        print("\nOne or more tasks raised exceptions:")
        for err in group_errors.exceptions:
            print(" -", err)

    print("\nProgram continues after handling TaskGroup errors.\n")


# Entry point
if __name__ == "__main__":
    asyncio.run(main())
