from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.building import BuildingCreate, BuildingResponse
from app.crud.building import(
    create_building,
    get_building,
    get_building_by_id,
    delete_building,
)

router = APIRouter(prefix="/buildings", tags=["Buildings"])


@router.post("/", response_model=BuildingResponse, status_code=201)
def create_new_building(building: BuildingCreate, db: Session = Depends(get_db)):
    return create_building(db, building)

@router.get("/", response_model=list[BuildingResponse])
def read_building(db: Session = Depends(get_db)):
    return get_building(db)

@router.get("/{building_id}", response_model=BuildingResponse)
def read_building(building_id: int, db: Session = Depends(get_db)):
    building = get_building_by_id(db, building_id)
    if not building:
        raise HTTPException(status_code=404, detail="Building not found")
    return building

@router.delete("/{building_id}", response_model=BuildingResponse)
def remove_building(building_id: int, db: Session = Depends(get_db)):
    building = delete_building(db, building_id)
    if not building:
        raise HTTPException(status_code=404, detail="Building not found")
    return building