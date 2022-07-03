from typing import Union, List

from fastapi import FastAPI,Query
import json

from search_in_indices import Search,QueryRange,GetPITid
from document_CURD import GetAllDocument,InsertIntoIndices

from model import Trade

from pingDatabase import CheckTesting

app = FastAPI()

def stringToJSON(s):
    return json.loads(s)


# home url return sample result from elastic search
@app.get("/")
def read_root():    
    return GetAllDocument()

# search API with advance filter
@app.get("/search")
def search(q: Union[str, None] = None,
    assetClass:Union[str,None]=None,
    size:Union[int,None]=None,
    minPrice:Union[str,None]=None,
    maxPrice:Union[str,None]=None,
    start:Union[str,None]=None,
    tradeType:Union[str,None]=None,
    pitId:Union[str,None]=None,
    sortD:List[str] = Query(default=[]),
    sortA:List[str] = Query(default=[]),
    end:Union[str,None]=None):

    if pitId==None:
        pitId = stringToJSON(GetPITid())
        pitId = pitId["id"]
    if size==None:
        size=10
    query = {"size":size,"query":{"bool":{"must":[]}},"sort": ["_score"]}
    
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

# API for inserting indices to elasticsearch cloud
@app.post("/insertIndices")
async def insetIndices(trade: Trade):
    InsertIntoIndices(trade.json())
    return trade

# check database is working or not
@app.get("/check")
def read_root():    
    return {"resp":CheckTesting()}
