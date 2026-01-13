from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas, crud, face_ops

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/health')
def health():
    return {'status': 'up'}

@app.post('/register', response_model=schemas.StudentResponse)
async def register(name: str, student_id: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    if crud.get_student_by_id(db, student_id): raise HTTPException(status_code=400, detail='Exists')
    enc = face_ops.map_face(face_ops.parse_image(await file.read()))
    if enc is None: raise HTTPException(status_code=400, detail='No face')
    return crud.create_student(db, schemas.StudentCreate(name=name, student_id=student_id), face_ops.to_bytes(enc))

@app.post('/recognize')
async def recognize(file: UploadFile = File(...), db: Session = Depends(get_db)):
    enc = face_ops.map_face(face_ops.parse_image(await file.read()))
    if enc is None: raise HTTPException(status_code=400, detail='No face')
    students = crud.get_all_students(db)
    known, sids = [], []
    for s in students:
        if s.face_data:
            known.append(face_ops.from_bytes(s.face_data))
            sids.append(s.id)
    idx = face_ops.identify(known, enc)
    if idx == -1: raise HTTPException(status_code=404, detail='Not found')
    crud.log_presence(db, sids[idx])
    return {'status': 'success', 'match': sids[idx]}
