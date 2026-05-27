import httpx

from kd_scraper_core.core.base_crawler import BaseCrawler
from kd_scraper_core.core.constants import ( DEFAULT_HEADERS, DEFAULT_TIMEOUT, )

class HttpCrawler(BaseCrawler):
  async def fetch(self, url: str) -> str:
    async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT, headers=DEFAULT_HEADERS) as client:
      response = await client.get(url)

      response.raise_for_status()

      return response.text
