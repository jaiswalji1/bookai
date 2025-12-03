from pydantic import BaseModel

class BaseRecommendation(BaseModel):
    gener: str

class Recommendation(BaseRecommendation):
    gener: str