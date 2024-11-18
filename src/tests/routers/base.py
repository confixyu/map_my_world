import pytest
import random
from faker import Faker
from sqlmodel.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine
from fastapi.testclient import TestClient


# Apps
from main import app
from src.config.database.sqlmodel import get_session


class TestBase:
    BASE_URL: str = "/"
    fake: Faker = Faker()

    @pytest.fixture(name="client")
    def client_fixture(self, session: Session):
        def get_session_override():
            return session

        app.dependency_overrides[get_session] = get_session_override

        client = TestClient(app)
        yield client
        app.dependency_overrides.clear()

    @pytest.fixture(name="session")
    def session_fixture(self):
        engine = create_engine(
            "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
        )
        SQLModel.metadata.create_all(engine)
        with Session(engine) as session:
            yield session

    @pytest.fixture
    def session_instance(self, session: Session):
        return session

    @pytest.fixture
    def client_instance(self, client: TestClient):
        return client

    def get_url(self, path: str, params=None):
        url_path: str = f"{self.BASE_URL}{path}"
        if params is None:
            params = {}
        return url_path.format(**params)
