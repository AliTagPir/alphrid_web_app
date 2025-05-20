from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import ChartCache
from app.schemas import ChartResponse

router = APIRouter()

@router.get("/{timeframe}", response_model=ChartResponse)
def get_latest_chart(timeframe: str, db: Session = Depends(get_db)):

    valid_timeframes = ["daily", "weekly", "monthly", "yearly"]
    if timeframe not in valid_timeframes:
        raise HTTPException(status_code=400, detail="Invalid_timeframe")
    
    stmt = (
        select(ChartCache)
        .where(ChartCache.chart_key.like(f"{timeframe}_%"))
        .order_by(ChartCache.created_at.desc())
        .limit(1)
    )

    result = db.execute(stmt).scalars().first()

    if not result:
        raise HTTPException(status_code=400, detail="No chart found for that timeframe")
    
    return {"chart_html": result.chart_html}