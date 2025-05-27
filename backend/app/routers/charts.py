from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import ChartCache, WebAppUser
from app.schemas import ChartResponse
from app.crud import get_latest_chart_by_timeframe
from app.deps import get_current_user

router = APIRouter()

@router.get("/{timeframe}", response_model=ChartResponse)
def get_latest_chart(
    timeframe: str, 
    db: Session = Depends(get_db), 
    current_user: WebAppUser = Depends(get_current_user)
):

    valid_timeframes = ["daily", "weekly", "monthly", "yearly"]
    if timeframe not in valid_timeframes:
        raise HTTPException(status_code=400, detail="Invalid_timeframe")
    
    result = get_latest_chart_by_timeframe(db, timeframe)

    if not result:
        raise HTTPException(status_code=404, detail="No chart found for that timeframe")
    
    return {"chart_html": result.chart_html}