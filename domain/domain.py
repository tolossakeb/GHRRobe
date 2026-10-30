from pydantic import BaseModel

class GHRInput(BaseModel):
    P: float
    RH: float
    SH: float
    MaxTem: float
    MinTem: float
    TemR: float
    WS: float


class GHRPredicationResponse(BaseModel):
    H: float