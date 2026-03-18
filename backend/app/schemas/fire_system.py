from pydantic import BaseModel
from typing import Optional, Literal
from datetime import date, datetime
from decimal import Decimal

class FireSystemBase(BaseModel):
    building_id: int
    system_type: Literal['wet', 'dry', 'pre_action', 'deluge']
    install_date: date
    last_major_maintenance_date: Optional[date] = None
    design_pressure: Optional[Decimal] = None
    status: Optional[Literal['active', 'decommisioned']] = 'active'


class FireSystemCreate(FireSystemBase):
    pass 


class FireSystemResponse(FireSystemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 