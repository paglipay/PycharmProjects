import time
class CustomKeyObj:
    def __init__(self, int_name, data=None):
        print('__init_'+int_name)
        self.name = int_name
        self.bol = None
        self.data = None
        self.data_list = []
        self_data = {int_name: self.data_list}

        if data != None:
            self.data = data
            self.data.update(self_data)
        i = 0
        while True:
            if i > 4:
                break
            print('CustomKeyObj_while:'+int_name+' '+str(i))
            self.data_list.append(i)
            i += 1
            time.sleep(1)

    def k_func(self,str_config, v_val):
        bol_config = False
        if str_config == 'True':
            bol_config = True

        elif str_config == 'False':
            bol_config = False

        elif str_config == 'return':
            print('return')
            print(v_val)
            if v_val == 'True':
                b_val = True
            elif v_val == 'False':
                b_val = False
            print(b_val)
            self.bol = b_val
            bol_config = True
        else:
            bol_config = False
            #self.bol = bol_config

        return bol_config

    def v_func(self,str_config):
        if str_config == 'break':
            bol_config = False
            #self.bol = bol_config
        else:
            bol_config = True
            #self.bol = bol_config
        return bol_config

