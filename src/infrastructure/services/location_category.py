"""Location Category Service module"""
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from src.constants.code_status import CodeStatus
from src.domain.repository.commands.location_category import LocationCategoryCommand
from src.domain.repository.queries.category import CategoryQuery
from src.domain.repository.queries.location import LocationQuery
from src.domain.repository.queries.location_category import LocationCategoryQuery
from src.utils.api_response import api_response


class LocationCategoryService:
    """
    The location category service
    contain feature methods.
    """
    def __init__(self):
        self.query = LocationCategoryQuery
        self.location_query = LocationQuery
        self.category_query = CategoryQuery
        self.command = LocationCategoryCommand

    def list(self, db_session):
        """
        This method has the objective to list
        all the locations categories saved from the database.
        :param db_session:
        :return:
        """
        return api_response(self.query(db_session).list())

    def discover(self, db_session):
        """
        This method has the objective to list
        all the locations categories saved from the database.
        :param db_session:
        :return:
        """
        return api_response(self.query(db_session).discover())

    def get_by_id(self, location_category_id: int, db_session):
        """
        This method has the objective to return a
        location_category saved from database
        filtered by the location category.
        :param location_category_id:
        :param db_session:
        :return:
        """
        location_category = self.query(db_session).get_by_id(location_category_id)
        if not location_category:
            raise HTTPException(
                status_code=CodeStatus.NOT_FOUND,
                detail=f"A location category with id {location_category_id} does not exists.",
            )
        location_category = self.command(db_session).update_date_reviewed(location_category)
        return api_response(location_category)

    def create(self, location_category_data, db_session):
        """
        This method has the objective create a location, receiving
        the location category data as an input and save it into the database.
        :param location_category_data:
        :param db_session:
        :return:
        """
        try:
            location = self.location_query(db_session).get_by_id(location_category_data.location_id)
            if not location:
                raise HTTPException(
                    status_code=CodeStatus.BAD_REQUEST,
                    detail=f"A location with id {location_category_data.location_id} does not exists.",
                )
            category = self.category_query(db_session).get_by_id(location_category_data.category_id)
            if not category:
                raise HTTPException(
                    status_code=CodeStatus.BAD_REQUEST,
                    detail=f"A category with id {location_category_data.category_id} does not exists.",
                )
            return api_response(self.command(db_session).create(location_category_data))
        except IntegrityError:
            raise HTTPException(
                status_code=CodeStatus.BAD_REQUEST,
                detail=f"A location category with this location id {location_category_data.location_id} and category id {location_category_data.category_id} already exists.",
            )

    def delete(self, location_category_id: int, db_session):
        """
        This method has the objective to delete a location category
        , receiving the location category id as an input, using
        the location category id to filter and bring the matched
        location category  then delete it from the database.
        :param location_category_id:
        :param db_session:
        :return:
        """
        return api_response(self.command(db_session).delete(location_category_id))
