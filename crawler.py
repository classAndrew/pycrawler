import aiohttp
import asyncio
import re
import lxml.etree as etree
from httpwraper import SessionWrapper
import time

class Crawler:

    def __init__(self, starting_link, session):
        self._start_link = starting_link
        self.http = SessionWrapper(session)
        self.collected_links = []

    async def start(self, depth, n_calls):
        # Iterative
        total_links = [await self.http.search(await self.http.fetch(self._start_link)), *[[]]*(depth)]
        i = 0
        calls = 0
        while i < depth and calls < n_calls:
            tasks = []
            for link in total_links[i]:
                if calls >= n_calls:
                    break
                tasks.append(asyncio.create_task(self.http.fetch_search(link)))
                calls += 1
                
            all_links = await asyncio.gather(*tasks)
            all_links = [y for x in all_links for y in x] # flatten
            total_links[i+1] += all_links
            i += 1
        total_links = [y for x in total_links for y in x] # flatten again
        self.collected_links = total_links
        return self.collected_links

    def _assign_tasks(self, data, task):
        return [asyncio.ensure_future(task(piece)) for piece in data]

    def write_out(self, fn):
        with open(fn, "w") as f:
            f.write('\n'.join(link for link in self.collected_links if link))
                


async def main():
    pass
        
        
    


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(main())
    loop.run_until_complete(future)
