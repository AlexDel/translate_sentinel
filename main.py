# coding=utf-8
import json, logging
from calculator import *
from decider import Decider


test = u'{"orig": {"lang": "en", "text": "Are your foregrounds fighting for the users’ attention?"}, "target": {"lang": "ru", "text": "Объекты вашего переднего плана борются за внимание пользователей?"}}'
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


def debug(t_unit_raw):
    t_unit = json.loads(t_unit_raw)

    result = []
    tu  =  Translation(t_unit['orig'],t_unit['target'])

    result.append(tu.original.text)
    result.append(tu.target.text)
    result.append(str(tu.is_vandal()))
    for p in tu.params:
        result.append(u'%s  %s' % (p.name, p.value))

    #возвращаем список
    return result

def process(t_unit_raw, make_log = True):
    # эта функция отвечает за получение данных и обработку результата
    t_unit = json.loads(t_unit_raw)
    is_vandal = Translation(t_unit['orig'],t_unit['target']).is_vandal()

    #записываем данные в блог

    logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'trans_log.log')
    logging.debug(u'\n'.join(debug(t_unit_raw)))

    return json.dumps(is_vandal)

#test stuff
# tu = Translation(t['orig'],t['target'])
# for p in tu.params:
#     print u'%s  %s' % (p.name, p.value)
# print tu.is_vandal()
