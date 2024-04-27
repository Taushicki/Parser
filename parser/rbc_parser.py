import aiohttp
from loging_config import setup_logging
setup_logging()
import logging
import asyncio
from typing import Dict
from settings import settings
import xml.etree.ElementTree as ET
from models.news import Content
from apikit import ApiTools
from parser.create_content import create

class Parser:
    async def fetch_page(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
            
    async def parse(self):
        news_list: Dict[str, Content] = {}
        try:
            for item in ET.fromstring(await self.fetch_page(settings.rbc_url)).findall('.//item'):
                content = create(item)
                if content != None:
                    news_list[item.find('.//{https://www.rbc.ru}news_id').text] = content
            ApiTools().send_data_via_api(news_list, get_status=True)
        except Exception as error:
            logging.error(error, exc_info=True)

async def parse():
    while True:
        await Parser().parse()
        await asyncio.sleep(300) 
