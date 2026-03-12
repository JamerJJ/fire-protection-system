from sqlalchemy import Column, Integer, String, Date, Numeric, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class FireSystem(Base):
    __tablename__ = "fire_systems"

    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id", ondelete="CASCADE"), nullable=False)

    system_type = Column(String, nullable=False)
    install_date = Column(Date, nullable=False)
    last_major_maintenance_date = Column(Date, nullable=True)
    design_pressure = Column(Numeric(6, 2), nullable=True)
    status = Column(String(50), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())