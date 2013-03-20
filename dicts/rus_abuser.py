# coding=utf-8
import re
abuse_words = [
u'[а-яА-я]{2,8}',
u'жопа']

print re.findall(abuse_words[0],u'сунь хуй в чай')[0]