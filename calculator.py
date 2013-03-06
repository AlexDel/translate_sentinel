# coding=utf-8

class Calculator:
    '''
    Calculators' base class
    '''

    def perform_calc(self, translation_unit):
        raise NotImplementedError


class String_target_length(Calculator):

    def __init__(self):
        self.name = u'String_target_length'

    def perform_calc(self, translation_unit):
       return len(translation_unit.target.text)


class Length_difference(Calculator):

    def __init__(self):
        self.name = u'Length_difference'

    def perform_calc(self, translation_unit):
        or_length = float(len(translation_unit.original.text))
        tar_length = float(len(translation_unit.target.text))


        return or_length/tar_length

class Digits_amount(Calculator):

    def __init__(self):
        self.name = u'Digits_amount'

    def _count_digits(self, string):
        return float(len([s for s in string if s.isdigit()]))

    def perform_calc(self, translation_unit):
        target = translation_unit.target.text
        return self._count_digits(target)/float((len(target)))




calculators = [String_target_length(), Length_difference()]
