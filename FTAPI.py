import requests
import json
import os
from bs4 import BeautifulSoup

#initialize variables
sites = [{
    'name':'goal',
    'address':'https://www.goal.com/en-us'
    ,'base':""
},
{
    'name':'sky sports',
    'address':'https://www.skysports.com'
    ,'base':"https://www.skysports.com"
},
{
    'name':'footballtransfers',
    'address':'https://www.footballtransfers.com/en',
    'base':""
},
{
    'name':'espn',
    'address':'https://www.espn.com/soccer/transfers',
    'base':""
},
{
    'name':'mirror',
    'address':'https://www.mirror.co.uk/sport/football/transfer-news/',
    'base':""
}
] 
articles = []
#scrapes sites 
for site in sites:
    response = requests.get(site['address'])
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', text='transfer')
    for link in links:
        title = link.text
        url = link['href']
        articles.append({
            'title': title,
            'url': site['base'] + url,
            'source': site['name']
        })

#write to json file
with open('articles.json', 'w') as outfile:
    json.dump(articles, outfile)

#read from json file
with open('articles.json', 'r') as infile:
    articles = json.load(infile)

#listen to changes on port 8000
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)