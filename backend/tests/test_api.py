import pytest
from httpx import AsyncClient
from app.main import app
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.test")

test_admin_username = os.getenv("TEST_ADMIN_USERNAME")
test_admin_password = os.getenv("TEST_ADMIN_PASSWORD")
test_guest_username = os.getenv("TEST_GUEST_USERNAME")
test_guest_password = os.getenv("TEST_GUEST_PASSWORD")

@pytest.mark.asyncio
async def test_login_valid_user():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.post("/auth/login", json={
            "username": test_admin_username,
            "password": test_admin_password
        })
        print("Status code:", response.status_code)
        print("Response body:", response.text)

        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_invalid_user():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.post("/auth/login", json={
            "username": "invalid",
            "password": "wrong"
        })
        print("Status code:", response.status_code)
        print("Response body:", response.text)

        assert response.status_code == 401

@pytest.mark.asyncio
async def test_admin_can_post_tracker_data():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        # Login as admin first
        login = await client.post("/auth/login", json={
            "username": test_admin_username,
            "password": test_admin_password
        })
        token = login.json()["access_token"]

        # Submit activity
        response = await client.post("/track/", json={
            "activity": "working",
            "hours": 2.5,
            "logged_at": "2025-05-13T00:00:00"
        }, headers={"Authorization": f"Bearer {token}"})
        
        data = response.json()
        print("Response JSON:", data)
        assert response.status_code == 200
        assert "message" in data, "Missing 'message' in response"
        assert data["message"] == "Activity logged successfully"

@pytest.mark.asyncio
async def test_guest_cannot_post_tracker_data():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        # Login as admin first
        login = await client.post("/auth/login", json={
            "username": test_guest_username,
            "password": test_guest_password
        })
        token = login.json()["access_token"]

        # Submit activity
        response = await client.post("/track/", json={
            "activity": "leisure",
            "hours": 1,
            "logged_at": "2025-06-13T00:00:00"
        }, headers={"Authorization": f"Bearer {token}"})

        assert response.status_code == 403

@pytest.mark.asyncio
async def test_chart_access_without_auth():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/charts/daily")
        # 200 if chart exists, 404 if chart does not exist
        assert response.status_code in [200, 404]

