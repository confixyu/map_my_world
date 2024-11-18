"""Location Service module"""
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from src.constants.code_status import CodeStatus
from src.domain.repository.commands.location import LocationCommand
from src.domain.repository.queries.location import LocationQuery
from src.utils.api_response import api_response


class LocationService:
    """
    The location service contain feature methods.
    """
    def __init__(self):
        self.query = LocationQuery
        self.command = LocationCommand

    def list(self, db_session):
        """
        This method has the objective to list all the locations
        saved from the database.
        :param db_session:
        :return:
        """
        return api_response(self.query(db_session).list())

    def get_by_id(self, location_id: int, db_session):
        """
        This method has the objective to return a location saved
        from database filtered by the location id.
        :param location_id:
        :param db_session:
        :return:
        """
        return api_response(self.query(db_session).get_by_id(location_id))

    def create(self, location_data, db_session):
        """
        This method has the objective create a location, receiving
        the location data as an input and save it into the database.
        :param location_data:
        :param db_session:
        :return:
        """
        try:
            return api_response(self.command(db_session).create(location_data))
        except IntegrityError as e:
            raise HTTPException(
                status_code=CodeStatus.BAD_REQUEST,
                detail=f"A location with this longitude: {location_data.latitude} and latitude: {location_data.longitude} already exists.",
            )

    def update(self, location_id, location_data, db_session):
        """
        This method has the objective to update a location, receiving the location data
        and the location id as an input, using the location id to filter
        and bring the matched location and update it with the new input data
        into the database.
        :param location_id:
        :param location_data:
        :param db_session:
        :return:
        """
        try:
            return api_response(self.command(db_session).update(location_id, location_data))
        except IntegrityError as e:
            raise HTTPException(
                status_code=CodeStatus.BAD_REQUEST,
                detail=f"A location with this longitude: {location_data.latitude} and latitude: {location_data.longitude} already exists.",
            )

    def delete(self, location_id: int, db_session):
        """
        This method has the objective to delete a location, receiving
        the location id as an input, using the location id to filter
        and bring the matched location then delete it from the database.
        :param location_id:
        :param db_session:
        :return:
        """
        return api_response(self.command(db_session).delete(location_id))
