from sqlalchemy.orm import Session
from app.models.building import Building
from app.schemas.building import BuildingCreate


def create_building(db: Session, building: BuildingCreate) -> Building:
    db_building = Building(**building.model_dump())
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building

def get_building(db: Session):
    return db.query(Building).all()

def get_building_by_id(db: Session, building_id: int):
    return db.query(Building).filter(Building.id == building_id).first()

def delete_building(db: Session, building_id: int):
    building = db.query(Building).filter(Building.id == building_id).first()
    if building:
        db.delete(building)
        db.commit()
    return building 

