'''handle adding new consert or delete or display the conserts'''
import datetime
from pydantic import BaseModel
from sqlmodel import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
import database.connection as Base


class Consert(Base):
    __tablename__ = "Konsert"
    id = Column(Integer, primary_key=True, index=True)
    namn = Column(String, unique=False, index=False)
    datum = Column(Date, unique=False, index=False)
    kommentar = Column(String, unique=False, index=False)
    lokal_id = Column(Integer, ForeignKey('konsert_lokal.id'), unique=False, \
                                                              index=False)
    arrangor_id = Column(Integer, ForeignKey('arrangor.arrangor_id'),
    unique=False, index=False)
    biljetpris = Column(String, unique=False, index=False)
    konserttid = Column(String, unique=False, index=False)
    konserttyp = Column(Integer, ForeignKey('konsert_typ.id'), unique=False, \
                                                              index=False)

    location = relationship('ConsertLocation',
                            back_populates="consert_location", uselist=False)
    organizer = relationship('Organizer',
                             back_populates="consert_organizer", uselist=False)
    type = relationship('ConsertType',
                        back_populates="consert_type", uselist=False)

class ConsertLocation(Base):
    __tablename__ = "konsert_lokal"
    id = Column(Integer, primary_key=True, index=True)
    namn = Column(String, unique=False, index=False)
    typ = Column(String, unique=False, index=False)
    kommentar = Column(String, unique=False, index=False)

    consert_location = relationship('Consert', back_populates="location")

class Organizer(Base):
     __tablename__ = "arrangor"
     arrangor_id = Column(Integer, primary_key=True, index=True)
     a_namn = Column(String, unique=False, index=False)
     kommentar = Column(String, unique=False, index=False)

     consert_organizer = relationship('Consert', back_populates="organizer")

class ConsertType(Base):
    __tablename__ = "konsert_typ"
    id = Column(Integer, primary_key=True, index=True)
    namn = Column(String, unique=False, index=False)

    consert_type = relationship('Consert', back_populates="type")

class Roll(Base):
    __tablename__ = "roll"
    id = Column(Integer, primary_key=True, index=True)
    namn = Column(String, unique=True, index=False)
    kommentar = Column(String, unique=False, index=False)


class ConsertReq(BaseModel):
                name: str
                date: datetime
                comment: str
                location: int
                orgnizer: int
                price_str: str
                time_str: str  # irregular time
                type: int

                class Config:
                    schema_extra = {
            "example": {
                "name": "Christmas choir 2022",
                "c_date": "2022-12-22",
                "comment": "something to say",
                "location": 3,
                "orgnizer": 2,
                "price_str": "4 p for men ",
                "time_str": "sunday or something",
                "type": 5
            }
        }
