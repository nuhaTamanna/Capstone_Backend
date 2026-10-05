from pydantic import BaseModel, Field


class SavedRouteCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    origin: str = Field(min_length=2, max_length=120)
    destination: str = Field(min_length=2, max_length=120)


class SavedRoute(BaseModel):
    id: int
    name: str
    origin: str
    destination: str
