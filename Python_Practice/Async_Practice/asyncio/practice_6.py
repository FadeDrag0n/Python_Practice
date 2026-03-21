import asyncio
import random

async def timer(max_time):
    for i in range(max_time):
        await asyncio.sleep(1)
        print(f'{i} seconds passed')

async def main():
    task1 = asyncio.create_task(timer(200))
    task2 = asyncio.create_task(timer(200))
    task3 = asyncio.create_task(timer(200))
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())