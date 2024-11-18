"""Category Command Repository module"""

from fastapi import HTTPException

from src.domain.models.category import Category
from src.config.database.sqlmodel import SessionDep
from src.domain.repository.queries.category import CategoryQuery
from src.constants.code_status import CodeStatus


class CategoryCommand:
    def __init__(self, db_session: SessionDep):
        self.db_session = db_session
        self.query = CategoryQuery(self.db_session)

    def create(self, category: Category):
        """
        Insert category data into category table into the database
        :param category:
        :return:
        """
        self.db_session.add(category)
        self.db_session.commit()
        self.db_session.refresh(category)
        return category

    def update(self, category_id: int, category_update_data: Category):
        """
        Update a category record from a category table from the database
        :param category_id:
        :param category_update_data:
        :return:
        """
        category = self.query.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=CodeStatus.NOT_FOUND, detail="Category not found")

        category_data = category_update_data.model_dump(exclude_unset=True)
        for key, value in category_data.items():
            setattr(category, key, value)
        self.db_session.add(category)
        self.db_session.commit()
        self.db_session.refresh(category)
        return category

    def delete(self, category_id: int):
        """
        Delete the location record by location id from
        the location table from database
        :param category_id:
        :return:
        """
        category = self.query.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=CodeStatus.NOT_FOUND,
                                detail="Category not found")
        self.db_session.delete(category)
        self.db_session.commit()
        return {"ok": True}
