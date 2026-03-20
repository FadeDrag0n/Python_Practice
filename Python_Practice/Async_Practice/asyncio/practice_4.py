import asyncio

async def producer(queue):
    for i in range(1, 11):
        print(f'Producer put {i}')
        await queue.put(i)
        await asyncio.sleep(0.5)
    print('Producer finished')


async def consumer(queue):
    while True:
        item = await queue.get()
        print(f'Consumer takes: {item}')
        queue.task_done()
        if item == 10:
            print('Consumer finished')
            break


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())