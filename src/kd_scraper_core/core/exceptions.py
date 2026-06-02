class ScraperCoreError(Exception):
  """Base exception for scraper core errors."""

class FetchError(ScraperCoreError):
  """Exception raised when fetching a resource cannot be retrieved."""
