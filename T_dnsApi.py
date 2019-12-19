# -*- coding: utf-8 -*-

import requests
from Mylogger import *
from All_Params import All_params

class Global_Var:
    '''通用变量'''
    def __init__(self,Login_Token,product):
        self.Product = product
        self.Login_Token = Login_Token
        self.Format = 'json'
        self.offset = '0'
        self.length = '50'
        self.Batch_Add_Domain_URL = 'https://dnsapi.cn/Batch.Record.Create'  #批量添加域名
        self.Batch_Add_Record_URL = 'https://dnsapi.cn/Batch.Record.Create'  #批量添加记录
        self.Alter_Record_URL = 'https://dnsapi.cn/Batch.Record.Modify'     #批量修改记录
        self.Add_Domain_URL = 'https://dnsapi.cn/Domain.Create'             #添加域名
        self.Add_Record_URL = 'https://dnsapi.cn/Record.Create'             #添加记录
        #self.Alter_Record_URL = 'https://dnsapi.cn/Record.Modify'          #修改记录
        self.Get_Record_URL = 'https://dnsapi.cn/Record.List'              #获取记录列表
        self.Del_Domain_URL = 'https://dnsapi.cn/Domain.Remove'            #删除域名
        self.Del_Record_URL = 'https://dnsapi.cn/Record.Remove'            #删除记录
        self.Get_Domain_List_URL = 'https://dnsapi.cn/Domain.List'         #获取域名列表
        self.Get_Domain_Log_URL = 'https://dnsapi.cn/Domain.Log'           #获取域名日志
        self.Get_monit_info = 'https://dnsapi.cn/Monitor.Getdowns'         #查看D监控报警
        self.Get_monit_list = 'https://dnsapi.cn/Monitor.List'             #获取监控列表

        self.b79_mkt = {'@':'yyweb.mktcname.com',
                        'www':'yyweb.mktcname.com',
                        'm':'b79_mobile.mktcname.com',
                        '999':'b79gi.cdnp4.com',
                        'vip':'b79_vipweb.mktcname.com',
                        'vipm':'b79_vipmobile.mktcname.com'}
        self.b79_pro = {'@':'218.253.216.145',
                        'www':'218.253.216.145',
                        'm':'b79_mobile.cdnspod.com.',
                        '999':'b79gi.cdnspod.com.',
                        'vip':'b79_vipweb.cdnspod.com',
                        'vipm':'b79_vipmobile.cdnspod.com'}
        self.e03_pro = {'@':'e03web.cdnv7.com',
                        'www':'e03web.cdnv7.com',
                        '999':'e03gi.cdnp4.com',
                        'm':'e03_mobile.cdnv7.com'}
        self.e04_pro = {'@':'e04web.cdnv8.com',
                        'www':'e04web.cdnv8.com',
                        '999':'e04gi.cdnp4.com',
                        'm':'e04_mobile.cdnv8.com'}
        self.u06_pro = {'@':'6upweb.6upcname.com.', 
                        'www':'6upweb.6upcname.com.'}

class Dns_Add_Domain_Record(Global_Var):
    '''添加域名或解析'''
    def Add_Domain(self,Domains_List):
        '''添加域名'''
        for Domain in Domains_List:
            r = requests.post(self.Add_Domain_URL, data={'login_token': self.Login_Token,
                                                         'format': self.Format,
                                                         'domain': Domain,
                                                         })
            response_record_json = r.json()
            if response_record_json["status"]["code"] == "1":
                print('域名：{:15}添加成功；域名ID：{:15}'.format(response_record_json["domain"]["domain"], response_record_json["domain"]["id"]))
                mylogger.info('本次操作人：--- ；域名：{} 添加成功；域名ID：{}'.format(response_record_json["domain"]["domain"], response_record_json["domain"]["id"]))

            else:
                print('域名：{:15}添加失败,错误信息：{:15}'.format(Domain, response_record_json["status"]["message"]))
                mylogger.error('本次操作人：--- ；域名：{} 添加失败,错误信息：{}'.format(Domain, response_record_json["status"]["message"]))


    def Add_Record(self,Domains_List):
        '''添加解析'''
        Record_Type = 'CNAME'
        Record_Line = '默认'
        Domain_Status = 'enable'
        if not self.Product:
            print(All_params.display('产品号为空，请检查','red'))
            mylogger.error('产品号为空，请检查')
        elif self.Product:
           for Domain in Domains_List:
               for Sub_Domain in eval('self.{}'.format(self.Product)):
                   Value = eval("self.{}['{}']".format(self.Product,Sub_Domain))
                   r = requests.post(self.Add_Record_URL, data={'login_token': self.Login_Token,
                                                                 'format': self.Format,
                                                                 'domain': Domain,
                                                                 'sub_domain': Sub_Domain,
                                                                 'record_type': Record_Type,
                                                                 'record_line': Record_Line,
                                                                 'value': Value,
                                                                 'status': Domain_Status
                                                                 })
                   response_record_json = r.json()
                   if response_record_json["status"]["code"] == "1":
                      print('域名：{:15}添加记录：{:15}成功'.format(Domain, response_record_json["record"]["name"]))
                      mylogger.info('本次操作人：--- ；域名：{} 添加记录 {} 成功'.format(Domain, response_record_json["record"]["name"]))
                   else:
                      print('域名：{:15}添加记录：{:15}失败，错误信息：{:15}'.format(Domain, Sub_Domain,response_record_json["status"]["message"]))
                      mylogger.error('本次操作人：--- ；域名：{} 添加失败,错误信息：{}'.format(Domain, response_record_json["status"]["message"]))
        else:
            print(All_params.display('产品号{}错误','red'.format(self.Product)))
            mylogger.error('产品号{}错误'.format(self.Product))

class Dns_Del_Domain(Global_Var):
    '''删除域名'''
    def Del_Domain(self,Domains_List):
        '''删除域名'''
        for Domain in Domains_List:
            r = requests.post(self.Del_Domain_URL,data={'login_token':self.Login_Token,
                                                        'format':self.Format,
                                                        'domain':Domain,
                                                        })
            resoponse_record_json = r.json()
            if resoponse_record_json["status"]["code"] == "1":
                print("删除域名：{:15}成功".format(Domain))
                mylogger.info('本次操作人：--- ；删除域名：{} 成功'.format(Domain))

            else:
                print("删除域名：{:15}失败,错误信息：{:15}".format(Domain,resoponse_record_json["status"]["message"]))
                mylogger.error('本次操作人：--- ；域名：{} 状态 {} 失败'.format(Domain,resoponse_record_json["status"]["message"]))

class Dns_Add_Record(Global_Var):
    '''添加解析记录'''
    def Add_Record(self,Domains_List,Sub_Domian_List,Record_Type,Record_Line_value,Value):
        '''添加域名和解析记录'''
        for Domain in Domains_List:
            for Sub_Domian in Sub_Domian_List:
                r = requests.post(self.Add_Record_URL, data={'login_token': self.Login_Token,
                                                        'format': self.Format,
                                                        'domain': Domain,
                                                        'sub_domain': Sub_Domian,
                                                        'record_type': Record_Type,
                                                        'record_line': Record_Line_value,
                                                        'value': Value,
                                                        })
                resoponse_record_json = r.json()
                if resoponse_record_json["status"]["code"] == "1":
                    print("域名:{:15} 添加子域名:{:15}记录成功:{:15}".format(Domain,resoponse_record_json["record"]["name"],Value))
                    mylogger.info('本次操作人：--- ；域名：{} 添加子域名: {} 记录成功:'.format(Domain,resoponse_record_json["record"]["name"],Value))
                else:
                    print("域名:{:15}添加:{:15}记录失败,错误信息：{}".format(Domain,Sub_Domian,resoponse_record_json["status"]["message"]))
                    mylogger.error('本次操作人：--- ；域名：{} 添加: {} 记录失败:'.format(Domain,Sub_Domian,resoponse_record_json["status"]["message"]))

class Dns_Alter_Record(Global_Var):
    '''修改解析记录'''
    def Get_Record(self,Domains_List):
        '''获取记录ID'''
        for Domian in Domains_List:
            r = requests.post(self.Get_Record_URL,data={'login_token':self.Login_Token,
                                                        'format':self.Format,
                                                        'domain':Domian,
                                                        'offset': self.offset,
                                                        'length': self.length
                                                        })

            resoponse_record_json = r.json()
            if resoponse_record_json['status']['code'] == '1':
                print('域名:{:15}共有:{:15}个子域名和:{:15}条解析记录.'.format(resoponse_record_json['domain']['name'],resoponse_record_json['info']['sub_domains'],resoponse_record_json['info']['record_total']))
                mylogger.info('本次操作人：--- 域名: {} 共有: {}个子域名和： {} 条解析记录.'.format(resoponse_record_json['domain']['name'],resoponse_record_json['info']['sub_domains'],resoponse_record_json['info']['record_total']))

                print("\t 结果如下：")
                mylogger.info('\t 结果如下：')
                for record in resoponse_record_json['records']:
                    Record_Type = record['type']
                    Record_Name = record['name']
                    Record_Value = record['value']
                    Record_ID = record['id']
                    print('记录类型：{:15}子域名：{:15}记录值：{:15}记录ID：{:15}'.format(Record_Type,Record_Name,Record_Value,Record_ID))
                    mylogger.info('本次操作人：--- 记录类型: {} 子域名: {} 记录值: {} 记录ID：{} '.format(Record_Type,Record_Name,Record_Value,Record_ID))


    def Alter_Record(self,Records_List,Change,Change_TO,Value):
        '''修改解析记录'''
        if Value == '':
            for Record in Records_List:
                r = requests.post(self.Alter_Record_URL,data={'login_token': self.Login_Token,
                                                               'format': self.Format,
                                                               'record_id': Record,
                                                               'change': Change,
                                                               'change_to': Change_TO
                                                               })
                resoponse_record_json = r.json()
                if resoponse_record_json['status']['code'] == '1':
                    print('域名:{:15}修改字段:{:15}成功:{:15}'.format(resoponse_record_json['detail'][0]['domain'],Change,Change_TO))
                    mylogger.info('本次操作人：--- 域名:{} 修改字段:{}为{}\t成功'.format(resoponse_record_json['detail'][0]['domain'],Change,Change_TO))

                else:
                    print('记录ID:{:15}修改字段:{:15}为:{:15}失败,错误信息：{:15}'.format(Record,Change,Change_TO,resoponse_record_json['status']['message']))
                    mylogger.error('本次操作人：--- 记录ID: {} 修改字段：{}为:{}失败,错误信息：{}'.format(Record,Change,Change_TO,resoponse_record_json['status']['message']))
        else:
            for Record in Records_List:
                r = requests.post(self.Alter_Record_URL,data={'login_token':self.Login_Token,
                                                              'format':self.Format,
                                                              'record_id':Record,
                                                              'change':Change,
                                                              'change_to':Change_TO,
                                                              'value':Value
                                                              })
                resoponse_record_json = r.json()
                if resoponse_record_json['status']['code'] == '1':
                    print('域名:{:15}将字段:{:15}修改为:{:15}字段,值为:{:15}'.format(resoponse_record_json['detail'][0]['domain'],Change,Change_TO,Value))
                    mylogger.info('本次操作人：--- 域名: {} 将字段修改为{} 值为：{}\t成功'.format(resoponse_record_json['detail'][0]['domain'],Change,Change_TO,Value))
                else:
                    print('记录ID:{:15}将字段:{:15}修改为:{:15}值为:{:15}失败--错误信息：{:15}'.format(Record,Change,Change_TO,Value,resoponse_record_json['status']['message']))
                    mylogger.error('本次操作人：--- 记录ID: {} 将字段：{}修改为:\t失败,错误信息：{}'.format(Record,Change,Change_TO,Value,resoponse_record_json['status']['message']))

class Dns_Del_Record(Global_Var):
    '''删除解析记录'''
    def Get_Record(self,Domains_List):
        '''获取记录ID'''
        for Domian in Domains_List:
            r = requests.post(self.Get_Record_URL,data={'login_token':self.Login_Token,
                                                        'format':self.Format,
                                                        'domain':Domian,
                                                        'offset':self.offset,
                                                        'length':self.length,
                                                        })

            resoponse_record_json = r.json()
            if resoponse_record_json['status']['code'] == '1':
                print('域名:{:15}共有:{:15}个子域名和:{:15}条解析记录.'.format(resoponse_record_json['domain']['name'],resoponse_record_json['info']['sub_domains'],resoponse_record_json['info']['record_total']))
                mylogger.info('本次操作人：--- 域名：{} \t共有：{}个子域名和：{}条解析记录.'.format(resoponse_record_json['domain']['name'],resoponse_record_json['info']['sub_domains'],resoponse_record_json['info']['record_total']))

                print("\t 结果如下：")
                mylogger.info('\t 结果如下：')
                for record in resoponse_record_json['records']:
                    Record_Type = record['type']
                    Record_Name = record['name']
                    Record_Value = record['value']
                    Record_ID = record['id']
                    print('记录类型:{:15}子域名:{:15}记录值:{:15}记录ID:{:15} '.format(Record_Type,Record_Name,Record_Value,Record_ID))
                    mylogger.info('本次操作人：--- 记录类型: {} 子域名: {} 记录值: {} 记录ID：{} '.format(Record_Type,Record_Name,Record_Value,Record_ID))

    def Del_Record(self,Domains_Records_List):
        '''删除解析记录'''
        for Domain_Record in Domains_Records_List:
            Domain = Domain_Record.split(sep='=')[0]
            Record = Domain_Record.split(sep='=')[1]
            r = requests.post(self.Del_Record_URL,data={'login_token':self.Login_Token,
                                                        'format':self.Format,
                                                        'domain':Domain,
                                                        'record_id':Record,
                                                        })
            resoponse_record_json = r.json()
            if resoponse_record_json['status']['code'] == '1':
                print('您正在删除域名：{:15}的解析记录,记录ID为：{:15}删除状态值为：{:15}信息为：{:15}'.format(Domain,Record,resoponse_record_json['status']['code'],resoponse_record_json['status']['message']))
                mylogger.info('本次操作人：--- 您正在删除域名：{}的解析记录,\t记录ID为:{}\t删除状态值为:{}\t信息为:{}'.format(Domain,Record,resoponse_record_json['status']['message'],resoponse_record_json['status']['message']))
            else:
                print('您正在删除域名：{:15}的解析记录,记录ID为:{:15}删除状态值为:{:15}信息为:{:15}'.format(Domain,Record,resoponse_record_json['status']['message'],resoponse_record_json['status']['message']))
                mylogger.error('本次操作人：--- 您正在删除域名：{}的解析记录,\t记录ID为:{}\t 删除状态值为:{}\t信息为:{}'.format(Domain,Record,resoponse_record_json['status']['message'],resoponse_record_json['status']['message']))

class Dns_Get_Domain_List(Global_Var):
    '''获取域名列表'''
    def Get_Domain_List(self):
        '''获取域名列表'''
        r = requests.post(self.Get_Domain_List_URL,data={'login_token':self.Login_Token,
                                                         'format':self.Format})
        resoponse_record_json = r.json()
        Get_Message = "域名获取状态为：" + str(resoponse_record_json['status']['code']) +\
                      "，共有 " + str(resoponse_record_json['info']['domain_total']) + \
                      "个域名。"
        print(Get_Message)
        for Domains_List in resoponse_record_json['domains']:
            Domain_Id = Domains_List['id']
            Domain_Status = Domains_List['status']
            Domain_Status_DICT = {"enable": "正常", "pause": "已暂停解析", "spam": "已被封禁", "lock": "已被锁定"}
            Domain = Domains_List['name']
            Domain_Records_Num = Domains_List['records']
            if Domain_Status == 'enable':
                print('域名：{:20}域名ID:{:10} 域名状态:{:15}域名解析记录共:{:5}条,'.format(Domain,Domain_Id,Domain_Status_DICT[Domain_Status],Domain_Records_Num))
                mylogger.info('本次操作人：--- 域名：{}\t域名ID:{}\t域名状态:{}\t域名解析记录共:{}条,'.format(Domain,Domain_Id,Domain_Status_DICT[Domain_Status],Domain_Records_Num))

            else:
                print('域名：{:20}域名ID:{:10} 域名状态:{:15}域名解析记录共:{:5}条,'.format(Domain,Domain_Id,Domain_Status_DICT[Domain_Status],Domain_Records_Num))
                mylogger.info('本次操作人：--- 域名：{}\t域名ID:{}\t域名状态:{}\t域名解析记录共:{}条,'.format(Domain,Domain_Id,Domain_Status_DICT[Domain_Status],Domain_Records_Num))

class Dns_Get_Domain_Record_Info(Global_Var):
    '''查看域名记录'''
    def Get_Domain_Record_Info(self,Domains_List):
        '''查看域名记录'''
        for Domain in Domains_List:
            r = requests.post(self.Get_Record_URL,data={'login_token':self.Login_Token,
                                                        'format':self.Format,
                                                        'domain':Domain,
                                                        'offset':self.offset,
                                                        'length':self.length,
                                                        })

            resoponse_record_json = r.json()
            if resoponse_record_json['status']['code'] == '1':
                print("域名:" + resoponse_record_json['domain']['name'],
                      "共有:" + resoponse_record_json['info']['sub_domains'],
                      "个子域名和:" + resoponse_record_json['info']['record_total'],
                      "条解析记录.")
                mylogger.info('本次操作人：--- 域名: {} 共有: {}子域名和: {} 解析 '.format(resoponse_record_json['domain']['name'],
                      resoponse_record_json['info']['sub_domains'],
                      resoponse_record_json['info']['record_total']))

                mylogger.info("结果如下：")
                for record in resoponse_record_json['records']:
                    Record_Type = record['type']
                    Record_Name = record['name']
                    Record_Value = record['value']
                    Record_ID = record['id']
                    print("记录类型:" + Record_Type, "子域名:" + Record_Name,"记录值:" + Record_Value, "记录ID:" + Record_ID)
                    mylogger.info('本次操作人：--- 记录类型:{} 子域名:{} 记录值:{} 记录ID:{} '.format(Record_Type,Record_Name,Record_Value,Record_ID))
            else:
                print(All_params.display(u'域名不在账户中','red'))
                mylogger.error('域名:{}不在账户中'.format(Domain))

class Dns_Add_Domain(Global_Var):
     '''添加域名'''
     def Add_Domain(self, Domains_List):
         '''添加域名'''
         for Domain in Domains_List:
             r = requests.post(self.Add_Domain_URL, data={'login_token': self.Login_Token,
                                                          'format': self.Format,
                                                          'domain': Domain,
                                                          })
             response_record_json = r.json()
             if response_record_json["status"]["code"] == "1":
                 print('域名：{}\t添加成功；域名ID：{:15}'.format(response_record_json["domain"]["domain"],
                                                    response_record_json["domain"]["id"]))
                 mylogger.info('本次操作人：--- ；域名：{} 添加成功；域名ID：{}'.format(response_record_json["domain"]["domain"],
                                                                      response_record_json["domain"]["id"]))
             else:
                 print('域名：{}\t添加失败,错误信息：{:15}\t'.format(Domain, response_record_json["status"]["message"]))
                 mylogger.error('本次操作人：--- ；域名：{} 添加失败,错误信息：{}'.format(Domain, response_record_json["status"]["message"]))

class Dns_Get_Domain_Log(Global_Var):
    '''查询域名日志'''
    def Get_Domain_Log_Info(self,Domains_List):
        for Domain in Domains_List:
            r = requests.post(self.Get_Domain_Log_URL,data={'login_token': self.Login_Token,
                                                         'format': self.Format,
                                                         'domain': Domain,
                                                         'offset': self.offset,
                                                         'length': self.length,
                                                         })
            response_record_json = r.json()
            if response_record_json['status']['code'] == '1':
                for domain_log in response_record_json['log']:
                    print(domain_log)
                    mylogger.info(domain_log)
            else:
                print('域名:{}查询失败,error_info:{}'.format(Domain,response_record_json['status']['message']))
                mylogger.error('域名:{}查询失败,error_info:{}'.format(Domain,response_record_json['status']['message']))

class Dns_Alter_Domin_Record(Global_Var):
    '''批量修改域名记录'''
    def Record_Info(self,domain):
        '''查看域名记录'''
        r = requests.post(self.Get_Record_URL,data={'login_token':self.Login_Token,
                                                    'format':self.Format,
                                                    'domain':domain,
                                                    'offset':self.offset,
                                                    'length':self.length,
                                                    })

        resoponse_record_json = r.json()
        if resoponse_record_json['status']['code'] == '1':
           return resoponse_record_json['records'] 
        else:
            print(All_params.display('域名:{}不在账户中','red'.format(domain)))
            mylogger.error('域名:{}不在账户中'.format(domain))
    def Batch_Alter_Record(self,Records,Change,Change_TO,Value):
        '''修改解析记录'''
        if not Value:
           r = requests.post(self.Alter_Record_URL,data={'login_token': self.Login_Token,
                                                          'format': self.Format,
                                                          'record_id': Records,
                                                          'change': Change,
                                                          'change_to': Change_TO
                                                          })
           resoponse_record_json = r.json()
           if resoponse_record_json['status']['code'] == '1':
               print('域名:{:15}修改字段:{:15}成功:{:15}'.format(resoponse_record_json['detail'][0]['domain'],Change,Change_TO))
               mylogger.info('本次操作人：--- 域名:{} 修改字段:{}为{}\t成功'.format(resoponse_record_json['detail'][0]['domain'],Change,Change_TO))

           else:
               print('记录ID:{:15}修改字段:{:15}为:{:15}失败,错误信息：{:15}'.format(Records,Change,Change_TO,resoponse_record_json['status']['message']))
               mylogger.error('本次操作人：--- 记录ID: {} 修改字段：{}为:{}失败,错误信息：{}'.format(Records,Change,Change_TO,resoponse_record_json['status']['message']))

class Dns_Get_D_Monit(Global_Var):
    '''获取D监控报警'''
    def D_Monit_Info(self):
        try:
           r = requests.post(self.Get_monit_info,data={'login_token': self.Login_Token,'format': self.Format,'offset':'0','length':'20'})
           resoponse_record_json = r.json()
           if resoponse_record_json['status']['code'] == '1':
              for D_info in resoponse_record_json['monitor_downs']:
                  print('主机:{}   线路:{}   IP:{}   告警信息为:{}   记录时间:{}'.format(D_info['host'],D_info['record_line'],D_info['ip'],D_info['warn_reason'],D_info['switch_log']))
                  mylogger.info('主机:{}线路:{}IP:{}告警信息为:{}记录时间:{}'.format(D_info['host'],D_info['record_line'],D_info['ip'],D_info['warn_reason'],D_info['switch_log']))
        except Exception as e:
             print(e)

class Dns_Get_monit_list(Global_Var):
      '''获取监控列表'''
      def Monit_list(self):
          try:
             r = requests.post(self.Get_monit_list,data={'login_token':self.Login_Token,'format': self.Format}) 
             resoponse_record_json = r.json()
             if resoponse_record_json['status']['code'] == '1':
                for monit_list in resoponse_record_json['monitors']:
                    print('域名:{}  子域名:{}  线路:{}  IP:{}  主机:{}  端口:{}  监听类型:{}  超时时间:{}  监控是否开启:{}  状态:{}'.format(monit_list['domain'],monit_list['sub_domain'],
                         monit_list['record_line'],monit_list['ip'],monit_list['host'],monit_list['port'],
                         monit_list['monitor_type'],monit_list['monitor_interval'],monit_list['monitor_status'],monit_list['status']))
                    mylogger.info('域名:{}  子域名:{}  线路:{}  IP:{}  主机:{}  端口:{}  监听类型:{}  超时时间:{}  监控是否开启:{}  状态:{}'.format(monit_list['domain'],monit_list['sub_domain'],
                         monit_list['record_line'],monit_list['ip'],monit_list['host'],monit_list['port'],
                         monit_list['monitor_type'],monit_list['monitor_interval'],monit_list['monitor_status'],monit_list['status']))
          except Exception as e:
               print(e)
