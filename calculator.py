# coding=utf-8
class Calculator:
    '''
    Calculators' base class
    '''
    def __init__(self, name):
        self.name = name

    def perform_calc(self, translation_unit):
        raise NotImplementedError



class String_length(Calculator):

    def __init__(self, t_unit):
        self.t_unit.target_length = len(t_unit.target.text)

