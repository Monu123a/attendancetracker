from fastapi import FastAPI, Depends, UploadFile, File
import crud, schemas, ai_service
...
@app.post('/register')
async def register_student(name: str, student_id: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Registration logic
    pass
