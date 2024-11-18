from sqlmodel import Field, UniqueConstraint, Relationship

from src.domain.models.base import BaseModel


class Location(BaseModel, table=True):
    longitude: str = Field(nullable=False)
    latitude: str = Field(nullable=False)

    location_categories: list["LocationCategory"] = Relationship(back_populates="location")

    __table_args__ = (
        UniqueConstraint("longitude", "latitude", name="unique_longitude_latitude"),
    )
