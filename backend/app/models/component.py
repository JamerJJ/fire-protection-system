from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class Component(Base):
    __tablename__ = "components"

    id = Column(Integer, primary_key=True, index=True)
    system_id = Column(Integer, ForeignKey("fire_systems.id", ondelete="CASCADE"), nullable=False)

    component_type = Column(String, nullable=False)
    manufacturer = Column(String(255), nullable=True)
    model = Column(String(255), nullable=True)
    material = Column(String, nullable=True)
    install_date = Column(Date, nullable=True)
    location_description = Column(Text, nullable=True)
    criticality_level = Column(Integer, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())