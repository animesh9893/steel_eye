import datetime as dt

from typing import Optional
from pydantic import BaseModel, Field
from pydantic import ValidationError, validator

import json

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(default=None,description="A value of BUY for buys, SELL for sells.")
    price: float = Field(default=None,description="The price of the Trade.")
    quantity: int = Field(default=None,description="The amount of units traded.")

class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")
    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")
    instrument_id: str = Field(alias="instrumentId",default=None, description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
    instrument_name: str = Field(alias="instrumentName",default=None, description="The name of the instrument traded.")
    trade_date_time: dt.datetime = Field(alias="tradeDateTime",default=None, description="The date-time the Trade was executed")
    trade_details: TradeDetails = Field(alias="tradeDetails",default=None, description="The details of the trade, i.e. price, quantity")
    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")
    trader: str = Field(default=None,description="The name of the Trader")


def createTradeDetails(buySellIndicator,price,quantity):
    obj = TradeDetails()
    obj.buySellIndicator = buySellIndicator
    obj.price = price
    obj.quantity = quantity
    return obj

def createTrade(data):
    obj = Trade()
    obj.asset_class = data["asset_class"]
    obj.counterparty = data["counterparty"]
    obj.instrument_id = data["instrument_id"]
    obj.instrument_name = data["instrument_name"]
    obj.trade_date_time = data["trade_date_time"]
    obj.trade_details = createTradeDetails(data["buySellIndicator"],data["price"],data["quantity"])
    obj.trade_id = data["trade_id"]
    obj.trader = data["trader"]

    return obj

def objectToJSON(obj):
    return obj.json()


def stringToJSON(s):
    return json.loads(s)

def CreateObjects(data):
    resp = {}
    data = stringToJSON(data)
    if "error" in data:
        resp["error"] = True
        resp["error_cause"] = data["error"]
        return resp
    resp["error"] = False
    resp["error_cause"] = None

    objs = data["hits"]["hits"]
    resp["data"] = []

    for item in objs:
        temp = createTrade(item["_source"])
        resp["data"].append(temp)
        
    print("Request send this data")
    print(resp)

    return resp

