from sqlmodel import Field, Relationship
from src.domain.models.base import BaseModel


class Category(BaseModel, table=True):
    title: str = Field(nullable=False, index=True, unique=True)

    location_categories: list["LocationCategory"] = Relationship(back_populates="category")
