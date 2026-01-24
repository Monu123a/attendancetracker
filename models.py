from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, index=True)
    name = Column(String)
    logs = relationship('AttendanceLog', back_populates='student')

class AttendanceLog(Base):
    __tablename__ = 'attendance_logs'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    student = relationship('Student', back_populates='logs')
