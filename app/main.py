from fastapi import FastAPI
from app.routers import character
from app.routers import quote
from app.routers import media

# run: uvicorn app.main:app --reload
app = FastAPI(
    title="Gachimuchi API",
    description="A serious place for ♂real men♂. This API lets you add, search, and store iconic quotes and media from the most powerful warriors of the male universe.",
    swagger_ui_parameters={"syntaxHighlight": False}, 
    debug=True
)
app.include_router(character.router, prefix='/chatacter', tags=['Characters'])
app.include_router(quote.router, prefix='/quote', tags=['Quotes'])
app.include_router(media.router, prefix='/media', tags=['Media'])