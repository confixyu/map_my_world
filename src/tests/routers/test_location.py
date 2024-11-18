from src.domain.models.location import Location
from src.tests.routers.base import TestBase
from src.constants.code_status import CodeStatus


class TestLocation(TestBase):
    BASE_URL = "/api/v1/locations"

    def test_list_locations_empty_data_success(self, client_instance):
        response = client_instance.get(self.BASE_URL)
        assert response.status_code == CodeStatus.OK

    def test_list_locations_success(self, session_instance, client_instance):
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(location)
        session_instance.commit()
        response = client_instance.get(self.BASE_URL)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert len(data) > 0

    def test_get_by_id_locations_success(self, session_instance, client_instance):
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(location)
        session_instance.commit()
        response = client_instance.get(f"{self.BASE_URL}/1")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert data

    def test_get_by_id_locations_not_found_fail(self, session_instance, client_instance):
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(location)
        session_instance.commit()
        response = client_instance.get(f"{self.BASE_URL}/2")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert not data

    def test_create_location_success(self, client_instance):
        data_payload = {
            "latitude": str(self.fake.latitude()),
            "longitude": str(self.fake.longitude())
        }
        response = client_instance.post(f"{self.BASE_URL}/", json=data_payload)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.CREATED
        assert data.get("title") == data_payload.get("title")

    def test_create_repeating_location_fail(self, session_instance, client_instance):
        latitude = str(self.fake.latitude())
        longitude = str(self.fake.longitude())
        location = Location(
            latitude=latitude,
            longitude=longitude
        )
        session_instance.add(location)
        session_instance.commit()
        data_payload = {
            "latitude": latitude,
            "longitude": longitude
        }
        response = client_instance.post(f"{self.BASE_URL}/", json=data_payload)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.BAD_REQUEST

    def test_update_location_success(self, client_instance, session_instance):
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(location)
        session_instance.commit()
        data_payload = {
            "latitude": str(self.fake.latitude()),
            "longitude": str(self.fake.longitude())
        }
        response = client_instance.put(f"{self.BASE_URL}/1", json=data_payload)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert data.get("title") == data_payload.get("title")

    def test_delete_location_success(self, client_instance, session_instance):
        location = Location(
            latitude=str(self.fake.latitude()),
            longitude=str(self.fake.longitude())
        )
        session_instance.add(location)
        session_instance.commit()
        response = client_instance.delete(f"{self.BASE_URL}/1")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert data.get("ok")
