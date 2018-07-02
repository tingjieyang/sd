# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:34:35 2018

@author: Administrator
"""

##############作业汇总
##################################################
#作业1###############################################################################################################
x=3
y='男'
a=[20,17,29,30,28,32,31]
print('星期一是'+str(a[0])+'度')
print('星期二是'+str(a[1])+'度')
print('星期三是'+str(a[2])+'度')
print('星期四是'+str(a[3])+'度')
print('星期五是'+str(a[4])+'度')
print('星期六是'+str(a[5])+'度')
print('星期日是'+str(a[6])+'度')
#作业2####################################################################################################################
天气={"7天的温度":[20,17,29,30,28,32,31],"7天的天气情况":['晴','阴','晴','多云','晴','小雨','阵雨'],"今天的最高温度":[20,30,13,40,33,26,23]}
print('星期三的温度是'+str(天气["7天的温度"][2])+'度')
print('星期三的天气情况是'+str(天气["7天的天气情况"][2]))
print('今天最高的温度是'+str(天气["今天的最高温度"][3])+'度')
#作业3
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q=jinchang&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
print('温度是'+str(data['main']['temp'])+'度')
print('气压是'+str(data['main']['pressure'])+'百帕')
print('天气情况是'+data['weather'][0]['description'])
#作业4#####################################################################################################
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)

time=data['list'][0]['dt_txt']
temp=data['list'][0]['main']['temp']#温度
whe=data['list'][0]['weather'][0]['description']#天气
high=data['list'][0]['main']['temp_max']
low=data['list'][0]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
time=data['list'][2]['dt_txt']
temp=data['list'][2]['main']['temp']#温度
whe=data['list'][2]['weather'][0]['description']#天气
high=data['list'][2]['main']['temp_max']
low=data['list'][2]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
time=data['list'][4]['dt_txt']
temp=data['list'][4]['main']['temp']#温度
whe=data['list'][4]['weather'][0]['description']#天气
high=data['list'][4]['main']['temp_max']
low=data['list'][4]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
time=data['list'][8]['dt_txt']
temp=data['list'][8]['main']['temp']#温度
whe=data['list'][8]['weather'][0]['description']#天气
high=data['list'][8]['main']['temp_max']
low=data['list'][8]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
time=data['list'][10]['dt_txt']
temp=data['list'][10]['main']['temp']#温度
whe=data['list'][10]['weather'][0]['description']#天气
high=data['list'][10]['main']['temp_max']
low=data['list'][10]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
time=data['list'][12]['dt_txt']
temp=data['list'][12]['main']['temp']#温度
whe=data['list'][12]['weather'][0]['description']#天气
high=data['list'][12]['main']['temp_max']
low=data['list'][12]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
t='2018-06-23 06:00:00'
temp=data['list'][16]['main']['temp']#温度
whe=data['list'][16]['weather'][0]['description']#天气
high=data['list'][16]['main']['temp_max']
low=data['list'][16]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(t,temp,whe,high,low))
time=data['list'][18]['dt_txt']
temp=data['list'][18]['main']['temp']#温度
whe=data['list'][18]['weather'][0]['description']#天气
high=data['list'][18]['main']['temp_max']
low=data['list'][18]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
time=data['list'][20]['dt_txt']
temp=data['list'][20]['main']['temp']#温度
whe=data['list'][20]['weather'][0]['description']#天气
high=data['list'][20]['main']['temp_max']
low=data['list'][20]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
time=data['list'][24]['dt_txt']
temp=data['list'][24]['main']['temp']#温度
whe=data['list'][24]['weather'][0]['description']#天气
high=data['list'][24]['main']['temp_max']
low=data['list'][24]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
time=data['list'][12]['dt_txt']
temp=data['list'][12]['main']['temp']#温度
whe=data['list'][12]['weather'][0]['description']#天气
high=data['list'][12]['main']['temp_max']
low=data['list'][12]['main']['temp_min']
print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))
#英文版
for i in range(37):
    if i%2==0 and i!=6 and i!=14 and i!=22 and i!=30:
        time=data['list'][i]['dt_txt']
        temp=data['list'][i]['main']['temp']#温度
        whe=data['list'][i]['weather'][0]['main']#天气
        high=data['list'][i]['main']['temp_max']
        low=data['list'][i]['main']['temp_min']
        print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}度，最低气温是{}度".format(time,temp,whe,high,low))
    
    
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)

time=data['list'][0]['dt_txt']
temp=data['list'][0]['main']['temp']#温度
whe=data['list'][0]['weather'][0]['main']#天气
high=data['list'][0]['main']['temp_max']
low=data['list'][0]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")

time=data['list'][2]['dt_txt']
temp=data['list'][2]['main']['temp']#温度
whe=data['list'][2]['weather'][0]['main']#天气
high=data['list'][2]['main']['temp_max']
low=data['list'][2]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][4]['dt_txt']
temp=data['list'][4]['main']['temp']#温度
whe=data['list'][4]['weather'][0]['main']#天气
high=data['list'][4]['main']['temp_max']
low=data['list'][4]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][8]['dt_txt']
temp=data['list'][8]['main']['temp']#温度
whe=data['list'][8]['weather'][0]['main']#天气
high=data['list'][8]['main']['temp_max']
low=data['list'][8]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][10]['dt_txt']
temp=data['list'][10]['main']['temp']#温度
whe=data['list'][10]['weather'][0]['main']#天气
high=data['list'][10]['main']['temp_max']
low=data['list'][10]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][12]['dt_txt']
temp=data['list'][12]['main']['temp']#温度
whe=data['list'][12]['weather'][0]['main']#天气
high=data['list'][12]['main']['temp_max']
low=data['list'][12]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
t='2018-06-23 06:00:00'
temp=data['list'][16]['main']['temp']#温度
whe=data['list'][16]['weather'][0]['main']#天气
high=data['list'][16]['main']['temp_max']
low=data['list'][16]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][18]['dt_txt']
temp=data['list'][18]['main']['temp']#温度
whe=data['list'][18]['weather'][0]['main']#天气
high=data['list'][18]['main']['temp_max']
low=data['list'][18]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][20]['dt_txt']
temp=data['list'][20]['main']['temp']#温度
whe=data['list'][20]['weather'][0]['main']#天气
high=data['list'][20]['main']['temp_max']
low=data['list'][20]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
temp=data['list'][24]['main']['temp']#温度
whe=data['list'][24]['weather'][0]['main']#天气
high=data['list'][24]['main']['temp_max']
low=data['list'][24]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][26]['dt_txt']
temp=data['list'][26]['main']['temp']#温度
whe=data['list'][26]['weather'][0]['main']#天气
high=data['list'][26]['main']['temp_max']
low=data['list'][26]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][28]['dt_txt']
temp=data['list'][28]['main']['temp']#温度
whe=data['list'][28]['weather'][0]['main']#天气
high=data['list'][28]['main']['temp_max']
low=data['list'][28]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][32]['dt_txt']
temp=data['list'][32]['main']['temp']#温度
whe=data['list'][32]['weather'][0]['main']#天气
high=data['list'][32]['main']['temp_max']
low=data['list'][32]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][34]['dt_txt']
temp=data['list'][34]['main']['temp']#温度
whe=data['list'][34]['weather'][0]['main']#天气
high=data['list'][34]['main']['temp_max']
low=data['list'][34]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")
time=data['list'][36]['dt_txt']
temp=data['list'][36]['main']['temp']#温度
whe=data['list'][36]['weather'][0]['main']#天气
high=data['list'][36]['main']['temp_max']
low=data['list'][36]['main']['temp_min']
print("Today is{},tempreture is{}，weather is{}，the highist tempretrue{}，the lowest tempretrue{}".format(time,temp,whe,high,low))
if whe=='Clouds':
    print("今天的建议是不抹防晒霜")
if whe=='Clear':
    print("不上学")
if whe=='Rain':
    print("好好学习吧！")

temp=data['list'][2]['main']['temp']#温度
def temp():
    temp1=data['list'][0]['main']['temp']#温度
    temp2=data['list'][2]['main']['temp']#温度
    temp3=data['list'][4]['main']['temp']#温度
    temp4=data['list'][8]['main']['temp']#温度
    temp5=data['list'][10]['main']['temp']#温度
    temp6=data['list'][12]['main']['temp']#温度
    temp7=data['list'][16]['main']['temp']#温度
    temp8=data['list'][18]['main']['temp']#温度
    temp9=data['list'][20]['main']['temp']#温度
    temp10=data['list'][24]['main']['temp']#温度
    temp11=data['list'][26]['main']['temp']#温度 
    temp12=data['list'][28]['main']['temp']#温度 
    temp13=data['list'][32]['main']['temp']#温度
    temp14=data['list'][34]['main']['temp']#温度
    temp15=data['list'][36]['main']['temp']#温度
  
print(int(temp1)*"-")
print(int(temp2)*"-")
print(int(temp3)*"-")
print(int(temp4)*"-")
print(int(temp5)*"-")
print(int(temp6)*"-")
print(int(temp7)*"-")
print(int(temp8)*"-")
print(int(temp9)*"-")
print(int(temp10)*"-")
print(int(temp11)*"-")
print(int(temp12)*"-")
print(int(temp13)*"-")
print(int(temp14)*"-")


ls=[]
for i in range(30):
    if(i%2==0)&(i!=14)&(i!=22)&(i!=30):
ls.append(23)
ls.append(43)
ls.append(21)
ls.append(24)
ls.append(16)
ls.append(28)
ls.append(33)
ls.append(23)
ls.append(27)
ls.append(22)
ls.append(13)
sorted(ls)

#作业5######################################################
"""
Created on Thu Jun 21 14:39:54 2018
函数：
变量(生命周期)
全局变量，局部变量(函数内)
练习五:实现练习四，
1.使用函数写出来。定义函数，输出每一天6:00,12:00,18:00的天气信息
2.打印折线图,使用字符串的*号操作
10----------
5-----
@author: Administrator
"""


def day(i):
    for i in range(37):
        if i%2==0 and i!=6 and i!=14 and i!=22 and i!=30:
            time=data['list'][i]['dt_txt']
            temp=data['list'][i]['main']['temp']#温度
            whe=data['list'][i]['weather'][0]['description']#天气
            high=data['list'][i]['main']['temp_max']
            low=data['list'][i]['main']['temp_min'] 
        return day
 def summ(day):          
     print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(time,temp,whe,high,low))

summ(day(0))
summ(day(1))
    
    
def time(i):
     time=data['list'][i]['dt_txt']
     
    
def a(i):
    a=data['list'][i]['dt_txt']
    return a
def b(i):
    b=data['list'][i]['main']['temp']#温度
    return b
def c(i):
    c=data['list'][i]['weather'][0]['description']#天气
    return c
def d(i):
    d=data['list'][i]['main']['temp_max']
    return d
def e(i):
    e=data['list'][i]['main']['temp_min']
    return e
def summ(a,b,c,d,e):          
     print("今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度".format(a,b,c,d,e))
summ(a(0),b(0),c(0),d(0),e(0))
summ(a(2),b(2),c(2),d(2),e(2))
summ(a(4),b(4),c(4),d(4),e(4))
summ(a(8),b(8),c(8),d(8),e(8))
summ(a(10),b(10),c(10),d(10),e(10))
summ(a(12),b(12),c(12),d(12),e(12))
summ(a(14),b(14),c(14),d(14),e(14))
summ(a(18),b(18),c(18),d(18),e(18))
summ(a(20),b(20),c(20),d(20),e(20))
summ(a(22),b(22),c(22),d(22),e(22))
summ(a(24),b(24),c(24),d(24),e(24))
summ(a(26),b(26),c(26),d(26),e(26))
summ(a(30),b(30),c(30),d(30),e(30))
summ(a(32),b(32),c(32),d(32),e(32))
summ(a(34),b(34),c(34),d(34),e(34))
summ(a(36),b(36),c(36),d(36),e(36))

#5.2打印折线图
def d(i):
    d=data['list'][i]['main']['temp_max']
print(int(b(0))*"-")
print(int(b(2))*"-")
print(int(b(4))*"-")
print(int(b(8))*"-")
print(int(b(10))*"-")
print(int(b(12))*"-")
print(int(b(14))*"-")
print(int(b(18))*"-")
print(int(b(20))*"-")
print(int(b(22))*"-")
print(int(b(26))*"-")
print(int(b(28))*"-")
print(int(b(30))*"-")
print(int(b(32))*"-")
print(int(b(34))*"-")
print(int(b(36))*"-")#    

#作业6#################################
"""
Created on Thu Jun 21 15:52:44 2018
练习六：获取淘宝数据并且展示(只要第一页的商品48个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""
 #6.1
https://s.taobao.com/search?q=%E6%89%8B%E5%8A%9E&bcoffset=3&ntoffset=3&p4ppushleft=1,48&s=44&ajax=true
    
    
import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E4%B9%A6&bcoffset=3&ntoffset=3&p4ppushleft=1,48&s=44&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

def a(i):
    name=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    return name
def b(i):
    price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    return price
def c(i):
    sale=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    return sale
def d(i):
    store=data['mods']['itemlist']['data']['auctions'][i]['nick']
    return store
def e(i):
    address=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    return address

for i in range(0,44):
    print('书名:{},价格:{},销量:{},书店名:{},地址:{}'.format(a(i),b(i),c(i),d(i),e(i)))





print(name,end='/t')

print(price,end='/t')

print(sale,end='/t')

print(sale,end='/t')

print(store,end='/t')

print(addres,end='/t')
#
#6.2排序
print('销量升序为：')
ls=[]

c0=c(0)
c01=c0[0:4]
ls.append(c01)
c1=c(1)
c11=c1[0:3]
ls.append(c01)
c2=c(2)
c21=c2[0:2]
ls.append(c21)
c3=c(3)
c31=c3[0:2]
ls.append(c31)
c4=c(4)
c41=c4[0:2]
ls.append(c41)
c5=c(5)
c51=c5[0:2]
ls.append(c51)
c6=c(6)
c61=c6[0:2]
ls.append(c61)
c7=c(7)
c71=c7[0:2]
ls.append(c71)
c8=c(8)
c81=c8[0:2]
ls.append(c81)
c9=c(9)
c91=c9[0:2]
ls.append(c91)
c10=c(10)
c101=c10[0:2]
ls.append(c101)
c11=c(11)
c111=c11[0:3]
ls.append(c111)
sorted(ls)
print(c(1))
for i in range(0,11):
   sale=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    d=str(sale)
    ls.append(d)

print('价格降序为：')
ls=[]
for i in range(0,11):
    price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    b=float(price)
    ls.append(b)
lsl=sorted(ls,reverse=True)
print(lsl)
for i in range(0,44):
    free=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    a=float(free)
    if a==0.00:
        print(i)
        name=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
        price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
        sale=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        store=data['mods']['itemlist']['data']['auctions'][i]['nick']
        address=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
        print('书名:{},价格:{},销量:{},书店名:{},地址:{}，，，，，，包邮'.format(name,price,sale,store,address))

#第7题
'''        #
练习七:全球天气未来3天
1.使用多选其一，完成天气的提醒
2.一定要多ci使用到for循环,偶尔用一次while循环
3.初步学会使用debug，知道里面的设置断点，下一步执行，下一个断点执行。
4.《闪屏的制作》进入我们天气程序的时候，有一个温馨图形的提示。使用循环实现，
  要知道是什么意思，照抄网上代码不行。
'''
#第七题
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=lanzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
datanew=json.loads(data)
def a(i):
    time=datanew['list'][i]['dt_txt']
    return time
def b(i):
    temp=datanew['list'][i]['main']['temp']#温度
    return time
def c(i):
    whe=datanew['list'][i]['weather'][0]['description']#天气
    return whe
def d(i):
    high=datanew['list'][i]['main']['temp_max']
    return high
def e(i):
    low=datanew['list'][i]['main']['temp_min']
    return low
for i in range(0,37):
    if i==11 or i==19 or i==27:
        print('今天是{},温度是{}度，天气情况是{}，最高气温是{}度，最低气温是{}度'.format(a(i),b(i),c(i),d(i),e(i)))
        temp=datanew['list'][i]['main']['temp']#温度
        if temp>30.5:
            print('请戴墨镜')
        else:
            print('go home')
    else:
        print('')



for i in range(11):
    if i==0 or i==1 or i==2 :
        print('$$$$$猪$$$$$')
    elif i==3 or i==4 or i==5:
         print('$$$$$$$$$$猪猪猪$$$$$$$$')
    elif i==6 or i==7 or i==8:
         print('$$$$$$$$$$猪猪猪猪猪$$$$$$$$$$$$$')
    elif i==9 or i==10 or i==11:
         print('$$$$$$$$$$$$$$$$$$$$$猪猪猪猪猪$$$$$$$$$$')
    elif i==6 or i==7 or i==8:
         print('$$$$$$$$$$猪猪猪猪猪$$$$$$$$$$$$$')
    elif i==6 or i==7 or i==8:
         print('$$$$$$$$$$猪猪猪猪猪$$$$$$$$$$$$$')
    elif i==6 or i==7 or i==8:
         print('$$$$$$$$$$猪猪猪猪猪$$$$$$$$$$$$$')
         
#第8题
'''
第8题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格
'''

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E6%B7%B1%E5%9C%B3&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data1=json.loads(data)

f=open('./c.csv','w')#csv表格文件，以逗号分割
f.write(data1)
f.close()#关闭文件，保存文件

def a(i):
    name=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    return name
def b(i):
    price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    return price
def c(i):
    sale=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    return sale
def d(i):
    store=data['mods']['itemlist']['data']['auctions'][i]['nick']
    return store
def e(i):
    address=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    return address

for i in range(0,44):
    print('书名:{},价格:{},销量:{},书店名:{},地址:{}'.format(a(i),b(i),c(i),d(i),e(i)))

#第9题
'''
题目九：余票查询组项目
1.查询某种火车的余票，动车，高铁，直达，特快....
2.组长将各组员功能汇总
'''
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-30&leftTicketDTO.from_station=XAY&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')

import json
data=json.loads(data)
data=data['data']['result']

p='  '
s="%2F2fkaLCTp%2BkAaV0E7rrtyf9%2BAD3EaH7JyE%2FYs%2B%2BrlscFvkM0XHHuM8D7jVMXTzlB%0Az43aG7hx09zw6WwHzINE58PN4GwzkkABvfJS7BzMK%2FhBhu%2BbQtzBJZWtALse%2BYxofDwmoKdGrACX%0An3Qge0RetdqmplnDGWFvstp0y4qgu4%2B7TWW0nJ18jIODYEGM9anC48Tv7TEA1HxnjjFCgbXDgOr%2F%0AducTaklevxFS4WR7YaPdphj8g5rd50mGIQ%3D%3D|预订|4f000G191404|G1914|EAY|AOH|EAY|AOH|06:26|13:23|06:57|Y|ypXlLe%2Bt8CUa4Jll5wRM0so3teT%2F3jth7z0PLcKSu70frio2|20180630|3|Y2|01|13|1|0|||||||||||有|有|18||O0M090|OM9|1","|列车运行图调整,暂停发售|4f0000G36203|G362|EAY|AOH|EAY|AOH|24:00|24:00|99:59|IS_TIME_NOT_BUY||20180630||Y2|01|05|0|1|||||||||||||||||0","94F1ZnSJGd%2FmkyvCXVo3ej2F626T%2FbrE%2B%2B7zSQ3Zi%2FxIyFagm0bo%2BH7n92eB%2FQPE2d8YL9eFUpLn%0AptKCT7v%2Bchntzi8MxJXGK7%2BIxX%2B5MLP6%2FDMmJMjaZ4yhZ7ertnH50%2BYt7TxAkgH6Cbt8OgsHza5O%0AViD2SvzO%2Fw517Bi6x2HEN2pYwiV3SF%2Frs%2B7MP%2FrD4wkbrPpLCL1kK0myOapFrjZKhLoKMm2obCY4%0AGx8ODnsBPduqy2dRR5De%2B0PxdeJTNBFb4g%3D%3D|预订|4f000G191809|G1918|EAY|AOH|EAY|AOH|09:23|16:45|07:22|Y|XlIg46hsfKKhtGopWzfcHNDHDXMX6qCwlUlfHVh2p%2B3N%2FWWj|20180630|3|Y2|01|16|1|0|||||||||||有|有|16||O0M090|OM9|0","OimdDap%2F%2F7L%2FiN7oXAXGmUay8OhsmgVgWRIu9kFRo8cOkFRqJo6IX%2BMD%2FxueaofV5MQvGFfPylVw%0Ab3SkCT2f4Wedwug%2FmnEEAyGnDv0GUbsEVN7zsWTpf57qrjzUSfLzRe4tM2bQqyE%2F7rIaSB3VaXpL%0AMdAYGkn17vMpICQRuuxAHYX476qJYi8q3cc6JfVMgYfREhYmrq4qJtwUcZ7naAXDSpip3p1VoyZl%0A8z8TfWUZZV6uqxY0i5F%2FaoWSExd5PovmUQ%3D%3D|预订|760000K29208|K292|CDW|SHH|XAY|SHH|09:37|05:34|19:57|Y|NCgBu0Vvu3sM66Yu4Ka5v3N6xWYoDtvA8MkaAHmwhfDgKEgJaiN7fwP5P1M%3D|20180629|3|W1|10|24|0|0||||无|||有||无|无|||||10401030|1413|0","krz%2BlgKHuzLcVUKbq6lApbjdOoIn7H3VrNMB3EdBSjAEO8YVvmm%2BWTcMMyVvXEdyahOfBD8uH%2BcL%0AkkRcxz7C6TrWQfleUmgfBXNK4LUP28NccGYF01JlSnH0rABOZIIjZuOesqo1F92r4rakiEQXWY1h%0ApyijtzO3m5xiczx1vlBZPT3FD6WJ1hManBo9QDUarqnojbeOMRK8vrOZEmt7C3H5IiHaDsWY4JW0%0A9pmQ90h6Zb3cAAAZqeGgfeFN41TkLbJZlw%3D%3D|预订|880000K3780M|K378|XNO|SHH|XAY|SHH|09:52|05:24|19:32|Y|nox%2BJblqePbZLjUi6It5MtT9iWRXCj2xnu39lUGP1ICpaSCt3ITTlvwvwJo%3D|20180629|3|O1|11|25|0|0||||无|||无||无|1|||||10401030|1413|1","Jsh10eDN5W68S0S4nO6VSh3DDl1m00lD9LpisxLrd5AOGMKNk0O5rTNFE9F7utei7Q%2FCYmQ1MCJ5%0Azk1n3AarQQ%2FAnyvNiFLsjYxLIlrK4SiCYqOlzlEVTMVmSioIy%2F7RkCy6xjqCeVJrfngmoE6WXTr%2F%0AtBt7gG6XKgiaLurR64jz3LvrwpAPkJwns%2BHYg9DWvhmvx94X7Hzs%2FXZhtdxR2IlKa9ntbPV9xJdC%0ANI0eXlgE6i8jdw2yR5VPFXmYfa2tsOfezA%3D%3D|预订|4f000G192207|G1922|EAY|AOH|EAY|AOH|10:23|17:38|07:15|Y|CQDJP2X%2F8aMnF0vmcTphP4%2BgAzCvkdG%2BpLL6oz6mFrQl1bwF|20180630|3|Y2|01|15|1|0|||||||||||有|无|5||O0M090|OM9|0","7ICOEfbVyh4sUsVRD5iotW%2BPvsYe%2BK0NKVgDFvW3UYtQji0zrupwRF7y6Cyx3twLF45fgDLeNZd9%0ARtCjjPO3PIcGcLQyxRs2pRAyOzSfNZ5EFifNUeht2gztXPKf%2Fr%2F9yKJhlcgkAiKP9vmNSgm9BvFC%0ALQLfM6EpJ12aoN9WloedBcZnMsUOmX5nrcUt%2BxCblhqEx2j9DfsRzrEfzF1WTneKK0KyL4IAQ83t%0Aw%2BzfobIpZgAFuMQvGBlnczGmoz9UeHQGLg%3D%3D|预订|870000K35964|K362|YIJ|SHH|XAY|SHH|10:54|05:56|19:02|Y|9gPoSLJi0TC7Y4Nb96goeAm%2FeAiwVBrP4IwxYIGkB19PvK1tdWtprZXgHW0%3D|20180629|3|J1|11|25|0|0||||3|||有||无|无|||||10401030|1413|0","CD2l5AWaL7wM8QK3rFKICE8fJyGEmsKa4mEaKYgAdon7567f8I%2B6rX9YDzHIvqcDNhCMbyxvmT%2FQ%0AGndiED7K7PwY%2FbNSbW2Xbw9PsZu6peaFf82PQ4IIDUmMTq2aL%2Ftfhr0UwtUvukZLHLDO6RckciJj%0AYOHrxT7nwF97hW2YpstFqKao7wAVVomdyV8fFjSj%2BoKm88LjkHSIDcYtM7j84k5pkN%2FYWmnKHT8k%0Av49NQBYaqMcY6sdcA%2BoDr5ViiYM0pPx1Pw%3D%3D|预订|4f000G192608|G1926|EAY|AOH|EAY|AOH|12:25|19:49|07:24|Y|PFClUaoYjmrhVKq44lQvXJ5EDE46lvnnqQR3Vh5Wd0v5d3g1|20180630|3|Y2|01|14|1|0|||||||||||有|有|无||O0M090|OM9|0","LE4nNQyIOoMbmtf1H1c%2BRYuDNB%2FGyFXbp8Hi1h1Qf1spaS%2BL2oZwRvs%2BFWvzIdW7NA6kkRL4la1o%0ANtpCzArvI7JovJPs2z89BgyJemiIl1Noj6JprHa9uIQsMijekVEv%2FHPm25fQbxVziVRDqUbVkCcd%0AH475O0GIaBr8YfGnLvU8pqtRRf7h7p%2BkTkfeouV58M6O%2FG%2FJrhikxXiFQTNOSBu9sf1%2FE%2FeZbGjN%0AVavZ%2FIoiQGSEZ3tMDS%2Fdo1MpIgGwqfDUjQ%3D%3D|预订|8d000G197202|G1972|LAJ|AOH|EAY|AOH|13:50|21:24|07:34|Y|SFtxtiU00jkdNwHbF6hldavZ5ipZsRBjqqQPdDXrfcWIGEb7|20180630|3|J1|07|21|1|0|||||||||||无|1|无||O0M090|OM9|0","qVGnXv0ocHuJrsI99IsXEwDBCP3MGnPQjYMi9CO%2FQcsdkrTMjkCPyDV5bRwwrJdxbJLxJ0t6ouej%0ASFKqNcm5QBia6XCQNli2AdBf4wZQlsiT1cre3Wbsc%2Bu9IVViLE1KJTwwEZc1bRfZGDn%2FPVuwqUhY%0A4xQSdaBKj9UCNXgNeC5BaT58dic1ov7Ht2CGYzku4bR7qpQRYxltJqJ1PtKGF16g4znuOp1rkSEC%0AKQemCIh5FS4G7ZUYqtpk57mBMKiUMVAWWg%3D%3D|预订|77000G197602|G1976|CXW|AOH|EAY|AOH|14:57|22:25|07:28|Y|YrKoTen995k6iyrq7XxX6vz9KXipH2b4ygDtpfHAqd8s8TL6|20180630|3|W2|09|23|1|0|||||||||||2|10|8||O0M090|OM9|0","QIICHe6N8fBOtCPsZEb0QazE8gl7EOxPNH8X5v%2Fgbueed9j3h%2BqxMzDMFfsapRPv%2BuJmxTq4fCly%0AsnyV6Yb4pQW5GHjAgx11%2FosixtoJSKLx4dtD5CwFqZ%2FIWZ9oWDTDYbkdbiawEWlfKDv%2Fm5KP%2B8pk%0A4BcA1ZsyWbmxJe9wGk1GHjQVSWmtDMYRftd5N9icN0lK1Teb6%2BH176y3hh2xU4Zx2S3RVJMeHODa%0AgFsJD0MmmEI5rOQGfwH3VGuOJtUaF4%2B5iw%3D%3D|预订|4f000G193807|G1938|EAY|AOH|EAY|AOH|15:13|21:46|06:33|Y|hSFkV49GBVihOBIfps5qb5RanZoCa5TjO7r3rbhgTZeLJaoQ|20180630|3|Y2|01|09|1|0|||||||||||有|有|有||O0M090|OM9|0","CeN7wlMS82qLHHFmvWIZJpxM%2BX3mbAIcjJ6oa%2BBXA43YgZBrzvV5Q4M%2FwqkxejVK7X8pA8oLsSck%0ALqVMoTFlMPXU7pGEK%2FIiDibS9qCOGOlrTa1nP0JWpBMvEa4kwcX49VvKVbhhEW1jV%2FYdjzmjLezC%0ALtadT4mvzdS79DEj1RBBAeKxFFmF%2BLKXvSAfmTlcLVjcNJ%2BK67QGXziYGaYI9KXc2Akx7A9DJSWh%0A9LnExtwaiLgVTm4TXB5Ea95VEsQwMvzcGA%3D%3D|预订|4f000G194205|G1942|EAY|AOH|EAY|AOH|15:50|23:23|07:33|Y|WEVOlgG4VnQG87Mwax5OOEvbHHKG3Fb5byyihjYo8SWaMMSz|20180630|3|Y2|01|16|1|0|||||||||||有|16|10||O0M090|OM9|0"
G1914=s[0].split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(11),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
G1914[6]='西安北'
G1914[7]='虹桥'
lsG1914=[G1914[3],[G1914[6],G1914[7]],[G1914[8],G1914[9]],G1914[10],G1914[32],G1914[31],G1914[30],'--','--','--','--','--','--','--','--',G1914[1]]
for i in lsG1914:
    print(str(i).center(14).replace('[', '').replace(']', '').replace(',','/').replace('’,''),end='')
    
print()
G1918=s[2].split('|')
G1918[6]='西安北'
G1918[7]='虹桥'
lsG1918=[G1918[3],[G1918[6],G1918[7]],[G1914[8],G1918[9]],G1918[10],G1918[32],G1918[31],G1918[30],'--','--','--','--','--','--','--','--',G1918[1]]
for i in lsG1918:
    print(str(i).center(14).replace('[','').replace(']',''),end='')

print()
G1922=s[5].split('|')
G1922[6]='西安北'
G1922[7]='虹桥'
lsG1922=[G1922[3],[G1922[6],G1922[7]],[G1922[8],G1922[9]],G1922[10],G1922[32],G1922[31],G1922[30],'--','--','--','--','--','--','--','--',G1922[1]]
for i in lsG1922:
    print(str(i).center(14).replace('[','').replace(']',''),end='')

print()
G1926=s[7].split('|')
G1926[6]='西安北'
G1926[7]='虹桥'
lsG1926=[G1926[3],[G1926[6],G1926[7]],[G1926[8],G1926[9]],G1926[10],G1926[32],G1926[31],G1926[30],'--','--','--','--','--','--','--','--',G1926[1]]
for i in lsG1926:
    print(str(i).center(14).replace('[','').replace(']',''),end='')

print()
G1972=s[8].split('|')
G1972[6]='西安北'
G1972[7]='虹桥'
lsG1972=[G1972[3],[G1972[6],G1972[7]],[G1972[8],G1972[9]],G1972[10],G1972[32],G1972[31],G1972[30],'--','--','--','--','--','--','--','--',G1972[1]]
for i in lsG1972:
    print(str(i).center(14).replace('[','').replace(']',''),end='')


print()
G1976=s[9].split('|')
G1976[6]='西安北'
G1976[7]='虹桥'
lsG1976=[G1976[3],[G1976[6],G1976[7]],[G1976[8],G1976[9]],G1976[10],G1976[32],G1976[31],G1976[30],'--','--','--','--','--','--','--','--',G1976[1]]
for i in lsG1976:
    print(str(i).center(14).replace('[','').replace(']',''),end='')

print()
G1938=s[10].split('|')
G1938[6]='西安北'
G1938[7]='虹桥'
lsG1938=[G1938[3],[G1938[6],G1938[7]],[G1938[8],G1938[9]],G1938[10],G1938[32],G1938[31],G1938[30],'--','--','--','--','--','--','--','--',G1938[1]]
for i in lsG1938:
    print(str(i).center(14).replace('[','').replace(']',''),end='')

print()
G1942=s[11].split('|')
G1942[6]='西安北'
G1942[7]='虹桥'
lsG1942=[G1942[3],[G1942[6],G1942[7]],[G1942[8],G1942[9]],G1942[10],G1942[32],G1942[31],G1942[30],'--','--','--','--','--','--','--','--',G1942[1]]
for i in lsG1942:
    print(str(i).center(14).replace('[','').replace(']',''),end='')

#第10题
'''
第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排
'''
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-30&leftTicketDTO.from_station=XAY&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')

import json
data=json.loads(data)
data=data['data']['result']

p='  '
s="%2F2fkaLCTp%2BkAaV0E7rrtyf9%2BAD3EaH7JyE%2FYs%2B%2BrlscFvkM0XHHuM8D7jVMXTzlB%0Az43aG7hx09zw6WwHzINE58PN4GwzkkABvfJS7BzMK%2FhBhu%2BbQtzBJZWtALse%2BYxofDwmoKdGrACX%0An3Qge0RetdqmplnDGWFvstp0y4qgu4%2B7TWW0nJ18jIODYEGM9anC48Tv7TEA1HxnjjFCgbXDgOr%2F%0AducTaklevxFS4WR7YaPdphj8g5rd50mGIQ%3D%3D|预订|4f000G191404|G1914|EAY|AOH|EAY|AOH|06:26|13:23|06:57|Y|ypXlLe%2Bt8CUa4Jll5wRM0so3teT%2F3jth7z0PLcKSu70frio2|20180630|3|Y2|01|13|1|0|||||||||||有|有|18||O0M090|OM9|1","|列车运行图调整,暂停发售|4f0000G36203|G362|EAY|AOH|EAY|AOH|24:00|24:00|99:59|IS_TIME_NOT_BUY||20180630||Y2|01|05|0|1|||||||||||||||||0","94F1ZnSJGd%2FmkyvCXVo3ej2F626T%2FbrE%2B%2B7zSQ3Zi%2FxIyFagm0bo%2BH7n92eB%2FQPE2d8YL9eFUpLn%0AptKCT7v%2Bchntzi8MxJXGK7%2BIxX%2B5MLP6%2FDMmJMjaZ4yhZ7ertnH50%2BYt7TxAkgH6Cbt8OgsHza5O%0AViD2SvzO%2Fw517Bi6x2HEN2pYwiV3SF%2Frs%2B7MP%2FrD4wkbrPpLCL1kK0myOapFrjZKhLoKMm2obCY4%0AGx8ODnsBPduqy2dRR5De%2B0PxdeJTNBFb4g%3D%3D|预订|4f000G191809|G1918|EAY|AOH|EAY|AOH|09:23|16:45|07:22|Y|XlIg46hsfKKhtGopWzfcHNDHDXMX6qCwlUlfHVh2p%2B3N%2FWWj|20180630|3|Y2|01|16|1|0|||||||||||有|有|16||O0M090|OM9|0","OimdDap%2F%2F7L%2FiN7oXAXGmUay8OhsmgVgWRIu9kFRo8cOkFRqJo6IX%2BMD%2FxueaofV5MQvGFfPylVw%0Ab3SkCT2f4Wedwug%2FmnEEAyGnDv0GUbsEVN7zsWTpf57qrjzUSfLzRe4tM2bQqyE%2F7rIaSB3VaXpL%0AMdAYGkn17vMpICQRuuxAHYX476qJYi8q3cc6JfVMgYfREhYmrq4qJtwUcZ7naAXDSpip3p1VoyZl%0A8z8TfWUZZV6uqxY0i5F%2FaoWSExd5PovmUQ%3D%3D|预订|760000K29208|K292|CDW|SHH|XAY|SHH|09:37|05:34|19:57|Y|NCgBu0Vvu3sM66Yu4Ka5v3N6xWYoDtvA8MkaAHmwhfDgKEgJaiN7fwP5P1M%3D|20180629|3|W1|10|24|0|0||||无|||有||无|无|||||10401030|1413|0","krz%2BlgKHuzLcVUKbq6lApbjdOoIn7H3VrNMB3EdBSjAEO8YVvmm%2BWTcMMyVvXEdyahOfBD8uH%2BcL%0AkkRcxz7C6TrWQfleUmgfBXNK4LUP28NccGYF01JlSnH0rABOZIIjZuOesqo1F92r4rakiEQXWY1h%0ApyijtzO3m5xiczx1vlBZPT3FD6WJ1hManBo9QDUarqnojbeOMRK8vrOZEmt7C3H5IiHaDsWY4JW0%0A9pmQ90h6Zb3cAAAZqeGgfeFN41TkLbJZlw%3D%3D|预订|880000K3780M|K378|XNO|SHH|XAY|SHH|09:52|05:24|19:32|Y|nox%2BJblqePbZLjUi6It5MtT9iWRXCj2xnu39lUGP1ICpaSCt3ITTlvwvwJo%3D|20180629|3|O1|11|25|0|0||||无|||无||无|1|||||10401030|1413|1","Jsh10eDN5W68S0S4nO6VSh3DDl1m00lD9LpisxLrd5AOGMKNk0O5rTNFE9F7utei7Q%2FCYmQ1MCJ5%0Azk1n3AarQQ%2FAnyvNiFLsjYxLIlrK4SiCYqOlzlEVTMVmSioIy%2F7RkCy6xjqCeVJrfngmoE6WXTr%2F%0AtBt7gG6XKgiaLurR64jz3LvrwpAPkJwns%2BHYg9DWvhmvx94X7Hzs%2FXZhtdxR2IlKa9ntbPV9xJdC%0ANI0eXlgE6i8jdw2yR5VPFXmYfa2tsOfezA%3D%3D|预订|4f000G192207|G1922|EAY|AOH|EAY|AOH|10:23|17:38|07:15|Y|CQDJP2X%2F8aMnF0vmcTphP4%2BgAzCvkdG%2BpLL6oz6mFrQl1bwF|20180630|3|Y2|01|15|1|0|||||||||||有|无|5||O0M090|OM9|0","7ICOEfbVyh4sUsVRD5iotW%2BPvsYe%2BK0NKVgDFvW3UYtQji0zrupwRF7y6Cyx3twLF45fgDLeNZd9%0ARtCjjPO3PIcGcLQyxRs2pRAyOzSfNZ5EFifNUeht2gztXPKf%2Fr%2F9yKJhlcgkAiKP9vmNSgm9BvFC%0ALQLfM6EpJ12aoN9WloedBcZnMsUOmX5nrcUt%2BxCblhqEx2j9DfsRzrEfzF1WTneKK0KyL4IAQ83t%0Aw%2BzfobIpZgAFuMQvGBlnczGmoz9UeHQGLg%3D%3D|预订|870000K35964|K362|YIJ|SHH|XAY|SHH|10:54|05:56|19:02|Y|9gPoSLJi0TC7Y4Nb96goeAm%2FeAiwVBrP4IwxYIGkB19PvK1tdWtprZXgHW0%3D|20180629|3|J1|11|25|0|0||||3|||有||无|无|||||10401030|1413|0","CD2l5AWaL7wM8QK3rFKICE8fJyGEmsKa4mEaKYgAdon7567f8I%2B6rX9YDzHIvqcDNhCMbyxvmT%2FQ%0AGndiED7K7PwY%2FbNSbW2Xbw9PsZu6peaFf82PQ4IIDUmMTq2aL%2Ftfhr0UwtUvukZLHLDO6RckciJj%0AYOHrxT7nwF97hW2YpstFqKao7wAVVomdyV8fFjSj%2BoKm88LjkHSIDcYtM7j84k5pkN%2FYWmnKHT8k%0Av49NQBYaqMcY6sdcA%2BoDr5ViiYM0pPx1Pw%3D%3D|预订|4f000G192608|G1926|EAY|AOH|EAY|AOH|12:25|19:49|07:24|Y|PFClUaoYjmrhVKq44lQvXJ5EDE46lvnnqQR3Vh5Wd0v5d3g1|20180630|3|Y2|01|14|1|0|||||||||||有|有|无||O0M090|OM9|0","LE4nNQyIOoMbmtf1H1c%2BRYuDNB%2FGyFXbp8Hi1h1Qf1spaS%2BL2oZwRvs%2BFWvzIdW7NA6kkRL4la1o%0ANtpCzArvI7JovJPs2z89BgyJemiIl1Noj6JprHa9uIQsMijekVEv%2FHPm25fQbxVziVRDqUbVkCcd%0AH475O0GIaBr8YfGnLvU8pqtRRf7h7p%2BkTkfeouV58M6O%2FG%2FJrhikxXiFQTNOSBu9sf1%2FE%2FeZbGjN%0AVavZ%2FIoiQGSEZ3tMDS%2Fdo1MpIgGwqfDUjQ%3D%3D|预订|8d000G197202|G1972|LAJ|AOH|EAY|AOH|13:50|21:24|07:34|Y|SFtxtiU00jkdNwHbF6hldavZ5ipZsRBjqqQPdDXrfcWIGEb7|20180630|3|J1|07|21|1|0|||||||||||无|1|无||O0M090|OM9|0","qVGnXv0ocHuJrsI99IsXEwDBCP3MGnPQjYMi9CO%2FQcsdkrTMjkCPyDV5bRwwrJdxbJLxJ0t6ouej%0ASFKqNcm5QBia6XCQNli2AdBf4wZQlsiT1cre3Wbsc%2Bu9IVViLE1KJTwwEZc1bRfZGDn%2FPVuwqUhY%0A4xQSdaBKj9UCNXgNeC5BaT58dic1ov7Ht2CGYzku4bR7qpQRYxltJqJ1PtKGF16g4znuOp1rkSEC%0AKQemCIh5FS4G7ZUYqtpk57mBMKiUMVAWWg%3D%3D|预订|77000G197602|G1976|CXW|AOH|EAY|AOH|14:57|22:25|07:28|Y|YrKoTen995k6iyrq7XxX6vz9KXipH2b4ygDtpfHAqd8s8TL6|20180630|3|W2|09|23|1|0|||||||||||2|10|8||O0M090|OM9|0","QIICHe6N8fBOtCPsZEb0QazE8gl7EOxPNH8X5v%2Fgbueed9j3h%2BqxMzDMFfsapRPv%2BuJmxTq4fCly%0AsnyV6Yb4pQW5GHjAgx11%2FosixtoJSKLx4dtD5CwFqZ%2FIWZ9oWDTDYbkdbiawEWlfKDv%2Fm5KP%2B8pk%0A4BcA1ZsyWbmxJe9wGk1GHjQVSWmtDMYRftd5N9icN0lK1Teb6%2BH176y3hh2xU4Zx2S3RVJMeHODa%0AgFsJD0MmmEI5rOQGfwH3VGuOJtUaF4%2B5iw%3D%3D|预订|4f000G193807|G1938|EAY|AOH|EAY|AOH|15:13|21:46|06:33|Y|hSFkV49GBVihOBIfps5qb5RanZoCa5TjO7r3rbhgTZeLJaoQ|20180630|3|Y2|01|09|1|0|||||||||||有|有|有||O0M090|OM9|0","CeN7wlMS82qLHHFmvWIZJpxM%2BX3mbAIcjJ6oa%2BBXA43YgZBrzvV5Q4M%2FwqkxejVK7X8pA8oLsSck%0ALqVMoTFlMPXU7pGEK%2FIiDibS9qCOGOlrTa1nP0JWpBMvEa4kwcX49VvKVbhhEW1jV%2FYdjzmjLezC%0ALtadT4mvzdS79DEj1RBBAeKxFFmF%2BLKXvSAfmTlcLVjcNJ%2BK67QGXziYGaYI9KXc2Akx7A9DJSWh%0A9LnExtwaiLgVTm4TXB5Ea95VEsQwMvzcGA%3D%3D|预订|4f000G194205|G1942|EAY|AOH|EAY|AOH|15:50|23:23|07:33|Y|WEVOlgG4VnQG87Mwax5OOEvbHHKG3Fb5byyihjYo8SWaMMSz|20180630|3|Y2|01|16|1|0|||||||||||有|16|10||O0M090|OM9|0"
ls=s.split('|')
G1914=s[0].split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(11),end='')
print()


##第11题
'''
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
'''
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=3&tn=78040160_26_pg&wd=%E6%91%84%E5%BD%B1&oq=clamp&rsv_pq=923aafd500011caf&rsv_t=97deOd77DA27c%2Bj2czubAhtqAafvYSYafFWOkGxFMEPbsJETw85YgY9EAIfH4GHN8Xp%2F2Tk&rqlang=cn&rsv_enter=1&inputT=17141&rsv_sug3=30&rsv_sug1=45&rsv_sug7=101&rsv_sug2=0&rsv_sug4=5166097&rsv_sug=1'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
description=re.compile('<div class="c-abstract">(.*?)</div>').findall(data)
net=re.compile('<a target="_blank" href="(.*?)" class="c-showurl" style="text-decoration:none;">(.*?)</a>').findall(data)
for i in range(7):
    print('标题是：{}\n描述是：{}\n网址是：{}\n'.format(ls[i],description[i],net[i]))

#第12题
'''
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压
'''
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=banan,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data1=r.urlopen(url).read().decode('utf-8')
print(data1)
description=re.compile('"description":"(.*?)"').findall(data1)
temp=re.compile('"temp":(.*?),').findall(data1)
pressure=re.compile('"pressure":(.*?),').findall(data1)

import re
for i in range(37):
    print('巴南的天气是：{}   温度是：{}度   气压是：{}百帕 '.format(description[i],temp[i],pressure[i]))


#第13题
'''
题目十三：糗事百科数据爬取
1.爬取作者和内容
2.爬取13页
3.下载图片。想做就做
'''
for i in range(1,13):
    req=r.Request('https://www.qiushibaike.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
    myurl=r.urlopen(req)
    print(myurl.getcode())
    data3=myurl.read().decode('utf-8')
    name='alt="(.*?)"'
    tent='<span>(.*?)</span>'
    import re
    r1=re.compile(name,re.S).findall(data3)
    r2=re.compile(tent,re.S).findall(data3)
    for t in range(27):
        print('作者：{},\n内容：{}'.format(r1[t],r2[t]))
#第14题
'''
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
'''
f=open('C:/Users/Administrator/Documents/Tencent Files/149132225/FileRecv/all_school.txt','r',encoding='utf-8')
ls=f.readlines()

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
import re
city_code=re.compile('"city_code":"(.*?)",').findall(d)
city=re.compile('"city":"(.*?)",').findall(d)



###获取网站编号
f=open('C:/Users/Administrator/Documents/Tencent Files/149132225/FileRecv/all_school.txt','r',encoding='utf-8')
content=f.read()
import re
net_code=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html').findall(content)
name=re.compile('  (.*?)http://www.gaokaopai').findall(content)
for i in range(2300):
    a=ls[i].split('\t')
    print('{}所对应的网址编号是：{}\n'.format(a[0],net_code[i]))



'﻿北京大学	北京	http://www.gaokaopai.com/daxue-jianjie-477.html'.split('\t')




<a href="http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html">(.*?)</a>
import urllib.request as r
url='http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
import re
city=re.compile('<span><a href="http://www.gaokaopai.com/daxue-(.*?)-0-0-0-0-0-0.html">',re.S).findall(d)
name=re.compile('<span><a href="http://www.gaokaopai.com/daxue-..-0-0-0-0-0-0.html">(.*?)</a></span>',re.S).findall(d)
for i in range(0,len(city)):
    print('{},代码是{}'.format(name[i],city[i]))

import urllib.request as r
url='http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html'
data='id=2948&type=2&city=50&state=1'.encode()
##14题第三问西藏理科

a={}
e=open('E:\hw/西藏文科（正确）.txt','r',encoding='utf-8')
l=e.readlines()
import json
for i in range(2300):
    a[i]=json.loads(l[i])
    data=json.loads(l)
for i in range(2300):
    if data['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
        print(area[city])
        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])
a=0
b=0
c=0

if '西藏'==plan:
   a=a+1 

import json
data=json.loads(l)

for i in range(2300):
    if data['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
        print(area[city])
        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])

#第15题
'''
题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法
'''
class Weather:
    def __init__(self,temp,de,pre):#########系统固定的方法
        self.temp=temp
        self.de=de
        self.pre=pre
    def tody(self):#self 有对象
        print(x+y)
    def bike(self):
        print('今天的天气情况是：温度是{}描述是{}气压是{}'.format(self.temp,self.de,self.pre))
future={'temp':[20,17,29]"de":['晴','阴','晴']"pre":[900,1000,1000]}
for i in range(3):
    a=Weather(furture['temp'][i],furture['de'][i],furture['pre'][i])
    a.today


#第16题
'''
题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例
'''
f=open('./全国高校招生.txt','r',encoding='utf-8')
data1=f.read()
import re
ls=re.compile('"plan":"(.*?)"',re.S).findall(data1)
a=0
for i in range(len(ls)):
    a=a+int(ls[i])
print(a)



################################################################
area={'黑龙江':'东北','吉林':'东北','辽宁':'东北','福建':'华东','江西':'华东','山东':'华东','北京':'华北','河北':'华北','天津':'华北','北京':'华北','山西':'华北','上海':'华东','江苏':'华东','浙江':'华东','安徽':'华东','河南':'华中','湖北':'华中','湖南':'华中','广东':'华南','广西':'华南','海南':'华南','西藏':'西南','四川':'西南','重庆':'西南','云南':'西南','贵州':'西南','甘肃':'西北','宁夏':'西北','青海':'西北','陕西':'西北','新疆':'西北','内蒙古':'西北'}
areaplan={'东北':0,'华北':0,'华中':0,'华东':0,'华南':0,'西北':0,'西南':0}
ls14=[]
f=open('C:/Users/Administrator/全国招生计划表0206C正确.txt','r',encoding='utf-8')
ls13=f.readlines()
for i in range(len(ls13)):
    import json
    ls14.append(json.loads(ls13[i]))
    
for k in range(len(ls14)):
    for j in range(len(ls14[k]['data'])):
        if ls14[k]["status"]==0:
            continue
        b=ls14[k]['data'][0]['city']
        areaplan[area[b]]=areaplan[area[b]]+int(ls14[k]['data'][j]['plan'])
print('招生人数如下：\n东北:{}\n华北：{}\n西北：{}\n华中：{}\n华南：{}\n西南:{}\n华东：{}'.format(areaplan['东北'],areaplan['华北'],areaplan['西北'],areaplan['华中'],areaplan['华南'],areaplan['西南'],areaplan['华东']))
f.close
#第17题(小组)
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides=7
colors=["steelblue","lightskyblue","skyblue","deepskyblue","lightblue",'powderblue','aqua']
for x in range(70):
    t.pencolor(colors[x%sides])
    t.forward(x*25/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)

s=[]
ls=[]
ls1=[]
ls2=[]
ls3=[]
import re
import urllib.request as r
for i in range(1,7):
    url='http://dianying.2345.com/list/jingdian-------{}.html'.format(i)
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    p=r.urlopen(req).read().decode('gbk','ignore')
    pat='<a title="(.*?)" target'
    pat1='target="_blank" href="//dianying.2345.com/detail/(.*?).html'
    ls=re.compile(pat,re.S).findall(p)
    ls2=re.compile(pat1,re.S).findall(p)
    for j in range(len(ls)):
        ls1.append(ls[j])
        ls3.append(ls2[j])
for ln in range(len(ls1)):
    print('{}:电影:{}'.format(ln,ls1[ln]))
for k in range(len(ls3)):
    url='http://dianying.2345.com/detail/{}.html '.format(ls3[k])
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    data=r.urlopen(url).read().decode('gbk')
    s.append(data)
p=open('./jingdian3.txt','w')
import re
for i in range(len(s)):
    a=re.compile('<h1>(.*?)</h1>',re.S).findall(s[i])
    b=re.compile('<span class="sAll">(.*?)</span>',re.S).findall(s[i])
    p.write('{}--电影名:{}  简介:{}\n'.format(i,a,b).replace("['",'').replace("']",'').replace("']",'').replace("'\r\n'",'').replace('\u3000\u3000',''))
p.close()                  
f=open('./jingdian3.txt','r')
ls4=f.readlines() 
ls4=open('./jingdian3.txt','r').readlines()
def xuhao(s):
    abc=''
    for i in ls4:
        if s==i.split('--')[0]:
            abc=i.split('--')[1]
            break
    return abc
while True:    
    shuzi=input("（备注：输入大于204号则退出APP）\n 以下APP为您推荐的人生必看百部电影，请您输入您感兴趣电影的序号: ") 
    x=xuhao(shuzi)
    print(x)
    if int(shuzi)>204: 
        break





















































