from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from app import crud,schemas
from app.dependency import get_db
router = APIRouter(
    prefix= "/notes",
    tags=["Notes"]
)
@router.post("/",response_model= schemas.NoteResponse,
             status_code=status.HTTP_201_CREATED)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db)
):
    return crud.create_note(db,note)
@router.get("/",response_model=list(schemas.NoteResponse))
def get_notes(db:Session = Depends(get_db)):
    return crud.get_note(db)
@router.get("/{note_id}",response_model=schemas.NoteResponse)
def get_note_id(note_id:int ,db:Session = Depends(get_db)):
    note=crud.get_note_id(db,note_id)
    if note is None :
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )
    return note 
@router.put("/{note_id}",response_model=schemas.NoteResponse)
def update_note(
    note_id :int,
    note:schemas.NoteUpdate,
    db: Session = Depends(get_db)
):
    updated_note = crud.update_note(db,note_id,note)
    if update_note is None :
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )
    return update_note 
@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id:int , db : Session = Depends(get_db)):
    deleted_note =  crud.delete_note(db,note_id)

    if deleted_note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)