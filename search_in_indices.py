import requests
from requests.auth import HTTPBasicAuth
from config import url,indices_name
import json

from getHeader import getHeader

from model import CreateObjects

def Search(data):
  url_ = url+indices_name+"/_search"
  payload = json.dumps(data)

  headers = getHeader()
  headers['Content-Type'] = 'application/json'

  response = requests.request("POST", url_, headers=headers, data=payload)

  return CreateObjects(response.text)


def QueryRange(title:str,maxP=None,minP=None):
  d = {"range":{title:{}}}
  if maxP!=None:
    d["range"][title]["lte"] = maxP
  if minP!=None:
    d["range"][title]["gte"] = minP
  return d
