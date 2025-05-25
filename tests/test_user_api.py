from http.client import responses
import pytest
import json
import uuid
from conftest import load_user_data
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_users(api_client, load_user_data):
    user_data = load_user_data["new_user"]
    
    # # Set known values for consistency
    # user_data["name"] = "Harshit QA"
    # user_data["username"] = "qa_user"
    # user_data["email"] = f"{uuid.uuid4().hex[:8]}@example.com"
    
    print(f"Generated email: {user_data['email']}")
    
    # POST to create user
    response = api_client.post("users", user_data)
    print("POST response:", response.json())
    assert response.status_code == 201
    assert response.json()['name'] == user_data['name']
    
    # Extract ID and fetch user
    id = response.json()['id']    
    responseget = api_client.get(f"users/10")
    print("GET response:", responseget.json())

    assert responseget.status_code == 200
    assert responseget.json()['name'] == 'Clementina DuBuque'


def test_update_users(api_client):
    user_data ={
        'name': 'Suraj QA',
        'username': 'QA team',
        'email': 'surajqa@example.com'
    }
    response = api_client.put("users/1", user_data)
    print(response.json())
    assert response.status_code == 200
    # assert response.json()['name'] == user_data['name']

def test_delete_users(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200
    # assert response.json()['name'] == user_data['name']
