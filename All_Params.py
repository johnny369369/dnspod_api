#-*- coding: utf-8 -*-
import json,pickle,os,sys

class All_params(object):
    colour_list = {
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'purple_red': 35,
        'bluish_blue': 36,
        'white': 37,
    }

    def __init__(self):
        pass

    @staticmethod
    def display(msg, colour='white'):
        choice = All_params.colour_list.get(colour)
        if choice:
            info = "\033[1;{};1m{}\033[0m".format(choice, msg)
            return info
        else:
            return False

    @staticmethod
    def check_input(msg,result = []):
        def entry(msg):
            ret = input(u'请输入{},或输入q退出: '.format(msg)).strip()
            return ret
        choice = entry(msg)
        result.append(choice)
        if not choice:
           check_input(msg)
        else:
            if choice == 'q':
               sys.exit(0)
        return result[-1]

    @staticmethod
    def input_ck(data,title):
        try:
            user_input = ''
            while user_input.strip() not in data:
                for key_id in data:
                    print('\t',key_id,data[key_id])
                user_input = input(f'请选择{title},或输入q退出:').strip()
                if user_input == 'q':
                    sys.exit(1)
            return user_input.strip()
        except Exception as e:
            print(e)

    @staticmethod
    def load(token_file):
        with open(token_file,'rb') as f:
            while True:
              try:
                 file = pickle.load(f)
                 return file
              except Exception as e:
                  print(e)
                  return False

    @staticmethod
    def dump(token_file):
        with open(token_file,'ab') as f:
            try:
                pickle.dump(f)
                return True
            except Exception as e:
                print(e)
                return False
