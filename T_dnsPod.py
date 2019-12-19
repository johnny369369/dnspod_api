#-*- coding: utf-8 -*-

import sys,os
from T_dnsApi import *
from Mylogger import *
from All_Params import All_params


class Procedure(Global_Var):

    def Add_Domain_And_Record(self):
        Domains_List = []
        with open('domain_list', 'r+',encoding='utf-8') as domains:
            for d in domains.readlines():
                Domains_List.append(d.strip())

        running = Dns_Add_Domain_Record(self.Login_Token,self.Product)
        running.Add_Domain(Domains_List)
        running.Add_Record(Domains_List)

    def Del_Domain(self):
        '''删除域名'''
        Domains = All_params.check_input("您需要删除的域名，用逗号分隔：")
        Domains_List = Domains.split(sep=',')
        running = Dns_Del_Domain(self.Login_Token,self.Product)
        running.Del_Domain(Domains_List)

    def Add_Record(self):
        '''添加解析记录'''
        Domains = All_params.check_input("您需要添加解析记录的域名，多个域名用逗号分隔：")
        Sub_Domians = All_params.check_input("需要添加的子域名，用逗号分隔：")
        Domains_List = Domains.split(sep=',')
        running = Dns_Add_Record(self.Login_Token,self.Product)
        Record_Type = All_params.check_input("选择记录类型，输入（   A  或  CNAME ）:")
        Value = All_params.check_input("要解析的记录值:")
        Record_Line = All_params.check_input("输入记录线路:输入null为默认:")
        if Record_Line == 'null':
            Record_Line_value = '默认'
        else:
            Record_Line_value = Record_Line
        Sub_Domian_List = Sub_Domians.split(sep=',')
        running.Add_Record(Domains_List,Sub_Domian_List,Record_Type,Record_Line_value,Value)

    def Alter_Record(self):
        '''修改记录'''
        Domains = All_params.check_input("您需要修改解析记录的域名，以便获取其子域名的记录ID，多个记录(只能单个域名修改)用逗号分隔:")
        Domains_List = Domains.split(sep=',')
        running = Dns_Alter_Record(self.Login_Token,self.Product)
        running.Get_Record(Domains_List)
        Records = All_params.check_input("需要修改的解析记录的ID，并且输入ID，用逗号分隔:")
        Records_List = Records.split(sep=',')
        Change = All_params.check_input("您要修改的字段([sub_domain,record_type,area,value,mx,ttl,status]):")
        Change_TO = All_params.check_input("你要修改的字段例如:record_type= A CNAME MX TTL,sub_domain= @ www test|这个值对应是你上一步选择的字段| 要修改为:")
        if Change == 'value':
            running.Alter_Record(Records_List, Change,Change_TO,Value='')
        else:
            Value = All_params.check_input("要修改到的记录值:")
            running.Alter_Record(Records_List,Change,Change_TO,Value)

    def Del_Record(self):
        '''删除记录'''
        Domains = All_params.check_input("您需要删除解析记录的域名，以便获取其子域名的记录ID，用逗号分隔：")
        Domains_List = Domains.split(sep=',')
        running = Dns_Del_Record(self.Login_Token,self.Product)
        running.Get_Record(Domains_List)
        Records = All_params.check_input("需要删除的 域名ID 和 解析记录ID,多个记录已逗号分隔(格式，agvip2003.com=384855336)：")
        Domains_Records_List = Records.split(sep=',')
        running.Del_Record(Domains_Records_List)

    def Get_Domain_List(self):
        '''获取域名列表'''
        running =  Dns_Get_Domain_List(self.Login_Token,self.Product)
        running.Get_Domain_List()

    def Get_Domain_Record_Info(self):
        '''获取域名解析记录'''
        Domains = All_params.check_input("您需要查看记录的域名，以便获取其子域名的记录ID，多个域名用逗号分隔：")
        Domains_List = Domains.split(sep=',')
        running = Dns_Get_Domain_Record_Info(self.Login_Token,self.Product)
        running.Get_Domain_Record_Info(Domains_List)

    def Add_Domain(self):
        '''添加域名'''
        Domains = input("请输入您要添加的域名，用逗号分隔:")
        Sub_Domians = input("请输入需要添加的子域名，用逗号分隔（不添加则回车）：")
        Domains_List = Domains.split(sep=',')
        running = Dns_Add_Domain(self.Login_Token,self.Product)
        if Sub_Domians == '':
            running.Add_Domain(Domains_List)

    def Get_Domain_Log(self):
        '''查询域名日志'''
        Domains = All_params.check_input(u'输入查询日志的域名，用逗号分隔:')
        Domains_List = Domains.split(sep=',')
        running = Dns_Get_Domain_Log(self.Login_Token,self.Product)
        running.Get_Domain_Log_Info(Domains_List)

    def Batch_Alter_Domain_Record(self):
        '''批量修改记录'''
        with open('domain_list', 'r+',encoding='utf-8') as domains:
            for domainlist in domains.readlines():
                running = Dns_Alter_Domin_Record(self.Login_Token,self.Product)
                record_info = running.Record_Info(domainlist)
                #value_dict = eval('self.{}'.format(self.Product))
                Change = "value"
                try:
                   for record in record_info:
                       if record['type'] == 'CNAME' and record['name'] == 'www':
                          Records = record['id']
                          Change_TO = 'mktxty.mktcname.com'
                          running.Batch_Alter_Record(Records,Change,Change_TO,Value='')
                       if record['type'] == 'CNAME' and record['name'] == '@':
                          Records = record['id']
                          Change_TO = 'mktxty.mktcname.com'
                          running.Batch_Alter_Record(Records,Change,Change_TO,Value='')
                       if record['type'] == 'CNAME' and record['name'] == 'm':
                          Records = record['id']
                          Change_TO = 'b79_mobile.mktcname.com'
                          running.Batch_Alter_Record(Records,Change,Change_TO,Value='')
                       if record['type'] == 'CNAME' and record['name'] == 'vip':
                          Records = record['id']
                          Change_TO = 'b79_vipweb.mktcname.com'
                          running.Batch_Alter_Record(Records,Change,Change_TO,Value='')
                       if record['type'] == 'CNAME' and record['name'] == 'vipm':
                          Records = record['id']
                          Change_TO = 'b79_vipweb.mktcname.com'
                          running.Batch_Alter_Record(Records,Change,Change_TO,Value='')
                except Exception as e:
                    print(e)
                finally:
                    exit(0)

    def Get_product_monit(self):
        '''获取D监控报警'''
        running = Dns_Get_D_Monit(self.Login_Token,self.Product)
        running.D_Monit_Info()
    def Get_D_list(self):
        '''获取监控列表'''
        running = Dns_Get_monit_list(self.Login_Token,self.Product)
        running.Monit_list()
