# coding=utf-8
import re, nltk, translator

class Calculator:
    '''
    Calculators' base class
    '''

    def tokenize(self,string):
        tokenizer = nltk.tokenize.RegexpTokenizer('\s+', gaps=True)
        return tokenizer.tokenize(string)

    def stem(self,word, lang = 'en'):
        if lang == 'en':
            return nltk.stem.PorterStemmer().stem(word)

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

class Alnum_symbols_part(Calculator):

    def __init__(self):
        self.name = 'Alphanum_symbols_part'

    def _count_alnum(self,string):
        return len([s for s in string if s.isalnum()])

    def perform_calc(self, translation_unit):
        or_alnum = self._count_alnum(translation_unit.original.text)
        tar_alnum = self._count_alnum(translation_unit.target.text)
        return (float(or_alnum)+1)/(tar_alnum+1)

class Target_upper_case(Calculator):

    def __init__(self):
        self.name = 'Target_upper_case'

    def _count_uppercase(self,string):
        return len([s for s in string if s.isupper()])

    def perform_calc(self, translation_unit):
        or_uppercase = self._count_uppercase(translation_unit.original.text)
        tar_uppercase = self. _count_uppercase(translation_unit.target.text)
        return (float(or_uppercase)+1)/(tar_uppercase+1)

class Longest_symbol_repetition(Calculator):

    def __init__(self):
        self.name = 'Longest_symbol_repetition'

    def _find_long_blocks(self, string):
        '''Метод ищет кол-во символов длинее 3 символов'''
        return [match[0] for match in re.findall(r'((\w)\2{2,})', string)]

    def perform_calc(self, translation_unit):
        return max(self._find_long_blocks(translation_unit.target.text))

class Longest_word(Calculator):

    def __init__(self):
        self.name = 'Longest_word'

    def perform_calc(self, translation_unit):
        return max([len(w) for w in self.tokenize(translation_unit.target.text)])


calculators = [String_target_length(), Length_difference(), Digits_amount(),Digits_blocks_difference(),
Target_upper_case(), Longest_symbol_repetition(),Longest_word()]


