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

    def remove_stopwords(self, word_list, lang = 'en'):
        if lang == 'en':
            stopwords = set(nltk.corpus.stopwords.words('english'))
            return [word for word in word_list if word not in stopwords]
        else:
            return None

    def normalize_sentence(self, sentence, lang = 'en'):
        """
        эта функция выполняет разбиение на токены, удаление стоп-слова и стемминг
        """
        tokens = self.tokenize(sentence)
        r_tokens = self.remove_stopwords(tokens, lang)
        return [self.stem(token) for token in r_tokens ]

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
        return max([len(s) for s in  self._find_long_blocks(translation_unit.target.text)])

class Longest_word(Calculator):

    def __init__(self):
        self.name = 'Longest_word'

    def perform_calc(self, translation_unit):
        return max([len(w) for w in self.tokenize(translation_unit.target.text)])

class BLEU_metrics(Calculator):

    def __init__(self):
        self.name = 'BLEU_metrics'

    def perform_calc(self, translation_unit):
        or_text = translation_unit.original
        tar_text = translation_unit.target

        #если текст оригинала на английском, переводим вариант на английский и сравниваем
        if or_text == 'en':
            tar_text_translated = translator.Translator.translate(tar_text, tar_text.lang, or_text.lang)
            token_intersection =len(self.normalize_sentence(tar_text_translated) & set(self.normalize_sentence(or_text)))
            or_normalized_length = len(set(self.normalize_sentence(or_text)))

            return float(token_intersection)/or_normalized_length
        #иначе ничего не возращаем (что делать с другими парами будем позже)
        else:
            return None


calculators = [String_target_length(), Length_difference(), Digits_amount(),Digits_blocks_difference(),
Target_upper_case(), Longest_symbol_repetition(),Longest_word(), BLEU_metrics()]


