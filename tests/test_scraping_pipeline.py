from kd_scraper_core.core.models import FetchResult
from kd_scraper_core.core.base_crawler import BaseCrawler
from kd_scraper_core.parsers.base_parser import BaseParser
from kd_scraper_core.pipelines.scraping_pipeline import (
    ScrapingPipeline,
)
import pytest


class DummyCrawler(BaseCrawler):
    async def fetch(self, url: str) -> FetchResult:
        return FetchResult(
            url=url,
            content="<html><body><h1>Dummy Content</h1></body></html>",
            status_code=200,
        )


class DummyParser(BaseParser):
    def parse(self, result: FetchResult) -> dict:
        return {
            "title": "Dummy Content",
            "url": result.url,
            "status": result.status_code,
        }


@pytest.mark.anyio
async def test_scraping_pipeline_execute() -> None:
    pipeline = ScrapingPipeline(
        crawler=DummyCrawler(), parser=DummyParser(), url="https://example.com"
    )

    result = await pipeline.execute()

    assert result["url"] == "https://example.com"
    assert result["status"] == 200

