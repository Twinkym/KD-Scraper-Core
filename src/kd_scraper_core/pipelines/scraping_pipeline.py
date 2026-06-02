from typing import Any

from kd_scraper_core.core.base_crawler import BaseCrawler
from kd_scraper_core.parsers.base_parser import BaseParser
from kd_scraper_core.pipelines.base_pipeline import BasePipeline


class ScrapingPipeline(BasePipeline):
    def __init__(
        self,
        crawler: BaseCrawler,
        parser: BaseParser,
        url: str,
    ) -> None:
        self._crawler = crawler
        self._parser = parser
        self._url = url

    async def execute(self) -> Any:
        result = await self._crawler.fetch(self._url)

        return self._parser.parse(result)
