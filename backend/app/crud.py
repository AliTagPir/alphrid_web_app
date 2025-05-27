
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import WebAppUser, WebAppTrackerData, ChartCache
from app.schemas import TrackerInput
from datetime import datetime

# --- Users ---

def get_user_by_username(db: Session, username: str) -> WebAppUser | None:
    return db.query(WebAppUser).filter_by(username=username).first()


# --- Tracker Submissions ---

def create_tracker_entry(db: Session, data: TrackerInput) -> WebAppTrackerData:
    entry = WebAppTrackerData(
        activity=data.activity,
        hours=data.hours,
        logged_at=data.logged_at,
        submitted_at=datetime.now()
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


# --- Charts  ---

def get_latest_chart_by_timeframe(db: Session, timeframe: str) -> ChartCache | None:
    stmt = (
        select(ChartCache)
        .where(ChartCache.chart_key.like(f"{timeframe}_%"))
        .order_by(ChartCache.created_at.desc())
        .limit(1)
    )
    return db.execute(stmt).scalars().first()