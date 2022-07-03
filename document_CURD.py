import requests
from requests.auth import HTTPBasicAuth
from config import url,name,pasw,indices_name
import json

from getHeader import getHeader
from model import CreateObjects


def GetAllDocument():
  url_ = url+indices_name+"/_search?pretty=true&q=*:*"

  payload={}
  headers = getHeader()

  response = requests.request("GET", url_, headers=headers, data=payload)

  return CreateObjects(response.text)


def InsertIntoIndices(data):

  url_ = url+indices_name+"/_doc"
  payload = json.dumps(data)
  headers = getHeader()
  headers['Content-Type'] = 'application/json'

  response = requests.request("POST", url_, headers=headers, data=payload)
  return response.text
