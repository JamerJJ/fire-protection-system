from sqlalchemy import Column, Integer, String, Boolean, Date, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class Deficiency(Base):
    __tablename__ = "deficiencies"

    id = Column(Integer, primary_key=True, index=True)
    inspection_result_id = Column(Integer, ForeignKey("inspection_results.id", ondelete="CASCADE"), nullable=False)

    deficiency_code = Column(String(100), nullable=True)
    severity_level = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_recurring = Column(Boolean, nullable=True)
    resolved_date = Column(Date, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())