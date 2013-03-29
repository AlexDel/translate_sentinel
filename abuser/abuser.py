# coding=utf-8
import re

rus_mats = {
    u".*ху(й|и|я|е|ли|ле).*",
    u".*пи(з|с)д.*",
    u"бля.*",
    u".*бля(д|т|ц).*",
    u"(с|сц)ук(а|о|и).*",
    u"еб.*",
    u".*уеб.*",
    u"заеб.*",
    u".*еб(а|и)(н|с|щ|ц).*",
    u".*ебу(ч|щ).*",
    u".*пид(о|е|а)р.*",
    u".*хер.*",
    u"г(а|о)ндон.*",
    u".*залуп.*",
    u"г(а|о)вн.*"
}

def prepare_text(tokens, lang):
    u'''
    эта функциия подготовляивает токены к последующему выявлению матов.
    например, ищет замену кириллических букв латинскими
    '''
    if lang == 'ru':
        replaces = [
            (u'a',u'а'),
            (u'x',u'х'),
            (u'o',u'о'),
        ]


        for i in range(len(tokens)):
            for r in replaces:
                tokens[i] = tokens[i].replace(r[0],r[1])

        return tokens
    else:
        return tokens

def collect_abuse_words(tokens, lang):
    u'''
    данная функция полкчает список токенов и язык и с помощью регулярных выражений ищет маты в них
    возвращает список матов
    '''

    abuse_words = []


    return abuse_words

