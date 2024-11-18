from datetime import date
from sqlmodel import Field, Relationship, UniqueConstraint

from src.domain.models.base import BaseModel


class LocationCategory(BaseModel, table=True):
    category_id: int = Field(foreign_key="category.id", nullable=False)
    location_id: int = Field(foreign_key="location.id", nullable=False)
    reviewed_date: date = Field(nullable=True)

    category: "Category" = Relationship(back_populates="location_categories")
    location: "Location" = Relationship(back_populates="location_categories")

    __table_args__ = (
        UniqueConstraint("category_id", "location_id", name="unique_category_location"),
    )
