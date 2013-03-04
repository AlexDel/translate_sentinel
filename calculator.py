# coding=utf-8
class Calculator:
    '''
    Calculators' base class
    '''

    def perform_calc(self, translation_unit):
        raise NotImplementedError



class String_target_length(Calculator):

    def __init__(self):
        self.name = 'String_target_length'

    def perform_calc(self, translation_unit):
       return len(translation_unit.target.text)

class String_original_length(Calculator):

    def __init__(self):
        self.name = 'String_original_length'

    def perform_calc(self, translation_unit):
        return len(translation_unit.original.text)



calculators = [String_original_length(),String_target_length()]
