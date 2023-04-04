'''
add a new actor, delete and display one, editing one with checking functions of variables
'''
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.connection import Base
from musicpiece import Musicpiece


# mapper to the tables
class Nation(Base):
    __tablename__ = "nation"
    id = Column(Integer, primary_key=True, index=True)
    name = Column("nation_namn", String, unique=True, index=False)

    nation_actor = relationship('Actor', back_populates='from_nation')
    actor_active = relationship('ActorActive', back_populates='actor_nation')

class Instrument(Base):
    __tablename__ = "instrument"
    instrument_id = Column(Integer, primary_key=True, index=True)
    instrument_namn = Column(String, unique=True, index=False)
    instrument_kommentar = Column(String, unique=False, index=False)

    instrument_actor = relationship('Actor', back_populates='use_instrument')

class Gender(Base):
    __tablename__ = "aktor_typ"
    gender_id = Column(Integer, primary_key=True, index=True)
    description = Column(String, unique=True, index=False)

    gender_actor = relationship('Actor', back_populates='actor_gender')


class Actor(Base):

    __tablename__ = "aktor"
    id = Column("aktor_id", Integer, primary_key=True, index=True)
    name = Column('a_namn', String, unique=False, index=False)
    comment = Column('kommentar', String, unique=False, index=False)
    composer = Column('tonsattare', Boolean, unique=False, index=False)
    born = Column('fodd', Integer, unique=False, index=False)
    death = Column('dod', Integer, unique=False, index=False)
    active_start = Column('aktivstart', Integer, unique=False, index=False)
    active_end = Column('aktivslut', Integer, unique=False, index=False)
    nation = Column('nation', Integer, ForeignKey('nation.id'), unique=False, index=False)
    url = Column('url', String, unique=False, index=False)
    instrument = Column('huvudinstrument', Integer, ForeignKey('instrument.instrument_id'), unique=False, index=False)
    gender = Column('typ', Integer, ForeignKey('aktor_typ.gender_id'), unique=False, index=False)

    use_instrument = relationship('Instrument', back_populates="instrument_actor", uselist=False)
    actor_gender = relationship('Gender', back_populates="gender_actor", uselist=False)
    from_nation = relationship('Nation', back_populates="nation_actor", uselist=False)
    actor_active = relationship('ActorActive', back_populates='actor')
    actor_music = relationship("Musicpiece", back_populates='music_aktor',
                               uselist=False)


# this is many to many relationship
class ActorActive(Base):
    __tablename__ = "aktor_verksam"
    actor_id = Column('aktor_id', Integer, ForeignKey('aktor.aktor_id'), primary_key=True, index=True)
    nation_id = Column('verksamnation', Integer, ForeignKey('nation.id'), primary_key=True, index=True)

    actor_nation = relationship('Nation', back_populates="actor_active")
    actor = relationship('Actor', back_populates="actor_active")


class NationReq(BaseModel):
    id: int
    country_name: str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "country_name": "Sweden"
            }
        }

class GenderReq(BaseModel):
    id: int
    description: str
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "description": "woman"
        }
    }

class InstrumentReq(BaseModel):
    id: int
    name: str
    comment: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "piano",
                "comment": "18 centry and something"
            }
        }


# this class describe the attributes returned in http, it is not exactly the same as the table, e.g. nation is the object nation containing id and name.
class ActorReq(BaseModel):
    actor_id: int
    name: str
    comment: str
    composer: bool
    born: int
    death: int
    active_start: int
    active_end: int
    nation: int
    url: str
    instrument: int
    gender: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "actor_id": 3,
                "name": "Mozart",
                "comment": "Something about him",
                "composer": True,
                "born": 1800,
                "death": 1867,
                "active_start": 1810,
                "active_end": 1867,
                "nation": 1,
                "url": "http://wikipedia/mozart/en",
                "instrument": 5,
                "gender": 3}
        }


class ActorJointReq(BaseModel):
    actor_id: int
    name: str
    comment: str
    composer: bool
    born: int
    death: int
    active_start: int
    active_end: int
    nation: NationReq
    url: str
    instrument: InstrumentReq
    gender: GenderReq

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "actor_id": 3,
                "name": "Mozart",
                "comment": "Something about him",
                "composer": True,
                "born": 1800,
                "death": 1867,
                "active_start": 1810,
                "active_end": 1867,
                "nation": {"id": 1, "country_name": 'Sverige'},
                "url": "http://wikipedia/mozart/en",
                "instrument": {"id": 5, "name": 'Kontrabas'},
                "gender": {"id": 3, "description": 'Orgnization'}
            }
        }
        #add into the da
