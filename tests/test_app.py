"""Модульные тесты HTTP-интерфейса."""

from app import create_app
import pytest


@pytest.fixture()
def client():
    """Создаёт изолированный тестовый клиент Flask."""
    test_application = create_app()
    test_application.config.update(TESTING=True)
    with test_application.test_client() as test_client:
        yield test_client


def test_health(client):
    """Проверяет код и тело ответа health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_index(client):
    """Проверяет основные сведения о службе."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {
        "service": "devops-ci-app",
        "version": "1.0.0",
        "status": "running",
    }
