from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import supabase
from app.models.character import Character

router = APIRouter()

@router.get('/', response_model=list[Character])
def get_characters():
    res = supabase.table('character').select('*').execute()
    print("DEBUG DATA:", res)
    return res.data

@router.post('/')
def create_character(character: Character):
    character_data = jsonable_encoder(character)
    res = supabase.table('character').insert(character_data).execute()
    return res.data[0]
