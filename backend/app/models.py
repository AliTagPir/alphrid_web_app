from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Float, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class Base(DeclarativeBase):
    pass

class ChartCache(Base):
    __tablename__ = "chart_cache"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chart_key: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    chart_type: Mapped[str] = mapped_column(String, nullable=False)
    chart_html: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    last_updated: Mapped[datetime] = mapped_column(DateTime, nullable=False)

class WebAppUser(Base):
    __tablename__ = "web_app_users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False) 
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())

class WebAppTrackerData(Base):
    __tablename__ = "web_app_tracker_data_log"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key="True", default=uuid.uuid4)
    activity: Mapped[str] = mapped_column(String, nullable=False)
    hours: Mapped[float] = mapped_column(Float, nullable=False)
    logged_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    submitted_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)