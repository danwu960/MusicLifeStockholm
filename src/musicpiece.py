from salalchemy import String, Boolean, Integer, Column, Foreignkey
from salalchemy.orm import relationship
from database.connection import Base
from actor import Actor

class Musicpiece(Base):
    __tablename__ = "verk"
    id = Column(Integer, primary_key=True, index=True)
    namn = Column(String, unique=False, index=False)
    tonsattare = Column(Integer, unique=False, index=False)
    aktor = Column(Integer, Foreignkey='', unique=False, index=False)
    verk_typ = Column(Integer, Foreignkey='verk_typ.id', unique=False,
                      index=False)

    music_aktor = relationship("Actor", back_populates="actor_music",
                               uselist=False)
    music_type = relationship("Musictype", back_populates="piece_type",
                              uselist=False)

class Musictype(Base):
    __tablename__ = "verk_typ"
    id = Column(Integer, primary_key=True, index=True)
    namn = Column(String, unique=False, index=False)

    piece_type = relationship("Musicpiece", back-populates="music_type", \
                                                           uselist=False)
