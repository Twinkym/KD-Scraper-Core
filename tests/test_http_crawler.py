from kd_scraper_core.crawlers.http_crawler import HttpCrawler

def test_http_crawler_creation() -> None:
    crawler = HttpCrawler()
    
    assert crawler is not None