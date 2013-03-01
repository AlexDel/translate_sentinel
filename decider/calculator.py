class Calculator:

    def __init__(self, t_unit = object):
        self.t_unit = t_unit
    pass

    def perform_calc(self, calc_name):
        pass

    def _param_assign(self):
        pass



class String_length(Calculator):

    def __init__(self, t_unit):
        self.t_unit.target_length = len(t_unit.target.text)

