from abc import ABC, abstractmethod

class BaseCrawler(ABC):
  @abstractmethod
  async def fetch(self, url: str) -> str:
    """
    Retrieve raw content from a target source.
    """
    raise NotImplementedError
