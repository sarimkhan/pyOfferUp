from pyOfferUp import fetch
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()
class Item(BaseModel):
    title: str
    price: float
    pics: list
    description: str

@app.get("/item/{itemId}")
def read_root(itemId):
    post = fetch.get_listing_details(itemId)
    item = Item(title =post['data']['listing']['originalTitle'], price = post['data']['listing']['originalPrice'], pics = post['data']['listing']['photos'], description = post['data']['listing']['description'])
    return item.model_dump_json() 