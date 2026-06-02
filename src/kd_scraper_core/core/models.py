from dataclasses import dataclass


@dataclass(slots=True)
class FetchResult:
    url: str
    content: str
    status_code: int
