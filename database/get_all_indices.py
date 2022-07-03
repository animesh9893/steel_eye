import requests
from requests.auth import HTTPBasicAuth
from config import url,name,pasw

def GetAllIndices():
  url_ = url+"_cat/indices"
  response = requests.get(url_,auth = HTTPBasicAuth(name,pasw))
  return response.text


if __name__ == '__main__':
  print(GetAllIndices())