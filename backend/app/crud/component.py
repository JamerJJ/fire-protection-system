from sqlalchemy.orm import Session

from app.models.component import Component
from app.models.fire_system import FireSystem
from app.models.component import ComponentCreate


def create_component(db: Session, component: ComponentCreate):
    fire_system = db.query(FireSystem).filter(FireSystem.id == component.system_id).first()
    if not fire_system:
        return None
    
    db_component = Component(**component.model_dump())
    db.add(db_component)
    db.commit()
    db.refresh(db_component)

    return db_component


def get_components(db: Session):
    return db.query(Component).all()

def get_component_id(db: Session, component_id: int):
    return db.query(Component).filter(Component.id == component_id).first()

def delete_component(db: Session, component_id: int):
    component = db.query(Component).filter(Component.id == component_id).first()

    if component:
        db.delete(component)
        db.commit()

    return component
