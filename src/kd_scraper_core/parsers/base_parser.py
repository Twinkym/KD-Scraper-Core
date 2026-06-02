from abc import ABC, abstractmethod
from kd_scraper_core.core.models import FetchResult
from typing import Any

class BaseParser(ABC):
  @abstractmethod
  def parse(self, fetch_result: FetchResult) -> Any:
    """
    Transform raw content into structured data.
    """
    raise NotImplementedError
