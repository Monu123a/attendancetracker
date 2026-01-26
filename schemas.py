from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    student_id: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True
