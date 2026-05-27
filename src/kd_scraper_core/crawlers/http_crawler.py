import httpx

from kd_scraper_core.core.base_crawler import BaseCrawler

class HttpCrawler(BaseCrawler):
  async def fetch(self, url: str) -> str:
    async with httpx.AsyncClient(timeout=10.0) as client:
      response = await client.get(url)

      response.raise_for_status()

      return response.text
