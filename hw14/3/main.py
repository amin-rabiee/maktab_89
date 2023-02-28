from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import engine, session_local
import schemas, models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

