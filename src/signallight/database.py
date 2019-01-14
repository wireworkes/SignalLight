from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Text,DATETIME,ForeignKey
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    url = Column(Text, nullable=False)
    ext = Column(Integer, nullable=False)
    create_at = Column(DATETIME, nullable=False)
    update_at = Column(DATETIME, nullable=False)

class EventLog(Base):
    __tablename__ = 'event_logs'
    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('statuses.service_id'))
    detail = Column(Text, nullable=False)
    date = Column(DATETIME, nullable=False)

class Status(Base):
    __tablename__ = 'statuses'
    service_id = Column(Integer, primary_key=True)
    status = Column(Integer, nullable=False)


engine = create_engine('sqlite:////home/wireworkes/PycharmProjects/SignalLight/db/signallight.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# test_status = Status(service_id=9999,status=999)
# session.add(test_status)
# session.commit()

statuses = session.query(Status).all()
for status in statuses:
    print(status.service_id)
