"""Location Category Query Repository module"""
from sqlmodel import select
from sqlalchemy.orm import joinedload
from datetime import datetime, timedelta
from sqlalchemy import or_

from src.domain.models.location_category import LocationCategory
from src.config.database.sqlmodel import SessionDep


class LocationCategoryQuery:
    def __init__(self, db_session: SessionDep):
        self.db_session = db_session

    def list(self):
        """
        Execute query to the database to returning all
        the locations categories
        :return:
        """
        stmt = select(LocationCategory).options(joinedload(LocationCategory.category),
                                                joinedload(LocationCategory.location))
        return self.db_session.exec(stmt).all()

    def discover(self):
        """
        Execute query to the database to returning all
        the locations categories
        :return:
        """
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        stmt = (select(LocationCategory)
                .options(joinedload(LocationCategory.category),
                         joinedload(LocationCategory.location))
                .where(
                    or_(
                        LocationCategory.reviewed_date == None,
                        LocationCategory.reviewed_date < thirty_days_ago
                    )
                )
                )
        return self.db_session.exec(stmt).all()

    def get_by_id(self, location_category_id: int):
        """
        Execute query to select and filter location category
        by location_category_id returning a location_category
        :param location_category_id:
        :return:
        """
        return self.db_session.get(LocationCategory,
                                   location_category_id)
