import requests
from pycognito.utils import RequestsSrpAuth
import os

username = os.getenv('username')
password = os.getenv('password')

auth = RequestsSrpAuth(
  username=username,
  password=password,
  user_pool_id='us-east-1_GUFWfhI7g',
  client_id='19efs8tgqe942atbqmot5m36t3',
  user_pool_region='us-east-1',
)

response = requests.get('https://app-prod.mysa.cloud/users/readingsForUsers', auth=auth)

print(response.json)