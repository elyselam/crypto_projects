from mozscape import Mozscape
from contextlib import closing
import traceback
import time
import pandas as pd
from urllib.parse import urlparse
import csv
import random

# Imput your member ID and secret key here
client = Mozscape('mozscape-c75d15e616', '5128f75efae32ed916a6eac395831ee3')
data = pd.read_csv('ICO-URL-Symbol.csv', encoding = "utf8")
url_column = data['URL']
remove_row_index = []
urls = data.drop(data.index[remove_row_index])
url_columns = urls['URL']
clean_list = []

for i in url_columns:

        clean_list.append(i)
        
clean_urls = []

for i in clean_list:
    clean_urls.append(i.split('/', 1)[0])
urls['index_URL'] = clean_urls
urls_10 = clean_urls

for i in urls_10:
#    metrics = client.urlMetrics(i)
    try:
        print(client.links(i))
        time.sleep(random.randint(2, 3))
        time.sleep(random.randint(2, 3))
    except:
        print(i + " could not be looked up due to rate limiting.")
        time.sleep(10)


