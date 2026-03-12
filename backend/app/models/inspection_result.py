from sqlalchemy import Column, Integer, Boolean, Text, TIMESTAMP, ForeignKey, Numeric
from sqlalchemy.sql import func
from app.db.base import Base

class InspectionResult(Base):
    __tablename__ = "inspection_results"

    id = Column(Integer, primary_key=True, index=True)
    inspection_id = Column(Integer, ForeignKey("inspections.id", ondelete="CASCADE"), nullable=False)
    component_id = Column(Integer, ForeignKey("components.id", ondelete="CASCADE"), nullable=False)

    condition_score = Column(Integer, nullable=True)
    pressure_reading = Column(Numeric(8, 2), nullable=True)
    flow_rate = Column(Numeric(8, 2), nullable=True)
    corrosion_index = Column(Integer, nullable=True)
    pass_fail = Column(Boolean, nullable=True)
    notes = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())