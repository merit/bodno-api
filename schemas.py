from typing import Optional

from pydantic import BaseModel

class BadgeBase(BaseModel):
    site: str
    first_name: str
    last_name: str
    email: str
    organization: str
    qr_code: str
    category: Optional[str] = None
    background: Optional[str] = None
    headshot_id: Optional[str] = None
    position: Optional[str] = None

class BadgeCreate(BadgeBase):
    pass

class Badge(BadgeBase):
    id: int

    class Config:
        orm_mode = True
