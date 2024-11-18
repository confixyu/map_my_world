"""Location Query Repository module"""
from sqlmodel import select

from src.domain.models.location import Location
from src.config.database.sqlmodel import SessionDep


class LocationQuery:
    def __init__(self, db_session: SessionDep):
        self.db_session = db_session

    def list(self):
        """
        Execute query to the database to returning all the locations
        :return:
        """
        stmt = select(Location)
        return self.db_session.exec(stmt).all()

    def get_by_id(self, location_id: int):
        """
        Execute query to select and filter location by location id
        returning a location
        :param location_id:
        :return:
        """
        return self.db_session.get(Location, location_id)
