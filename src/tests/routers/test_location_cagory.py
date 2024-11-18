from src.domain.models.location_category import LocationCategory
from src.domain.models.location import Location
from src.domain.models.category import Category
from src.tests.routers.base import TestBase
from src.constants.code_status import CodeStatus


class TestLocationCategory(TestBase):
    BASE_URL = "/api/v1/locations_categories"

    def test_list_locations_categories_empty_data_success(self, client_instance):
        response = client_instance.get(self.BASE_URL)
        assert response.status_code == CodeStatus.OK

    def test_list_locations_categories_success(self, session_instance, client_instance):
        category = Category(title=self.fake.name())
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(category)
        session_instance.add(location)
        session_instance.commit()
        session_instance.refresh(category)
        session_instance.refresh(location)
        location_category = LocationCategory(
            category_id=category.id,
            location_id=location.id
        )
        session_instance.add(location_category)
        session_instance.commit()
        response = client_instance.get(self.BASE_URL)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert len(data) > 0

    def test_get_by_id_location_category_success(self, session_instance, client_instance):
        category = Category(title=self.fake.name())
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(category)
        session_instance.add(location)
        session_instance.commit()
        session_instance.refresh(category)
        session_instance.refresh(location)
        location_category = LocationCategory(
            category_id=category.id,
            location_id=location.id
        )
        session_instance.add(location_category)
        session_instance.commit()
        response = client_instance.get(f"{self.BASE_URL}/{location_category.id}")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert data

    def test_get_by_id_locations_categories_not_found_fail(self, session_instance, client_instance):
        category = Category(title=self.fake.name())
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(category)
        session_instance.add(location)
        session_instance.commit()
        session_instance.refresh(category)
        session_instance.refresh(location)
        location_category = LocationCategory(
            category_id=category.id,
            location_id=location.id
        )
        session_instance.add(location_category)
        session_instance.commit()
        response = client_instance.get(f"{self.BASE_URL}/2")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.NOT_FOUND
        assert not data

    def test_create_location_category_success(self, session_instance, client_instance):
        category = Category(title=self.fake.name())
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(category)
        session_instance.add(location)
        session_instance.commit()
        session_instance.refresh(category)
        session_instance.refresh(location)
        data_payload = {
            "category_id": category.id,
            "location_id": location.id
        }
        response = client_instance.post(f"{self.BASE_URL}/", json=data_payload)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.CREATED
        assert data.get("title") == data_payload.get("title")

    def test_create_location_category_no_exists_location_fail(self, session_instance, client_instance):
        category = Category(title=self.fake.name())
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(category)
        session_instance.add(location)
        session_instance.commit()
        session_instance.refresh(category)
        session_instance.refresh(location)
        data_payload = {
            "category_id": category.id,
            "location_id": 10
        }
        response = client_instance.post(f"{self.BASE_URL}/", json=data_payload)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.BAD_REQUEST

    def test_create_location_category_no_exists_category_fail(self, session_instance, client_instance):
        category = Category(title=self.fake.name())
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(category)
        session_instance.add(location)
        session_instance.commit()
        session_instance.refresh(category)
        session_instance.refresh(location)
        data_payload = {
            "category_id": 10,
            "location_id": location.id
        }
        response = client_instance.post(f"{self.BASE_URL}/", json=data_payload)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.BAD_REQUEST

    def test_create_repeating_location_category_fail(self, session_instance, client_instance):
        category = Category(title=self.fake.name())
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(category)
        session_instance.add(location)
        session_instance.commit()
        session_instance.refresh(category)
        session_instance.refresh(location)
        location_category = LocationCategory(
            category_id=category.id,
            location_id=location.id
        )
        session_instance.add(location_category)
        session_instance.commit()
        data_payload = {
            "category_id": category.id,
            "location_id": location.id
        }
        response = client_instance.post(f"{self.BASE_URL}/", json=data_payload)
        assert response.status_code == CodeStatus.BAD_REQUEST

    def test_delete_location_category_success(self, client_instance, session_instance):
        category = Category(title=self.fake.name())
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(category)
        session_instance.add(location)
        session_instance.commit()
        session_instance.refresh(category)
        session_instance.refresh(location)
        location_category = LocationCategory(
            category_id=category.id,
            location_id=location.id
        )
        session_instance.add(location_category)
        session_instance.commit()
        response = client_instance.delete(f"{self.BASE_URL}/1")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert data.get("ok")
