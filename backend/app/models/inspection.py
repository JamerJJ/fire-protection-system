from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class Inspection(Base):
    __tablename__ = "inspections"

    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id", ondelete="CASCADE"), nullable=False)

    inspection_date = Column(Date, nullable=False)
    inspection_type = Column(String, nullable=False)
    inspector_name = Column(String(255), nullable=True)
    overall_status = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())