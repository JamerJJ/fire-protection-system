from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.component import(
    create_component,
    delete_component,
    get_component_id,
    get_components
)
from app.db.session import get_db
from app.schemas.component import ComponentCreate, ComponentResponse    

router = APIRouter