from fastapi import APIRouter, HTTPException
from uuid import UUID
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import supabase
from app.models.character import Character, CharacterUpdate

router = APIRouter()

@router.get('/', response_model=list[Character])
def get_characters():
    res = supabase.table('character').select('*').execute()
    return res.data

@router.post('/')
def create_character(character: Character):
    character_data = jsonable_encoder(character)
    res = supabase.table('character').insert(character_data).execute()
    return res.data[0]

@router.patch('/{id}')
def update_character(id: UUID, update_data: CharacterUpdate):
    update_data = jsonable_encoder(update_data)

    if not update_data:
        raise HTTPException(status_code=400, detail="No data to update")
    
    resposne = (
        supabase
        .table('character')
        .update(update_data)
        .eq('id', id)
        .execute()
    )

    if resposne.data:
        return resposne.data[0]
    else:
        raise HTTPException(status_code=404, detail="Character not found")
    
@router.delete('/{id}')
def delete_character(id: UUID):
    res = supabase.table('character').delete().eq('id', id).execute()

    if res.data and len(res.data) > 0:
        return {'message': 'Character deleted successfully!'}
    else:
        raise HTTPException(status_code=404, detail="Character not found")