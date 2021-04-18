from sqlalchemy.orm import Session

import models, schemas

def get_badge_by_site_and_email(db: Session, site: str, email: str):
    return db.query(models.Badge).filter(
        models.Badge.site == site,
        models.Badge.email == email
    ).first()

def create_badge(db: Session, badge: schemas.BadgeCreate):
    db_badge = models.Badge(**badge.dict())
    db.add(db_badge)
    db.commit()
    db.refresh(db_badge)
    return db_badge

def update_badge(db: Session, badge_id: int, badge: schemas.BadgeCreate):
    db_badge = db.query(models.Badge).filter(
        models.Badge.id == badge_id
    ).update(badge.dict())
    db.commit()
    return db.query(models.Badge).get(badge_id)
