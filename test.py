# coding=utf-8
import main, csv, json


def test():
    #берем тесты из csv-файла
    tests = []
    for row in csv.reader(open('test-set.csv'), delimiter=';'):
        tests.append(tuple([r.decode('utf8') for  r in row]))


    TP = 0
    TN = 0
    FP = 0
    FN = 0


    #try:
    for i, t in enumerate(tests[1565:]):
        # print i
        # print t[0]
        # print t[1]

        r = u'''{"orig": {"lang": "en", "text": "%s"}, "target": {"lang": "ru", "text": "%s"}}''' % (t[0].replace(u'"',u''),t[1].replace(u'"',u''))
        print i
        res = json.loads(main.process(r))
        if res != int(t[2]):
            print main.debug(r)
            print '\n'

        if res == 0 and  int(t[2]) == 0:
            TN += 1
        if res == 1 and int(t[2]) == 1:
            TP += 1
        if res == 1 and int(t[2]) == 0:
            FP += 1
        if res == 0 and  int(t[2]) == 1:
            FN += 1

    #except:
    print u'TP = %s ; TN = %s;  FP = %s, FN = %s' % (TP, TN, FP, FN)

test()
# o = 0
# for t in tests[1:]:
#     s1 = split_to_clauses(sentence = t[1], language='ru')
#     s2 = split_to_clauses(sentence = t[0], language='en')
#     if len(s2['clauses']) > 1:
#         print str(len(s2['clauses'])) + str(s2['clauses'])
#         for i,s in enumerate(s1['clauses']):
#             print i
#             print s.encode('utf8')
#         print '\n'
#         o += 1
#
# print o