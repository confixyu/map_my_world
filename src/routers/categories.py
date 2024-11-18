from fastapi import APIRouter
from typing import List

from src.config.database.sqlmodel import SessionDep
from src.constants.code_status import CodeStatus
from src.domain.models.category import Category
from src.domain.schema import JsonResponseSchema, StatusResponse
from src.infrastructure.services.category import CategoryService


category_router = APIRouter(tags=["categories"])
category_service = CategoryService()


@category_router.get("/categories")
def list_category(session: SessionDep) -> JsonResponseSchema[List[Category]]:
    """
    This Endpoint allow user to list all locations saved from the database.
    Fields
    """
    return category_service.list(session)


@category_router.get("/categories/{category_id}")
def get_category_by_id(category_id: int, session: SessionDep) -> JsonResponseSchema[Category]:
    """
    This endpoint allow user to get a specific category by the category id saved from the database.
    """
    return category_service.get_by_id(category_id, session)


@category_router.post("/categories", status_code=CodeStatus.CREATED)
def create_category(category: Category, session: SessionDep) -> JsonResponseSchema[Category]:
    """
    This endpoint allow user to create a category.
    """
    return category_service.create(category, session)


@category_router.put("/categories/{category_id}")
def update_category(category_id: int, category: Category, session: SessionDep) -> JsonResponseSchema[Category]:
    """
    This endpoint allow user to update a category finding by category id that must exists.
    """
    return category_service.update(category_id, category, session)


@category_router.delete("/categories/{category_id}")
def delete_category(category_id: int, session: SessionDep) -> JsonResponseSchema[StatusResponse]:
    """
    This endpoint allow user to delete a category finding by category id that must exists.
    """
    return category_service.delete(category_id, session)
