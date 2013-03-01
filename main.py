import json
from decider import *

test = '{"target": {"lang": "en", "text": "Women in Tech: Put Your Money Where Your Mouth\\u00a0Is."}, "orig": {"lang": "ru", "text": "\\u00c6\\u00e5\\u00ed\\u00f9\\u00e8\\u00ed\\u00fb \\u00e2 \\u00ee\\u00e1\\u00eb\\u00e0\\u00f1\\u00f2\\u00e8 \\u00f2\\u00e5\\u00f5\\u00ed\\u00ee\\u00eb\\u00ee\\u00e3\\u00e8\\u00e9: \\u00ef\\u00f0\\u00e8\\u00f1\\u00f2\\u00f0\\u00ee\\u00e9\\u00f2\\u00e5 \\u00e2\\u00e0\\u00f8\\u00e8 \\u00e4\\u00e5\\u00ed\\u00fc\\u00e3\\u00e8."}}'


class Exchanger:
    'This method performs communication with langprism'

    def __init__(self, obj = None):
        ''' Initialize class by getting json form LangPrism'''
        trans_unit = json.loads(obj)
        self.orig_lang = trans_unit['orig']['lang']
        self.orig_text = trans_unit['orig']['text']

        self.target_lang = trans_unit['target']['lang']
        self.target_text = trans_unit['target']['text']


t = Exchanger(test)

print t.orig