from typing import Union

from fastapi import FastAPI

from search_in_indices import Search

app = FastAPI()


@app.get("/")
def read_root():    
    return {"Hello": "World"}



@app.get("/search")
def search(q: Union[str, None] = None):
    resp = Search({"query": {"multi_match": 
    
    {"query" : q, "fields": [
        "counterparty","instrument_id","instrument_name","trader"
    ]}}})

    return resp


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
