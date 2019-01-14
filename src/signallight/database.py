from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Text,DATETIME

Base = declarative_base()
class Services(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    url = Column(Text, nullable=False)
    ext = Column(Integer, nullable=False)
    create_at = Column(DATETIME, nullable=False)
    update_at = Column(DATETIME, nullable=False)

# class EventLogs(Base):
#     __tablename__ = 'event_logs'
#     id = Column(Integer, primary_key=True)
#
# class Statuses(Base):
#     __tablename__ = 'statuses'
#     id = Column(Integer, primary_key=True)

engine = create_engine('sqlite:///signallight.db')

Base.metadata.create_all(engine)