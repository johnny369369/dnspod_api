#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-
import os,sys
from All_Params import All_params
from T_dnsPod import Procedure
from Mylogger import *

def get_token(token_file):
    pro_name = {'1': 'b79_pro', '2': 'b79_mkt', '3': 'e03_pro', '4': 'e04_pro','5':'u06_pro'}
    name_check = All_params.input_ck(pro_name,u'产品序号')
    product = pro_name[name_check]
    load_file = All_params.load(token_file)
    pro_token_dict = dict(load_file)
    Login_Token = pro_token_dict[product]
    try:
        oper_dict = {'1':'批量添加域名和记录',
                     '2':'删除域名',
                     '3':'添加域名解析记录',
                     '4':'修改域名解析记录',
                     '5':'删除域名解析记录',
                     '6':'获取域名列表',
                     '7':'获取域名解析记录',
                     '8':'添加域名',
                     '9':'查询域名日志',
                    '10':'批量修改域名记录',
                    '11':'获取D监控报警信息',
                    '12':'获取监控列表'}
        operation_id = All_params.input_ck(oper_dict,'你的操作')
        fun_dict = {'1':'running.Add_Domain_And_Record()',
                    '2':'running.Del_Domain()',
                    '3':'running.Add_Record()',
                    '4':'running.Alter_Record()',
                    '5':'running.Del_Record()',
                    '6':'running.Get_Domain_List()',
                    '7':'running.Get_Domain_Record_Info()',
                    '8':'running.Add_Domain()',
                    '9':'running.Get_Domain_Log()',
                   '10':'running.Batch_Alter_Domain_Record()',
                   '11':'running.Get_product_monit()',
                   '12':'running.Get_D_list()'}
        running = Procedure(Login_Token, product)
        exec(fun_dict[operation_id])
    except (KeyError):
        print(All_params.display(u'\t\t输入的数字不在字典内', 'red'))
        mylogger.error(u'输入的数字不在字典内')

if __name__ == '__main__':
   if len(sys.argv) < 2:
      print('\t',All_params.display('token_file需要pickle.dump序列化才能读取'))
      print('\t',All_params.display(u'使用方法:python Main.py token_file','red'))
      sys.exit(0)
   else:
      get_token(sys.argv[1])
