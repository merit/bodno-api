import os

from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader, APIKey
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN

import crud
import models
import schemas
import settings
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

API_KEY = settings.API_KEY
API_KEY_NAME = "X-API-Token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(
    api_key_header: str = Security(api_key_header),
):

    if api_key_header == str(API_KEY):
        return api_key_header
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
    )

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/badge", response_model=schemas.Badge)
def create_badge(badge: schemas.BadgeCreate, db: Session = Depends(get_db), api_key=Depends(get_api_key)):
    db_badge = crud.get_badge_by_site_and_email(db, site=badge.site, email=badge.email)
    if db_badge:
        return crud.update_badge(db=db, badge_id=db_badge.id, badge=badge)
    return crud.create_badge(db=db, badge=badge)
