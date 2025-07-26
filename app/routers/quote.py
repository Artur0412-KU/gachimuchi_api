from fastapi import APIRouter, HTTPException
from uuid import UUID
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import supabase
from app.models.quote import Quote, UpdateQuote

router = APIRouter()

@router.get('/', response_model=list[Quote])
def get_quotes():
    res = supabase.table('quote').select('*').execute()
    return res.data

@router.post('/')
def add_quote(quote: Quote):
    quote_data = jsonable_encoder(quote)
    res = supabase.table('quote').insert(quote_data).execute()
    return res.data


@router.patch('/{id}')
def update_quote(id: UUID, update_data: UpdateQuote):
    data = jsonable_encoder(update_data, exclude_unset=True)

    if not data:
        raise HTTPException(status_code=400, detail="No data to update")

    res = supabase.table('quote').update(data).eq('id', id).execute()

    if res.data:
        return res.data[0]
    else:
        raise HTTPException(status_code=404, detail="Quote not found")