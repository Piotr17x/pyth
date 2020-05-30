from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

xpath = '//h2/a[@class="stretched-link link-text-color"]'

foundElements = page.xpath(xpath)
for element in foundElements :
   print(element.tag, element.keys())
   for name, value in sorted(element.items()):
       if(name=="ng-href"):
        print('%s = %r' % (name, value))