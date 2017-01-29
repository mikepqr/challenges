import pandas as pd
import requests
import datetime

today = datetime.datetime.now().strftime('%Y%m%d')

data = requests.get('https://gist.githubusercontent.com/jorin-vogel/7f19ce95a9a842956358/raw/e319340c2f6691f9cc8d8cc57ed532b5093e3619/data.json')
df = pd.DataFrame(data.json())

#df['timestamp'] = pd.to_datetime(df['timestamp'])
#df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%Y%m%d'))
#print df

output = df[['name', 'creditcard']]
output = output[output['creditcard'].notnull()]
output.to_csv(today+'.csv', index=False)
