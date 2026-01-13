from pydantic import BaseModel
import datetime

class StudentBase(BaseModel):
    name: str
    student_id: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        orm_mode = True

class LogResponse(BaseModel):
    id: int
    student_id: int
    timestamp: datetime.datetime
    class Config:
        orm_mode = True
