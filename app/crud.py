from sqlalchemy.orm import Session
from app import schemas, models
def create_note(db:Session,note: schemas.NoteCreate):
    db_note = models.Note(
        title = note.title,
        content = note.content
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note) #changes seen after this 
    return db_note
