import httpx

from kd_scraper_core.core.exceptions import FetchError
from kd_scraper_core.core.models import FetchResult
from kd_scraper_core.core.base_crawler import BaseCrawler
from kd_scraper_core.core.logger import get_logger
from kd_scraper_core.core.constants import (
    DEFAULT_HEADERS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
)

logger = get_logger()


class HttpCrawler(BaseCrawler):
    async def fetch(self, url: str) -> FetchResult:
        logger.info("Fetching resource: %s", url)
        for attempt in range(DEFAULT_MAX_RETRIES):
            try:
                async with httpx.AsyncClient(
                    timeout=DEFAULT_TIMEOUT, headers=DEFAULT_HEADERS
                ) as client:
                    response = await client.get(url)

                    response.raise_for_status()

                    return FetchResult(
                        url=url,
                        content=response.text,
                        status_code=response.status_code,
                        response_time=response.elapsed.total_seconds(),
                        headers=response.headers,
                    )

            except httpx.HTTPError as error:
                if attempt == DEFAULT_MAX_RETRIES - 1:
                    logger.error(
                        "Failed to retrieve resource after %d attempts: %s",
                        DEFAULT_MAX_RETRIES,
                        url,
                    )
                    raise FetchError(f"Failed to retrieve resource: {url}") from error
