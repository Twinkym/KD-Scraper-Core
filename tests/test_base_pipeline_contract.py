from kd_scraper_core.pipelines.base_pipeline import BasePipeline

class DummyPipeline(BasePipeline):
  async def execute(self) -> dict:
    return {
      "status": "success",
    }

def test_pipeline_contract() -> None:
  pipeline = DummyPipeline()

  assert pipeline is not None
