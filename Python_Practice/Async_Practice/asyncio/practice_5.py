import asyncio

async def slow_task():
    print("Task Started")
    await asyncio.sleep(10)
    print("Task Finished")



async def main():
    try:
        await asyncio.wait_for(slow_task(), timeout=3)
    except asyncio.TimeoutError:
        print("Task Timeout! Task cancelled")


asyncio.run(main())