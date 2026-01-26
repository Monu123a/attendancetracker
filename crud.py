from sqlalchemy.orm import Session
import models, schemas

def get_student_by_id(db: Session, student_id: str):
    return db.query(models.Student).filter(models.Student.student_id == student_id).first()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, student_id=student.student_id)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
