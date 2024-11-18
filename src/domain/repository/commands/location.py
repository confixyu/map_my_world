"""Location Command Repository module"""

from fastapi import HTTPException

from src.domain.models.location import Location
from src.config.database.sqlmodel import SessionDep
from src.domain.repository.queries.location import LocationQuery
from src.constants.code_status import CodeStatus


class LocationCommand:
    def __init__(self, db_session: SessionDep):
        self.db_session = db_session
        self.query = LocationQuery(self.db_session)

    def create(self, location: Location):
        """
        Insert location data into location table into the database.
        :param location:
        :return:
        """
        self.db_session.add(location)
        self.db_session.commit()
        self.db_session.refresh(location)
        return location

    def update(self, location_id: int, location_update_data: Location):
        """
        Update a location record from a location table from the database.
        :param location_id:
        :param location_update_data:
        :return:
        """
        location = self.query.get_by_id(location_id)
        if not location:
            raise HTTPException(status_code=CodeStatus.NOT_FOUND, detail="Location not found")

        location_data = location_update_data.model_dump(exclude_unset=True)
        for key, value in location_data.items():
            setattr(location, key, value)
        self.db_session.add(location)
        self.db_session.commit()
        self.db_session.refresh(location)
        return location

    def delete(self, location_id: int):
        """
        Delete the location record by location id from
        the location table from database
        :param location_id:
        :return:
        """
        location = self.query.get_by_id(location_id)
        if not location:
            raise HTTPException(status_code=CodeStatus.NOT_FOUND,
                                detail="Location not found")
        self.db_session.delete(location)
        self.db_session.commit()
        return {"ok": True}
