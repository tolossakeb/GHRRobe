from fastapi import FastAPI

from domain.domain import GHRInput, GHRPredicationResponse
from service.GHRRobe_service import GHRService


GHR_app = FastAPI()


@GHR_app.post("/predict")
async def predict_GHR(request: GHRInput) -> GHRPredicationResponse:

    return GHRService().predict_GHR(request=request)
