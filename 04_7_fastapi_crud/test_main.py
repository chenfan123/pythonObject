from fastapi.testclient import TestClient

from main import app, users


client = TestClient(app)


def setup_function() -> None:
    users.clear()


def test_user_crud() -> None:
    create_response = client.post(
        "/users",
        json={
            "name": "Alice",
            "email": "alice@example.com",
            "password": "password123",
        },
    )
    assert create_response.status_code == 201
    created_user = create_response.json()
    assert created_user == {
        "id": created_user["id"],
        "name": "Alice",
        "email": "alice@example.com",
    }
    assert "password" not in created_user

    user_id = created_user["id"]

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json() == created_user

    update_response = client.patch(
        f"/users/{user_id}",
        json={"name": "Alice Updated"},
    )
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Alice Updated"

    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 204
    assert delete_response.content == b""

    missing_response = client.get(f"/users/{user_id}")
    assert missing_response.status_code == 404
    assert missing_response.json()["detail"]["code"] == "USER_NOT_FOUND"


def test_duplicate_email_returns_conflict() -> None:
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "password": "password123",
    }

    assert client.post("/users", json=payload).status_code == 201

    duplicate_response = client.post("/users", json=payload)
    assert duplicate_response.status_code == 409
    assert duplicate_response.json()["detail"]["code"] == "EMAIL_ALREADY_EXISTS"


def test_invalid_request_returns_422() -> None:
    response = client.post(
        "/users",
        json={
            "name": "A",
            "email": "alice@example.com",
            "password": "short",
        },
    )
    assert response.status_code == 422
