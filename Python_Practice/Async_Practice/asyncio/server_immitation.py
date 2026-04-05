import asyncio
import random


async def fetch_server_status(server_id, delay):
    await asyncio.sleep(delay)
    status = 'ok' if random.randint(1, 100) > 20 else 'error'
    return {"id": server_id, "status": status, "latency": delay}



async def monitor_servers(servers_):
    semaphore = asyncio.Semaphore(3)

    async def fetch_with_semaphore(server):
        async with semaphore:
            return await fetch_server_status(**server)

    tasks = [fetch_with_semaphore(s) for s in servers_]
    results = await asyncio.gather(*tasks)

    healthy = [r for r in results if r['status'] == 'ok']
    failed  = [r for r in results if r['status'] == 'error']
    return healthy, failed


async def retry_failed(servers_, retries=3):
    dead = []
    recovered = []

    for server in servers_:
        success = False
        for attempt in range(retries):
            await asyncio.sleep(1)
            result = await fetch_server_status(server['id'], server['latency'])
            if result['status'] == 'ok':
                recovered.append(result)
                success = True
                break
            print(f"[Retry {attempt + 1}] Server {server['id']} still failing...")

        if not success:
            dead.append({**server, "status": "dead"})

    return recovered, dead




async def dashboard(stats, interval=2):
    while True:
        await asyncio.sleep(interval)
        print(f"[Dashboard] Healthy: {stats['healthy']} | "
              f"Failed: {stats['failed']} | Dead: {stats['dead']}")


async def main():
    servers = [{"server_id": i, "delay": random.uniform(0.1, 1.5)} for i in range(10)]

    stats = {"healthy": 0, "failed": 0, "dead": 0}

    dash_task = asyncio.create_task(dashboard(stats, interval=2))

    healthy, failed = await monitor_servers(servers)
    stats["healthy"] = len(healthy)
    stats["failed"] = len(failed)

    recovered, dead = await retry_failed(failed)
    stats["healthy"] += len(recovered)
    stats["failed"] = 0
    stats["dead"] = len(dead)

    await asyncio.sleep(6)
    dash_task.cancel()


asyncio.run(main())