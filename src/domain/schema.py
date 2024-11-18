from datetime import date, datetime
from pydantic import BaseModel, ConfigDict
from typing import Generic, TypeVar, Union, Optional

from src.domain.models.category import Category
from src.domain.models.location import Location

T = TypeVar("T")


class JsonResponseSchema(BaseModel, Generic[T]):
    data: Union[T, None]


class StatusResponse(BaseModel):
    ok: bool


class LocationCategoryOut(BaseModel):
    id: int
    category: Category
    location: Location
    reviewed_date: Optional[date] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
