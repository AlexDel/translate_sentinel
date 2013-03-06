# coding=utf-8
import os, json

class Decider:
    def __init__(self):
        self.params = json.loads(file.read(open(os.path.join(os.path.dirname(__file__),'config.json'),'r')))

    def compare_with_conf(self,param):

        min_value = self.params[param]['min']
        max_value = self.params[param]['max']

        #Если нет максимального или минимального значения, то присваиваем бесконечность
        if not min_value and min_value != 0:
            min_value = float('-inf')

        if not max_value and max_value != 0:
            max_value = float('inf')

        if param >= min_value and value <= max_value:
            return True
        else:
            return False