from kd_scraper_core.core.models import FetchResult


def test_fetch_result_creation() -> None:
  result = FetchResult(
    url="https://example.com",
    content="<html></html>",
    status_code=200,
  )

  assert result.url == "https://example.com"
  assert result.status_code == 200
