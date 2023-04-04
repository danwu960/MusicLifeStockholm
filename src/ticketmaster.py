from sqlalchemy import Boolean, Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship
from consert import Consert

class TicketMaster(Base):
    __tablename__ = "ticket_master"
        id = Column(Integer, primary_key=True, index=True)
        namn = Column(String, unique=True, index=False)
        kommentar = Column(String, unique=False, index=False)
