#-*- coding:utf-8 -*-  
  
import time
import datetime
import os
import subprocess


def setDate(indate):
    cmd="date "+indate
    os.system(cmd)

def runCmd(cmd):
    os.system("start "+cmd)#后台执行

def getTime():
  #  return time.strftime("%Y-%m-%d %X", time.localtime())
    return datetime.date.today()
   # return datetime.datetime.now()
   
if __name__ == '__main__':  
    today=getTime()
    #修改时间
    setDate('2017-08-27')
    #启动navicat
    cmd = r'C:\"Program Files"\PremiumSoft\"Navicat for MySQL"\navicat.exe'
    runCmd(cmd)
    time.sleep(5)
    #还原时间
    setDate(f'{today}')
    #print(today)
    
    
    
