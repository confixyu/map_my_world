"""Location Category Command Repository module"""

from fastapi import HTTPException
from datetime import datetime

from src.domain.models.location_category import LocationCategory
from src.domain.repository.queries.location_category import LocationCategoryQuery
from src.config.database.sqlmodel import SessionDep
from src.constants.code_status import CodeStatus


class LocationCategoryCommand:
    def __init__(self, db_session: SessionDep):
        self.db_session = db_session
        self.query = LocationCategoryQuery(self.db_session)

    def create(self, location_category: LocationCategory):
        """
        Insert location category  data into
        location_category table into the database.
        :param location_category:
        :return:
        """
        self.db_session.add(location_category)
        self.db_session.commit()
        self.db_session.refresh(location_category)
        return location_category

    def delete(self, location_category_id: int):
        """
        Delete the location category record
        by location category  id from
        the location category table from database.
        :param location_category_id:
        :return:
        """
        location = self.query.get_by_id(location_category_id)
        if not location:
            raise HTTPException(status_code=CodeStatus.NOT_FOUND,
                                detail="Location not found")
        self.db_session.delete(location)
        self.db_session.commit()
        return {"ok": True}

    def update_date_reviewed(self, location_category: LocationCategory):
        """
        Update the location category record reviewed_date field by now date.
        :param location_category:
        :return:
        """
        location_category.reviewed_date = datetime.utcnow().date()
        self.db_session.add(location_category)
        self.db_session.commit()
        self.db_session.refresh(location_category)
        return location_category
