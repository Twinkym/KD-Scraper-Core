from abc import ABC, abstractmethod
from typing import Any

class BaseParser(ABC):
  @abstractmethod
  def parse(self, raw_content: str) -> Any:
    """
    Transform raw content into structured data.
    """
    raise NotImplementedError
