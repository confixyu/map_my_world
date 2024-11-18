from fastapi import APIRouter
from typing import List

from src.config.database.sqlmodel import SessionDep
from src.constants.code_status import CodeStatus
from src.domain.models.location import Location
from src.domain.schema import JsonResponseSchema, StatusResponse
from src.infrastructure.services.location import LocationService

location_router = APIRouter(tags=["locations"])
location_service = LocationService()


@location_router.get("/locations")
def list_location(session: SessionDep) -> JsonResponseSchema[List[Location]]:
    """
    This Endpoint allow user to list all locations saved from the database.
    Fields
    """
    return location_service.list(session)


@location_router.get("/locations/{location_id}")
def get_location_by_id(location_id: int, session: SessionDep) -> JsonResponseSchema[Location]:
    """
    This endpoint allow user to get a specific location by the location id saved from the database.
    """
    return location_service.get_by_id(location_id, session)


@location_router.post("/locations", status_code=CodeStatus.CREATED)
def create_location(location_data: Location, session: SessionDep) -> JsonResponseSchema[Location]:
    """
    This endpoint allow user to create a location.
    """
    return location_service.create(location_data, session)


@location_router.put("/locations/{location_id}")
def update_location(location_id: int, location_data: Location, session: SessionDep) -> JsonResponseSchema[Location]:
    """
    This endpoint allow user to update a location finding by location id that must exists.
    """
    return location_service.update(location_id, location_data, session)


@location_router.delete("/locations/{location_id}")
def delete_location(location_id: int, session: SessionDep) -> JsonResponseSchema[StatusResponse]:
    """
    This endpoint allow user to delete a location finding by location id that must exists.
    """
    return location_service.delete(location_id, session)
