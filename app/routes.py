from fastapi import APIRouter,Depends,status
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