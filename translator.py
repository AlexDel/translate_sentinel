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
            'key':u'trnsl.1.1.20130423T102226Z.0b47a720ba5cd3e5.1fc5823cac31e3cf5b1fcfc034ae67ab330b90a0'
        }
        return  json.loads(requests.post(self.url, data).text)['text'][0]