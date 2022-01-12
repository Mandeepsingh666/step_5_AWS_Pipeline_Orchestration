# import urllib library
from urllib.request import urlopen
import pandas as pd
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = 'https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json'
response = urlopen(url)
data_json = json.loads(response.read())

df = pd.DataFrame(data_json)

df.to_csv('out.csv')