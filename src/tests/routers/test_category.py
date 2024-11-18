from src.domain.models.category import Category
from src.tests.routers.base import TestBase
from src.constants.code_status import CodeStatus


class TestCategory(TestBase):
    BASE_URL = "/api/v1/categories"

    def test_list_categories_empty_data_success(self, client_instance):
        response = client_instance.get(self.BASE_URL)
        assert response.status_code == CodeStatus.OK

    def test_list_categories_success(self, session_instance, client_instance):
        session_instance.add(Category(title=self.fake.name()))
        session_instance.commit()
        response = client_instance.get(self.BASE_URL)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert len(data) > 0

    def test_get_by_id_categories_success(self, session_instance, client_instance):
        session_instance.add(Category(title=self.fake.name()))
        session_instance.commit()
        response = client_instance.get(f"{self.BASE_URL}/1")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert data

    def test_get_by_id_categories_not_found_fail(self, session_instance, client_instance):
        session_instance.add(Category(title=self.fake.name()))
        session_instance.commit()
        response = client_instance.get(f"{self.BASE_URL}/2")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert not data

    def test_create_category_success(self, client_instance):
        data_payload = {"title": "testing"}
        response = client_instance.post(f"{self.BASE_URL}/", json=data_payload)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.CREATED
        assert data.get("title") == data_payload.get("title")

    def test_create_repeating_category_fail(self, session_instance, client_instance):
        title = "testing"
        session_instance.add(Category(title=title))
        session_instance.commit()
        data_payload = {"title": title}
        response = client_instance.post(f"{self.BASE_URL}/", json=data_payload)
        assert response.status_code == CodeStatus.BAD_REQUEST

    def test_update_category_success(self, client_instance, session_instance):
        session_instance.add(Category(title=self.fake.name()))
        session_instance.commit()
        data_payload = {"title": "testing"}
        response = client_instance.put(f"{self.BASE_URL}/1", json=data_payload)
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert data.get("title") == data_payload.get("title")

    def test_delete_category_success(self, client_instance, session_instance):
        session_instance.add(Category(title=self.fake.name()))
        session_instance.commit()
        response = client_instance.delete(f"{self.BASE_URL}/1")
        data = response.json().get("data")
        assert response.status_code == CodeStatus.OK
        assert data.get("ok")
