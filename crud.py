from sqlalchemy.orm import Session
import models, schemas

def get_student_by_id(db: Session, student_id: str):
    return db.query(models.Student).filter(models.Student.student_id == student_id).first()

def get_all_students(db: Session):
    return db.query(models.Student).all()

def create_student(db: Session, payload: schemas.StudentCreate, enc: bytes = None):
    st = models.Student(name=payload.name, student_id=payload.student_id, face_data=enc)
    db.add(st)
    db.commit()
    db.refresh(st)
    return st

def log_presence(db: Session, student_id: int):
    log = models.AttendanceLog(student_id=student_id)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
