from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select


class BaseModel(SQLModel):
    id: int = Field(primary_key=True, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
