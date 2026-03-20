import asyncio
from random import randint
import time

async def get_func(num):
    print(f'Task {num} Started')
    start = time.time()
    rand_time = randint(1, 3)
    await asyncio.sleep(rand_time)
    print(f'Task {num} Finished in {time.time() - start} seconds')

async def main():
   async with asyncio.TaskGroup() as group:
       for i in range(1, 6):
           group.create_task(get_func(i))


asyncio.run(main())