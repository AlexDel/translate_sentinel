import json

class Exchanger(obj):
    'This method performs communication with langprism'

    def __init__(self, obj = None):
        ''' Initialize class by getting json form LangPrism'''
        self.requet = json.dump(obj)
