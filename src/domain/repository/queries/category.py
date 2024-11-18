"""Category Query Repository module"""
from sqlmodel import select

from src.domain.models.category import Category
from src.config.database.sqlmodel import SessionDep


class CategoryQuery:
    def __init__(self, db_session: SessionDep):
        self.db_session = db_session

    def list(self):
        """
        Execute query to the database to returning all the categories
        :return:
        """
        stmt = select(Category)
        return self.db_session.exec(stmt).all()

    def get_by_id(self, location_id: int):
        """
        Execute query to select and filter category by category id
        returning a category
        :param location_id:
        :return:
        """
        return self.db_session.get(Category, location_id)
