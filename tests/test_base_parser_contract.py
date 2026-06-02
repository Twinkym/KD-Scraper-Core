from kd_scraper_core.core.models import FetchResult
from kd_scraper_core.parsers.base_parser import BaseParser

class DummyParser(BaseParser):
  def parse(self, result: FetchResult) -> dict:
    return {"url": result.url}

def test_parser_contract() -> None:
  parser = DummyParser()

  result = FetchResult(
    url = "https://example.com",
    content = "<html></html>",
    status_code = 200,
  )

  parsed = parser.parse(result)

  assert parsed["url"] == "https://example.com"
