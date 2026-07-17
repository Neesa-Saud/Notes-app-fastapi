from sqlalchemy.orm import Session
from app import schemas, models
from sqlalchemy import or_
def create_note(db:Session,note: schemas.NoteCreate):
    db_note = models.Note(
        title = note.title,
        content = note.content
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note) #changes seen after this 
    return db_note
def get_note( db:Session,search : str = "",page: int =1,limit:int = 10):
    query =  db.query(models.Note)
    if search :
        query = query.filter(
            or_( #returns the row where either condition is true
                 models.Note.title.ilike(f"%{search}%"),
                models.Note.content.ilike(f"%{search}%")
            )
        )
    skip = (page - 1)*limit
    return query.offset(skip).limit(limit).all()
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
def delete_note(db:Session,note_id:int):
  db_note =db.query(models.Note).filter(models.Note.id== note_id).first()
  if db_note is None:
      return None
  db.delete(db_note)
  db.commit()
  return db_note