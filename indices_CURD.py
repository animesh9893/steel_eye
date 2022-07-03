import requests
from config import url,name,pasw,indices_name
from getHeader import getHeader
from requests.auth import HTTPBasicAuth

# this will create indices in elastic cloud
def CreateIndices(name):
  url_ =url+name

  payload={}
  headers = getHeader()

  response = requests.request("PUT", url_, headers=headers, data=payload)

  return response.text

# this will delete indices
def DeleteIndices(name):
  url_ =url+name

  payload={}
  headers = getHeader()

  response = requests.request("DELETE", url_, headers=headers, data=payload)

  return response.text

# it will return all presernt indices
def GetAllIndices():
  url_ = url+"_cat/indices"
  response = requests.get(url_,auth = HTTPBasicAuth(name,pasw))
  return response.text

