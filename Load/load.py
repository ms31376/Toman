import asyncio
import nest_asyncio
import aiohttp
import time

# Configuration
API_URL = 'https://api.digikala.com/v1/user/authenticate/'  
CONCURRENT_REQUESTS = 255  
RATE_LIMIT_SLEEP = 60  

# Allow nested asyncio loops
nest_asyncio.apply()

async def fetch(session, url, headers, payload):
    async with session.post(url, headers=headers, json=payload) as response:
        return response.status, await response.text()

async def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    payload = {
        "username": "09306823848",
        "otp_call": False,
        "hash": None
    }

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(CONCURRENT_REQUESTS):
            tasks.append(fetch(session, API_URL, headers, payload))

        start_time = time.time()
        responses = await asyncio.gather(*tasks)
        end_time = time.time()

        for index, content in enumerate(responses):
            print(f"Request #{index + 1} | Status: {content[0]}, Response (truncated): {content[1][:100]}")

        print(f"\nTotal time: {end_time - start_time:.2f} seconds")
        rate_limited_count = len([r for r in responses if r[0] == 429])
        print(f"Rate Limited Responses: {rate_limited_count}")

        if rate_limited_count == 0:
            print('Everything is OK')
        else:
            print(f"{rate_limited_count} requests were rate limited. Waiting {RATE_LIMIT_SLEEP}s...")
            await asyncio.sleep(RATE_LIMIT_SLEEP)
            await main()  # recursive retry

# Run the test
asyncio.run(main())
