from fastapi import FastAPI
from app.routers import character

# run: uvicorn app.main:app --reload
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False}, debug=True)
app.include_router(character.router, prefix='/chatacter', tags=['Characters'])