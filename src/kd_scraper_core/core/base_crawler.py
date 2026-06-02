from abc import ABC, abstractmethod
from kd_scraper_core.core.models import FetchResult

class BaseCrawler(ABC):
  @abstractmethod
  async def fetch(self, url: str) -> FetchResult:
    """
    Retrieve raw content from a target source.
    """
    raise NotImplementedError
