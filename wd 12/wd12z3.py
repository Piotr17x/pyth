from lxml import html
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)

url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)

page = html.fromstring(data.text)
xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
table_div = page.get_element_by_id('collection')


table = table_div.xpath('./*[@class="table-responsive"]/table')[0]


labels = [label.strip() for label in table.xpath('.//th/text()')]

headers = [label for label in table.xpath('.//th')]
labels = []
for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        labels.append(anchor[0].strip())
    else:
        labels.append(header.text.strip())



headers = [label for label in table.xpath('.//tr/td')]
e = []
for header in headers:
    anchor = header.xpath('./text()')
    if len(anchor) > 0:
        e.append(anchor[0].strip())
    else:
        e.append(header.text.strip())
e=np.array(e)
e=e.reshape((100,7))

df=pd.DataFrame(e,columns=labels)


headers = [label for label in table.xpath('.//tr/td/div/a')]
s = []
for header in headers:
    anchor = header.xpath('./text()')
    if len(anchor) > 0:
        s.append(anchor[0].strip())
    else:
        s.append(header.text.strip())
s=np.array(s)

df['Board Game']=s

df['Num Voters'] = pd.to_numeric(df['Num Voters'])
df=df.sort_values('Num Voters',ascending=False)
print(df[:10])
etykiety=df[:10]['Board Game']
wartosci=df[:10]['Num Voters']
plt.bar(etykiety,wartosci)
plt.xticks(rotation=45)
plt.xlabel('Nazwa')
plt.ylabel('Ilosc glosow')
plt.show()