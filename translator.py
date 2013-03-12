# coding=utf-8
import json
import requests

class Translator:

    def __init__(self):
        self.url = 'http://translate.yandex.net/api/v1/tr.json/translate'

    def translate(self, text, or_lang, tar_lang):
        data = {
            'lang': u'%s-%s' % (or_lang, tar_lang),
            'text': unicode(text),
        }
        return  json.loads(requests.post(self.url, data).text)['text'][0]