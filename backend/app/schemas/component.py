from datetime import date, datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


class ComponentBase(BaseModel):
    system_id: int
    component_type: Literal['pipe', 'sprinkler_head', 'valve', 'pump']
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    material: Optional[Literal['steel', 'cpvc', 'cast_iron']] = None
    install_date: Optional[date] = None
    location_description: Optional[str] = None
    criticality_level: Optional[int] = Field(default=None, ge=1, le=5)


class ComponentCreate(ComponentBase):
    pass

class ComponentResponse(ComponentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True