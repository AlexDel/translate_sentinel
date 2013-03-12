# coding=utf-8
import re

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

class Digits_blocks_difference(Calculator):

    def __init__(self):
        self.name = u'Digits_blocks_intersection'

    def _collect_digit_blocks(self, string):
        reg_exp = r'(\d+)'
        return set(re.findall(reg_exp,string))

    def perform_calc(self, translation_unit):
        or__blocks = self._collect_digit_blocks(translation_unit.original.text)
        tar__blocks = self._collect_digit_blocks(translation_unit.target.text)

        return float(len(or__blocks ^ tar__blocks))/ (len(or__blocks) + 1)

calculators = [String_target_length(), Length_difference(), Digits_amount(),Digits_blocks_difference(),
]
