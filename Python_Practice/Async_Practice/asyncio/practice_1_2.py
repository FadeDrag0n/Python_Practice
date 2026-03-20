import asyncio

async def say_hello(name, time):
    await asyncio.sleep(time)
    print(f'Hello, {name}! Sleep time {time}')



async def main():
    # await say_hello('Alice', 10)
    # await say_hello('Bob', 2)
    # await say_hello('Charlie', 3)
    # await say_hello('David', 1)

    task1 = say_hello('Alice', 5)
    task2 = say_hello('Bob', 3)
    task3 = say_hello('Charlie', 1)
    task4 = say_hello('David', 2)

    await asyncio.gather(task1, task2, task3, task4)

asyncio.run(main())