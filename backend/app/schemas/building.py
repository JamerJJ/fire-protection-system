from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class BuildingBase(BaseModel):
    name: str
    address: str
    city: str
    county: Optional[str] = None
    zip_code: Optional[str] = None
    occupancy_type: Literal["residential", "commercial", "industrial"]
    construction_year: Optional[int] = None
    square_footage: Optional[int] = None


class BuildingCreate(BuildingBase):
    pass 

class BuildingResponse(BuildingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

        
