# coding=utf-8
import json
import requests

url = 'http://translate.yandex.net/api/v1/tr.json/translate'

data = {
    'lang':'ru-en',
    'text':u'Текст, для которого требуется определить язык.',
    'format': u''

}


r = requests.post(url, data)

print r.text
