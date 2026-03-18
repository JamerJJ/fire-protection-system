from sqlalchemy.orm import Session
from app.models.fire_system import FireSystem
from app.models.building import Building
from app.schemas.fire_system import FireSystemCreate

def create_fire_system(db: Session, fire_system: FireSystemCreate):
    building = db.query(Building).filter(Building.id == fire_system.building_id).first()
    if not building:
        return None
    
    db_fire_system = FireSystem(**fire_system.model_dump())
    db.add(db_fire_system)
    db.commit()
    db.refresh(db_fire_system)
    return db_fire_system

def get_fire_system(db: Session):
    return db.query(FireSystem).all()


def get_fire_system_by_id(db: Session, fire_system_id: int):
    return db.query(FireSystem).filter(FireSystem.id == fire_system_id).first()

