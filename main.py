from typing import Union, List

from fastapi import FastAPI,Query

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
    sortD:List[str] = Query(default=[]),
    sortA:List[str] = Query(default=[]),
    end:Union[str,None]=None):

    print(sortD)

    query = {"query":{"bool":{"must":[    ]}},"sort": ["_score"]}
    
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
    if len(sortD)>0:
        for i in sortD:
            query["sort"].append({i: "desc"})
    if len(sortA)>0:
        for i in sortA:
            query["sort"].append({i: "asc"})


    return Search(query)



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


