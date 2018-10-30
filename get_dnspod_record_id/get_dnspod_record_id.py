#!/usr/bin/env python3

import requests
import json
import argparse

#Url = 'https://dnsapi.cn/Record.List'
#domain = '.qiniudn.com'

def Get_Record_id(Url,domain):
    with open('qiniudn.com','r',encoding='utf-8') as f:
        for line in f.readlines():
            sub = line.split(domain)[0]
            #print(sub)

            data = {
                'login_token':r"70853,5c4d9a2bc2b11f2d982252cea69279e6",
                'format':'json',
                'domain_id':2336558,
                'sub_domain':sub,
                'record_type':'CNAME',
                'offset':0,
                'length':3
                }

            r = requests.post(Url,data=data,timeout=10)
            #print(r.json())
            try:
                print(sub + '.qiniudn.com',r.json()['records'][0]['id'])
                #print(r.text)
            except KeyError:
                pass

if __name__ == "__main__":
    Get_Record_id('https://dnsapi.cn/Record.List','.qiniudn.com')
