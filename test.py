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
def read_root():
    post = fetch.get_listing_details('c8993477-60b7-3735-826f-8111b9a9df22')
    item = Item(title =post['data']['listing']['originalTitle'], price = post['data']['listing']['originalPrice'], pics = post['data']['listing']['photos'], description = post['data']['listing']['description'])
    return item.model_dump_json() 