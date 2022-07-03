import requests
from requests.auth import HTTPBasicAuth
from config import url,name,pasw

# it will check if database is connected or not
def CheckTesting():
  response = requests.get(url,auth = HTTPBasicAuth(name,pasw))
  return response.text
