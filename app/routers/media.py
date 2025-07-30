from fastapi import APIRouter, HTTPException, Query
from uuid import UUID
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import supabase
from app.models.media import Media, UpdateMedia
from typing import Optional

router = APIRouter()

@router.get('/', response_model=list[Media])
def get_media():
    res = supabase.table('media').select('*').execute()
    return res.data

# search
@router.get('/search-media')
def search_media(
    title: Optional[str] = Query(description="Search a name of media"),
):
    res = supabase.table('media').select('title, file_url').ilike('title', f"{title}%").execute()
    return res.data

# add a media with a character id
@router.post('/{character_id}')
def add_media(character_id: UUID, media: UpdateMedia):
    character_data = supabase.table('character').select('id').eq('id', str(character_id)).execute()
    if not character_data:
        raise HTTPException(status_code=400, detail="Character not found")
    
    media_data = jsonable_encoder(media)
    res=  supabase.table('media').insert(media_data).execute()
    return res.data

# add a media without a character id
@router.post('/')
def add_media_without_character(media: UpdateMedia):
    media_data = jsonable_encoder(media)
    res=  supabase.table('media').insert(media_data).execute()
    return res.data


# update media
@router.patch('/{id}')
def update_media(id: UUID, media: UpdateMedia):
    update_media = jsonable_encoder(media)

    if not update_media:
        raise HTTPException(status_code=400, detail="No data to update")
    
    res = supabase.table('media').update(update_media).eq('id', id).execute()

    if res.data:
      return res.data[0]
    else:
        raise HTTPException(status_code=404, detail="Media not found")
    

# delete media
@router.delete('/{id}')
def delete_media(id: UUID):
    res = supabase.table('media').delete().eq('id', id).execute()

    if res.data:
        return {'message': 'Media deleted successfully'}
    else:
        raise HTTPException(status_code=404, detail="Media not found")