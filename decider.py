# coding=utf-8
import os, json

class Decider:
    def __init__(self):
        self.params = json.loads(file.read(open(os.path.join(os.path.dirname(__file__),'config.json'),'r')))

    def compare_with_conf(self,param):
    #Если нет максимального или минимального значения, то присваиваем бесконечность

        if self.params[param.name].has_key(u'min'):
            min_value = self.params[param.name]['min']
        else:
            min_value = float('-inf')

        if self.params[param.name].has_key(u'max'):
            max_value = self.params[param.name]['max']
        else:
            max_value = float('inf')


        if param.value >= min_value and param.value <= max_value:
            return u'non_vandal'
        else:
            return u'vandal'