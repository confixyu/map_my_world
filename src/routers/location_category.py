from fastapi import APIRouter
from typing import List

from src.config.database.sqlmodel import SessionDep
from src.constants.code_status import CodeStatus
from src.domain.models.location_category import LocationCategory
from src.domain.schema import JsonResponseSchema, StatusResponse, LocationCategoryOut
from src.infrastructure.services.location_category import LocationCategoryService

location_category_router = APIRouter(tags=["locations_categories"])
location_category_service = LocationCategoryService()


@location_category_router.get("/locations_categories")
def list_locations_categories(session: SessionDep) -> JsonResponseSchema[List[LocationCategoryOut]]:
    """
    This Endpoint allow user to list all locations categories
    saved from the database.
    """
    return location_category_service.list(session)


@location_category_router.get("/locations_categories/explore/discover")
def list_locations_categories(session: SessionDep) -> JsonResponseSchema[List[LocationCategoryOut]]:
    """
    This Endpoint allow user to list all locations categories
    saved from the database.
    """
    return location_category_service.discover(session)


@location_category_router.get("/locations_categories/{location_category_id}")
def get_location_category_by_id(location_category_id: int, session: SessionDep) \
        -> JsonResponseSchema[LocationCategoryOut]:
    """
    This endpoint allow user to get a specific location category
    by the location category id saved from the database.
    """
    return location_category_service.get_by_id(location_category_id, session)


@location_category_router.post("/locations_categories",
                               status_code=CodeStatus.CREATED)
def create_location_category(location_category_data: LocationCategory, session: SessionDep) \
        -> JsonResponseSchema[LocationCategory]:
    """
    This endpoint allow user to create a location category.
    """
    return location_category_service.create(location_category_data, session)


@location_category_router.delete("/locations_categories/{location_category_id}")
def delete_location_category(location_category_id: int, session: SessionDep) \
        -> JsonResponseSchema[StatusResponse]:
    """
    This endpoint allow user to delete a location category
    finding by location category id that must exists.
    """
    return location_category_service.delete(location_category_id, session)
