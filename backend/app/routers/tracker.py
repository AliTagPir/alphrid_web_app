from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.schemas import TrackerInput, TrackerResponse
from app.models import WebAppTrackerData, WebAppUser
from app.deps import get_current_user
from app.crud import create_tracker_entry

router = APIRouter()

@router.post("/", response_model=TrackerResponse)
def submit_activity(
    data: TrackerInput,
    db: Session = Depends(get_db),
    current_user: WebAppUser = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admin users can submit activity data")
    
    entry = create_tracker_entry(db, data)

    return TrackerResponse(
        message="Activity logged successfully",
        entry_id=entry.id,
        activity=entry.activity,
        hours=entry.hours,
        logged_at=entry.logged_at
    )