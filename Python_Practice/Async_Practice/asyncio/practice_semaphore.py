import asyncio


async def say_hello(timeout):
    await asyncio.sleep(timeout)
    print(f"Hello! After {timeout} seconds")

async def main():
    async with asyncio.TaskGroup() as group:
        for i in range(10, 0, -1):
            group.create_task(say_hello(i))

asyncio.run(main())