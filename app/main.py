from fastapi import FastAPI
from app.routers import character

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False}, debug=True)
app.include_router(character.router, prefix='/chatacter', tags=['Characters'])