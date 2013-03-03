# coding=utf-8
import json
from decider import *

test = u'{"target": {"lang": "en", "text": "Women in Tech: Put Your Money Where Your Mouth."}, "orig": {"lang": "ru", "text": "Женщины в Tech: положить ваши деньги, когда ваш рот."}}'

t = json.loads(test)

class Sentence:

    def __init__(self, lang, text):
        self.lang = lang
        self.text = text

class Translation:

    def __init__(self,orig_sent, target_sent):
        self.original = Sentence(orig_sent['lang'],orig_sent['text'])
        self.target = Sentence(target_sent['lang'],target_sent['text'])
        self.params = []

    def add_param(self,param):
        self.params.append(param)


tu = Translation(t['orig'],t['target'])

#TODO: юнит сам обращается к калькулятору и сохраняет результат его обработки в параметр
#протестировать возможность добавления параметров
#создать список параметров для пробегания по их списку и вычислению значений




