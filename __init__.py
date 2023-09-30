import os
import requests

AZURE_BING_KEY = os.environ.get('AZURE_BING_KEY')

class ResultObj:
    def __init__(self, title, link, description):
        self.title = title
        self.url = link
        self.description = description
    
def search(query, advanced=False, num_results=10, lang='zh_TW'):
    headers = {'Ocp-Apim-Subscription-Key': AZURE_BING_KEY}
    params = {'q': query, 'mkt': lang, 'count': num_results}
    url = 'https://api.bing.microsoft.com/v7.0/search'
    res = requests.get(url, headers=headers, params=params)
    json = res.json()
    res.close()

    for item in json['webPages']['value']:
        if advanced:
            yield ResultObj(
                item['name'], 
                item['url'], 
                item['snippet'] if 'snippet' in item else "" )
        else:
            yield item['url']