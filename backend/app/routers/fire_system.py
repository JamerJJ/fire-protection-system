from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.fire_system import FireSystemCreate, FireSystemResponse
from app.crud.fire_system import (
    create_fire_system,
    get_fire_system,
    get_fire_system_by_id,
    delete_fire_system,
)

router = APIRouter(prefix="/fire-systems", tags=["Fire Systems"])

@router.post("/", response_model=FireSystemResponse, status_code=201)
def create_new_fire_system(fire_system: FireSystemCreate, db: Session = Depends(get_db)):
    created_fire_system = create_fire_system(db, fire_system)
    if not created_fire_system:
        raise HTTPException(status_code=404, detail="Building not found")
    return created_fire_system

@router.get("/", response_model= list[FireSystemResponse])
def read_fire_system(db: Session = Depends(get_db)):
    return get_fire_system(db)

@router.delete("/{fire_system_id}", response_model= FireSystemResponse)
def remove_fire_system(fire_system_id: int, db: Session =Depends(get_db)):
    fire_system = delete_fire_system(db, fire_system_id)
    if not fire_system:
        raise HTTPException(status_code=404, detail="Fire system not found")
    return fire_system

