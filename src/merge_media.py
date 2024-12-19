import aiohttp
import asyncio
import sys

global total
global current
global out
out = []
total = 0
current = 0
bar_finished = False

# loading bar
async def update_loading_bar(description="Progress"):
    global current, total, bar_finished
    animation = ['|', '/', '*', '\\']
    bar_length = 50
    i = 0

    while not bar_finished:
        percentage = int((current / total) * 100) if total > 0 else 0
        num_hashes = percentage // 2
        animator = animation[i % len(animation)]
        bar = "#" * num_hashes + animator + "-" * (bar_length - num_hashes)
        progress_message = f"\r{description}: [{bar}] {percentage}%"
        sys.stdout.write(progress_message)
        sys.stdout.flush()
        i += 1
        if percentage == 100:
            bar_finished = True
            sys.stdout.write(progress_message[:-1])
            sys.stdout.flush()
        await asyncio.sleep(0.05)

    # finish the loading bar
    sys.stdout.write(progress_message + "\n")

async def main(list, name):
    global total
    # get the total number of episodes expected
    total = len(list['data']['media'])
    n_pages = list['data']['foundPages']

    if list['data']['hasNextPage']:
        async with aiohttp.ClientSession() as session:
            last_page_url = f"https://animeflv.ahmedrangel.com/api/search?query={name}&page={n_pages}"
            async with session.get(last_page_url) as response:
                last_page = await response.json()
                total += len(last_page['data']['media'])
                total += (n_pages - 2) * 24

    await merge(list, name)

# merge all results in a single array
async def merge(list, name):
    global current
    async with aiohttp.ClientSession() as session:
        for x in list['data']['media']:
            out.append(x)
            current = len(out)
            await asyncio.sleep(0)
        if list['data']['hasNextPage']:
            next_page = list['data']['currentPage'] + 1
            next_url = f"https://animeflv.ahmedrangel.com/api/search?query={name}&page={next_page}"
            async with session.get(next_url) as response:
                next_data = await response.json()
                await merge(next_data, name)
    return out
