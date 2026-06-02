from abc import ABC, abstractmethod
from typing import Any


class BasePipeline(ABC):
    @abstractmethod
    async def execute(self) -> Any:
        """
        Execute a complete acquisition pipeline"
        """
        raise NotImplementedError
