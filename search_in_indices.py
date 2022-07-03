import requests
from requests.auth import HTTPBasicAuth
from config import url,indices_name
import json

from getHeader import getHeader

from model import CreateObjects

def POSTrequest(url,headers,data):
  response = requests.request("POST", url_, headers=headers, data=payload)
  return response.text


def Search(data):
  url_ = url+indices_name+"/_search"
  payload = json.dumps(data)

  headers = getHeader()
  headers['Content-Type'] = 'application/json'

  response = requests.request("POST", url_, headers=headers, data=payload)

  return CreateObjects(response.text)
