# coding=utf-8
import json
from calculator import calculators
import decider

print(decider.r)

test = u'{"target": {"lang": "en", "text": "Women in Tech: Put Your Money Where Your Mouth."}, "orig": {"lang": "ru", "text": "Женщины в Tech: положить ваши деньги, когда ваш рот."}}'
t = json.loads(test)

class Sentence:

    def __init__(self, lang, text):
        self.lang = lang
        self.text = text

class Param:

    def __init__(self, t_unit, calculator):
        self.name = calculator.name
        self.value = calculator.perform_calc(t_unit)

class Translation:

    def __init__(self,orig_sent, target_sent):
        self.original = Sentence(orig_sent['lang'],orig_sent['text'])
        self.target = Sentence(target_sent['lang'],target_sent['text'])
        self.params = []

    def add_param(self, param):
        self.params.append(param)

    def calc_all_params(self):
        for calc in calculators:
            self.add_param(Param(self,calc))



tu = Translation(t['orig'],t['target'])
tu.calc_all_params()
for p in tu.params:
    print u"%s  %s" % (p.name, p.value)