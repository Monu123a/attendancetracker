from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    student_id = Column(String, unique=True, index=True)
    face_data = Column(LargeBinary, nullable=True)
    logs = relationship('AttendanceLog', back_populates='student', cascade='all, delete')

class AttendanceLog(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    student = relationship('Student', back_populates='logs')
