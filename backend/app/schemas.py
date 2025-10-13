from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

# Chart
class ChartResponse(BaseModel):
    chart_data: dict

# Log in
class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserOut(BaseModel):
    username: str
    role: str

# Tracker
class TrackerInput(BaseModel):
    activity:str
    hours: float
    logged_at: datetime

class TrackerResponse(BaseModel):
    message: str
    entry_id: UUID
    activity: str
    hours: float
    logged_at: datetime