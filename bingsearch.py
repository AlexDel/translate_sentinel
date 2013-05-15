# coding=utf-8
import requests

URL = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/Web?Query=%(query)s&$top=50&$format=json'
API_KEY = u'zo2F7b3jIjkGBGIPIGV/7T8VdbJA1gBtEWEHi2SldVY='

def request(query, **params):
    r = requests.get(URL % {'query': query}, auth=(API_KEY, API_KEY))

    return r
