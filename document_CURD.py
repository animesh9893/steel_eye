import requests
from requests.auth import HTTPBasicAuth
from config import url,name,pasw,indices_name
import json

from getHeader import getHeader

def GetAllDocument(name):
  url_ = url+name+"/_search?pretty=true&q=*:*"

  payload={}
  headers = getHeader()

  response = requests.request("GET", url_, headers=headers, data=payload)

  return response.text


def InsertIntoIndices(name,data):

  url_ = url+name+"/_doc"
  payload = json.dumps(data)
  headers = getHeader()
  headers['Content-Type'] = 'application/json'

  response = requests.request("POST", url_, headers=headers, data=payload)
  return response.text
