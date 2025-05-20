from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, DateTime
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