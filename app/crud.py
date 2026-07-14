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
def get_note( db:Session):
    return db.query(models.Note).all
def get_note_id(db:Session,note_id:int):
    return db.query(models.Note).filter(models.Note.id== note_id).first()
def update_note(db:Session, note_id:int,note:schemas.NoteUpdate):
    db_note =db.query(models.Note).filter(models.Note.id== note_id).first()
    if db_note is None:
        return None
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note