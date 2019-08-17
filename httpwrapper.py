import aiohttp
import asyncio
import re
import lxml.etree as etree

class SessionWrapper:
    
    def __init__(self, session):
        self.session = session
        self.url = ""

    async def fetch(self, url):
        try:
            async with self.session.get(url) as res:
                self.url = url
                return await res.text()
        except Exception as e:
            print(e)
            return ""

    async def fetch_search(self, url):
        return await self.search(await self.fetch(url))

    async def search(self, data):
        try:
            html = etree.HTML(data)
        except:
            return []
        #print(html.xpath('//a/@href'))
        return [self.url+x if x[0] == "/" else x for x in html.xpath('//a/@href') if x and x[0] != "#" and x[0] != "."]