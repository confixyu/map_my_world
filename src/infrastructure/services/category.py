"""Category Service module"""

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from src.constants.code_status import CodeStatus
from src.domain.repository.commands.category import CategoryCommand
from src.domain.repository.queries.category import CategoryQuery
from src.utils.api_response import api_response


class CategoryService:
    """
    The Category service contain feature methods.
    """
    def __init__(self):
        self.query = CategoryQuery
        self.command = CategoryCommand

    def list(self, db_session):
        """
        This method has the objective to list all the categories
        saved from the database.
        :param db_session:
        :return:
        """
        return api_response(self.query(db_session).list())

    def get_by_id(self, category_id: int, db_session):
        """
        This method has the objective to return a category saved
        from database filtered by the category id.
        :param category_id:
        :param db_session:
        :return:
        """
        return api_response(self.query(db_session).get_by_id(category_id))

    def create(self, category_data, db_session):
        """
        This method has the objective create a category, receiving
        the category data as an input and save it into the database.
        :param category_data:
        :param db_session:
        :return:
        """
        try:
            return api_response(self.command(db_session).create(category_data))
        except IntegrityError as e:
            raise HTTPException(
                status_code=CodeStatus.BAD_REQUEST,
                detail=f"A category with title {category_data.title} already exists.",
            )

    def update(self, category_id, category_data, db_session):
        """
        This method has the objective to update a category, receiving the category data
        and the category id as an input, using the category id to filter
        and bring the matched category and update it with the new input data
        into the database.
        :param category_id:
        :param category_data:
        :param db_session:
        :return:
        """
        try:
            return api_response(self.command(db_session).update(category_id, category_data))
        except IntegrityError as e:
            raise HTTPException(
                status_code=CodeStatus.BAD_REQUEST,
                detail=f"A category with title {category_data.title} already exists.",
            )

    def delete(self, category_id: int, db_session):
        """
        This method has the objective to delete a category, receiving
        the category id as an input, using the category id to filter
        and bring the matched category then delete it from the database.
        :param category_id:
        :param db_session:
        :return:
        """
        return api_response(self.command(db_session).delete(category_id))
