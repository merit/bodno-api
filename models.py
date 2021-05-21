from sqlalchemy import Column, Integer, String, UniqueConstraint

from database import Base

class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, index=True)
    site = Column(String(255), index=True)
    first_name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(String(255), index=True)
    organization = Column(String(255))
    qr_code = Column(String(255))
    category = Column(String(255), nullable=True)
    background = Column(String(255), nullable=True)
    headshot_id = Column(String(255), nullable=True)
    position = Column(String(255), nullable=True)

    __table_args__ = (UniqueConstraint('site', 'email', __name__ = '_site_email_uc'),
                     )
