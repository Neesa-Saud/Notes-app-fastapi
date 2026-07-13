from pydantic import BaseModel , Field,ConfigDict
from datetime import datetime
class NoteCreate(BaseModel):
    title : str = Field(...,min_length=1,max_length=200)
    content :str = Field(...,min_length=1)
class NoteResponse(BaseModel):
    id:int
    title:str
    content:str
    created_at: datetime
    model_config : ConfigDict(from_attributes=True)