# coding=utf-8
import re, nltk, translator
from abuser import abuser
from nltk.corpus import wordnet as wn

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

    def normalize_sentence(self, sentence, lang = 'en',filter_stopwords = True):
        """
        эта функция выполняет разбиение на токены, удаление стоп-слова и стемминг
        """
        tokens = self.tokenize(sentence)
        if filter_stopwords == False:
            return [self.stem(token) for token in tokens ]
        else:
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
        long_bloks = self._find_long_blocks(translation_unit.target.text)
        if len(long_bloks)  > 0:
            return max([len(s) for s in long_bloks ])
        else:
            return 0

class Longest_word(Calculator):

    def __init__(self):
        self.name = 'Longest_word'

    def perform_calc(self, translation_unit):
        return max([len(w) for w in self.tokenize(translation_unit.target.text)])

class Calculator_with_translator(Calculator):
    '''
    расширение класса с использование машинного переводчика
    '''

    def translate(self, text, or_lang = 'ru', tar_lang = 'en'):
        return translator.Translator().translate(text, tar_lang, or_lang)

    def normalize_in_english(self, sentence):
        '''
        этот метод приводит предложение к набору лемм на английском языке
        '''
        if sentence.lang != 'en':
            return self.normalize_sentence(self.translate(sentence.text, sentence.lang, 'en'))
        else:
            return self.normalize_sentence(sentence.text)


class BLEU_metrics(Calculator_with_translator):

    def __init__(self):
        self.name = 'BLEU_metrics'

    def perform_calc(self, translation_unit):
        or_text = translation_unit.original
        tar_text = translation_unit.target

        #если текст оригинала на английском, переводим вариант на английский и сравниваем
        if or_text.lang == 'en':
            #переводим текст варианта на английский (оригинальный)
            tar_text_translated = self.translate(tar_text, tar_text.lang, or_text.lang)

            #считаем, сколько нормализованных токенов получилось
            token_intersection = len(self.normalize_sentence(tar_text_translated) & set(self.normalize_sentence(or_text)))

            #длина исходного предложения (в токенах)
            or_normalized_length = len(set(self.normalize_sentence(or_text)))

            return float(token_intersection)/or_normalized_length

        #иначе ничего не возращаем (что делать с другими парами будем позже думать)
        else:
            return None

class Bigram_calculator(Calculator_with_translator):

    def __init__(self):
        self.name = 'Bigram_calculator'

    def _make_bigrams(self, tokens):
        return nltk.util.bigrams(tokens)

    def perform_calc(self, translation_unit):
        or_text = translation_unit.original
        tar_text = translation_unit.target

        if or_text.lang == 'en':
            #переводим текст варианта на английский (оригинальный)
            tar_text_translated = self.translate(tar_text, tar_text.lang, or_text.lang)

            #превращаем текст в биграммы
            or_bigramms = self._make_bigrams(self.tokenize(or_text.text))
            tar_bigrams = self._make_bigrams(self.tokenize(tar_text_translated))

            #считаем пересечение биграм
            bigram_intersection = set(or_bigramms).intersection(set(tar_bigrams))

            return float(len(bigram_intersection))/(2*len(self.tokenize(tar_text_translated)))

        #иначе ничего не возращаем (что делать с другими парами будем позже думать)
        else:
            return None


class Binary_calculator(Calculator_with_translator):

    def retrieve_normalized_tokens(self, translation_unit):
        #этот метод возращает нормализованные токены оригинала и перевода

        or_text = translation_unit.original
        tar_text = translation_unit.target
        if or_text.lang == 'en':
            #переводим текст варианта на английский (оригинальный)
            tar_text_translated = self.translate(tar_text, tar_text.lang, or_text.lang)

            #нормализуем
            norm_or, norm_tar = (self.normalize_sentence(s) for s in (or_text,tar_text_translated))

            #возращаем нормализованные токены
            return norm_or, norm_tar

        #иначе ничего не возращаем (что делать с другими парами будем позже думать)
        else:

            return None, None


class Levenstein_calculator(Binary_calculator):

    def __init__(self):
        self.name = 'Levenstein_calculator'

    def _calc_levdistance(self, seq1,seq2):
        return nltk.metrics.distance.edit_distance(seq1, seq2, transposition = True)

    def perform_calc(self, translation_unit):
        norm_or, norm_tar = self.retrieve_normalized_tokens(translation_unit)

        if norm_or and norm_tar:
            #возращаем нормализованное расстояние Левенштейна
            return float(self._calc_levdistance(norm_or,norm_tar))/len(norm_or)

        #иначе ничего не возращаем (что делать с другими парами будем позже думать)
        else:
            return None

class Jaccard_distance(Binary_calculator):

    def __init__(self):
        self.name = 'Jaccard_distance'

    def perform_calc(self, translation_unit):
        norm_or, norm_tar = self.retrieve_normalized_tokens(translation_unit)

        if norm_or and norm_tar:
            #возращаем нормализованное расстояние Жаккара
            return float(nltk.metrics.jaccard_distance(set(norm_or),set(norm_tar)))

        #иначе ничего не возращаем (что делать с другими парами будем позже думать)
        else:
            return None

class Braun_Balke_calculator(Binary_calculator):

    def __init__(self):
        self.name = 'Braun_Balke_calculator'

    def perform_calc(self, translation_unit):
        norm_or, norm_tar = self.retrieve_normalized_tokens(translation_unit)

        if norm_or and norm_tar:
            return float(set(norm_or).intersection(set(norm_tar)))/max([len(s) for s in [norm_or,norm_tar]])

        #иначе ничего не возращаем (что делать с другими парами будем позже думать)
        else:
            return None

class Ochai_calculator(Binary_calculator):

    def __init__(self):
        self.name = 'Ochai_calculator'

    def perform_calc(self, translation_unit):
        norm_or, norm_tar = self.retrieve_normalized_tokens(translation_unit)

        if norm_or and norm_tar:
            return float(set(norm_or).intersection(set(norm_tar)))/(len(set(norm_tar)) * len(set(norm_or)))**0.5

        #иначе ничего не возращаем (что делать с другими парами будем позже думать)
        else:
            return None

class Simpson_calculator(Binary_calculator):

    def __init__(self):
        self.name = 'Simpson_calculator'

    def perform_calc(self, translation_unit):

        norm_or, norm_tar = self.retrieve_normalized_tokens(translation_unit)

        if norm_or and norm_tar:
            return float(set(norm_or).intersection(set(norm_tar)))/min([len(s) for s in [norm_or,norm_tar]])

        #иначе ничего не возращаем (что делать с другими парами будем позже думать)
        else:
            return None

class Profanity_calculator(Calculator):

    def __init__(self):
        self.name = 'Profanity_calculator'

    def perform_calc(self, translation_unit):
        profanity_num_or = len(abuser.collect_abuse_words(self.tokenize(translation_unit.original.text),translation_unit.original.lang))
        profanity_num_tar = len(abuser.collect_abuse_words(self.tokenize(translation_unit.target.text), translation_unit.target.lang))

        return float((1 + profanity_num_or))/(1 + profanity_num_tar)


class Semantic_calculator(Calculator_with_translator):

    def __init__(self):
        self.name = 'Semantic_calculator'

    def get_word_similarity(self, word_a, word_b):
        """
        find similarity between word senses of two words
        """
        wordasynsets = wn.synsets(word_a)
        wordbsynsets = wn.synsets(word_b)
        synsetnamea = [wn.synset(str(syns.name)) for syns in wordasynsets]
        synsetnameb = [wn.synset(str(syns.name)) for syns in wordbsynsets]

        sem_distance = []

        for sseta, ssetb in [(sseta,ssetb) for sseta in synsetnamea for ssetb in synsetnameb]:
            sem_distance.append(sseta.wup_similarity(ssetb))

        return max(sem_distance)

    def create_sent_vector(self, translation_unit):
        '''
        Этот метод создает вектор используемый для дальнейших вычислений
        '''
        t_var = [translation_unit.original, translation_unit.target]
        common_tokens = []

        #если язык варианта перевода - английский, то просто нормализуем предложение, иначе переводим машиной, а потом нормализуем
        for t in t_var:
            if t.lang != 'en':
                common_tokens.append(self.normalize_sentence(self.translate(t)))
            else:
                common_tokens.append(self.normalize_sentence(self.translate(t.text, t.lang, 'en')))

        #делаем собственно вектор
        sent_vector = {}

        for token in common_tokens:
            sent_vector[token] = 0

        return sent_vector

    def calc_vector(self,vector, tokens):
        '''
        Данный метод вычисляет значение вектора для данного предложения
        '''
        for t in tokens:
            for k in vector.keys():
                if k == t:
                    vector[k] = 1
                else:
                    vector[k] = self.get_word_similarity(k,t)

        return vector

    def perform_calc(self, translation_unit):
        original_tokens = self.normalize_sentence()
        target_tokens = ''

        vector = self.create_sent_vector(translation_unit)
        vector1 = self.calc_vector(vector, )

#список рабочих калькуляторов, используемых при оценке
calculators = [String_target_length(), Length_difference(), Digits_amount(),Digits_blocks_difference(),
Target_upper_case(), Longest_symbol_repetition(),Longest_word(), BLEU_metrics(), Bigram_calculator(),
Levenstein_calculator(), Braun_Balke_calculator(),Profanity_calculator()]



