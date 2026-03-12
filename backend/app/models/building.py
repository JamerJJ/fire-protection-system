from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    county = Column(String(100), nullable=True)
    zip_code = Column(String(20), nullable=True)

    # Stored as PostgreSQL ENUM; SQLAlchemy can treat as String unless we map Enum explicitly
    occupancy_type = Column(String, nullable=False)

    construction_year = Column(Integer, nullable=True)
    square_footage = Column(Integer, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())