# coding=utf-8
import json
from calculator import *
from decider import Decider


test = u'{"target": {"lang": "en", "text": "Women in Tech to put your money where your mouth is"}, "orig": {"lang": "ru", "text": "Женщины в Tech положить ваши деньги, когда ваш рот."}}'
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
        self.calc_all_params()

    def add_param(self, param):
        self.params.append(param)

    def calc_all_params(self):
        for calc in calculators:
            self.add_param(Param(self,calc))

    def is_vandal(self):
        for p in self.params:
            if Decider().compare_with_conf(p) == u'vandal':
                return True
                break
        return False

def process(t_unit):
    # эта функция отвечает за получение данных и обработку результата
    t_unit = json.loads(t_unit)
    is_vandal = Translation(t_unit).is_vandal()
    return json.dumps(is_vandal)



#test stuff
tu = Translation(t['orig'],t['target'])
for p in tu.params:
    print u'%s  %s' % (p.name, p.value)
print tu.is_vandal()
