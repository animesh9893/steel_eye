from typing import Union

from fastapi import FastAPI

from search_in_indices import Search,QueryRange

app = FastAPI()


@app.get("/")
def read_root():    
    return {"Hello": "World"}


@app.get("/search")
def search(q: Union[str, None] = None,
    assetClass:Union[str,None]=None,
    minPrice:Union[str,None]=None,
    maxPrice:Union[str,None]=None,
    start:Union[str,None]=None,
    tradeType:Union[str,None]=None,
    end:Union[str,None]=None):

    print(q,assetClass,minPrice,start,tradeType,end)

    query = {"query":{"bool":{"must":[    ]}}}
    
    if q!=None:
        query["query"]["bool"]["must"].append({"multi_match": {"query" :q, "fields": ["counterparty","instrument_id","instrument_name","trader"]}})
    if minPrice!=None or maxPrice!=None:
        query["query"]["bool"]["must"].append(QueryRange("price",maxP=maxPrice,minP=minPrice))
    if start!=None or end!=None:
        query["query"]["bool"]["must"].append(QueryRange("trade_date_time",maxP=maxPrice,minP=minPrice))
    if assetClass!=None:
        query["query"]["bool"]["must"].append({"multi_match": {"query" :assetClass, "fields": ["asset_class"]}})
    if tradeType!=None:
        query["query"]["bool"]["must"].append({"multi_match": {"query" :tradeType, "fields": ["asset_class"]}})

    return Search(query)



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


