from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_successful_match():
    data = {
        "email": "example@example.com",
        "phone": "+7 123 456 78 90",
        "date": "2022-01-01",
        "text": "some text"
    }

    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"form_template_name": "MyForm"}


def test_successful_match_for_other_form():
    data = {
        "email": "test@example.com",
        "phone": "+7 123 456 78 90",
        "date": "2023-01-01",
        "text": "text"
    }

    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"form_template_name": "OtherForm"}


def test_field_type_matching_for_wrong_case():
    """Тестирование сопоставления типов полей."""
    data = {
        "email": "example@example.com",
        "phone": "+7 123 456 78 22",
        "date": "2022-01-02",
        "text": "some text"
    }

    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"date": "date", "phone": "phone",
                               "email": "email", "text": "text"}
