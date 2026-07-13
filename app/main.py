from fastapi import FastAPI
from app.database import Base,engine
from app import models # must import the file containing data model
app = FastAPI()
Base.metadata.create_all(bind=engine) # yo cmnd run garaysi balla table chai database maa create vayo
# aba sabai table create hunxan jasley base class lae inherit garayko hunxa

