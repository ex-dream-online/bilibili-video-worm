import requests
import re
import datetime
import random
import time
import openpyxl

global bv
bv=input('请输入您想要爬取的视频的BV号:')
n=int(input('请输入您想爬取的数据条数(每两条数据间隔大概30s,您可以在下方更改间隔时间):'))

#获取av号
def get_av():
    global aid
    urla='http://api.bilibili.com/x/web-interface/archive/stat?bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"aid":\d+',str(js)).group(0)
    aid=re.search(r'\d+',str(raw)).group(0)
    return aid
get_av()
#获取cid
def get_cid():
    global cid
    urla='https://api.bilibili.com/x/player/pagelist?bvid='
    urlb='&jsonp=jsonp'
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv+urlb,headers=header).text
    #数据正则筛选
    raw=re.search(r'"cid":\d+',str(js)).group(0)
    cid=re.search(r'\d+',str(raw)).group(0)
    return cid
get_cid()
#获取播放量
def get_view():
    global view
    urla='http://api.bilibili.com/x/web-interface/archive/stat?bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"view":\d+',str(js)).group(0)
    view=re.search(r'\d+',str(raw)).group(0)
    return view
#获取弹幕数
def get_danmaku():
    global danmaku
    urla='http://api.bilibili.com/x/web-interface/archive/stat?bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"danmaku":\d+',str(js)).group(0)
    danmaku=re.search(r'\d+',str(raw)).group(0)
    return danmaku
#获取评论数
def get_reply():
    global reply
    urla='http://api.bilibili.com/x/web-interface/archive/stat?bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"reply":\d+',str(js)).group(0)
    reply=re.search(r'\d+',str(raw)).group(0)
    return reply
#获取收藏数
def get_favorite():
    global favorite
    urla='http://api.bilibili.com/x/web-interface/archive/stat?bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"favorite":\d+',str(js)).group(0)
    favorite=re.search(r'\d+',str(raw)).group(0)
    return favorite
#获取硬币数
def get_coin():
    global coin
    urla='http://api.bilibili.com/x/web-interface/archive/stat?bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"coin":\d+',str(js)).group(0)
    coin=re.search(r'\d+',str(raw)).group(0)
    return coin
#获取硬币数
def get_share():
    global share
    urla='http://api.bilibili.com/x/web-interface/archive/stat?bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"share":\d+',str(js)).group(0)
    share=re.search(r'\d+',str(raw)).group(0)
    return share
#获取点赞数
def get_like():
    global like
    urla='http://api.bilibili.com/x/web-interface/archive/stat?bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"like":\d+',str(js)).group(0)
    like=re.search(r'\d+',str(raw)).group(0)
    return like
#获取当前观看人数
def get_concurrent_viewers():
    global concurrent_viewers
    urla='https://api.bilibili.com/x/player/online/total?aid='
    urlb='&cid='
    urlc='&bvid='
    header={
        'Host':'api.bilibili.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie':''
    }
    js=requests.get(urla+aid+urlb+cid+urlc+bv,headers=header).text
    #数据正则筛选
    raw=re.search(r'"total":"\d+',str(js)).group(0)
    concurrent_viewers=re.search(r'\d+',str(raw)).group(0)
    if int(concurrent_viewers)>=1000:#判断当前观看人数是否大于1000，需不需要加+号
        concurrent_viewers=concurrent_viewers+'+'
        return concurrent_viewers
    return concurrent_viewers
#获取查询时间
def get_time1():
    global time1
    tm=datetime.datetime.now()
    time1=tm.strftime("%Y-%m-%d %H:%M:%S")
    return time1

#打开文件
wb=openpyxl.Workbook()
#使用的工作对象创建一张表
sheet1=wb.active
#在sheet1表中写入内容  插入内容
sheet1.append(['播放量','评论数','分享数','点赞量','当前观看人数','数据记录时间'])
for i in range(n):
    #延时
    if i>0:
        time.sleep(40+random.randint(-7,15))
    get_view();get_reply();get_share();get_like();get_concurrent_viewers();get_time1();
    print('播放量:%d'%int(view),'评论数:%d'%int(reply),'分享数:%d'%int(share),'点赞数:%d'%int(like),
          '当前观看人数:%s'%concurrent_viewers,'数据记录时间:%s'%time1,'剩余抓取次数:%d'%int(n-i-1))
    xx_info=[view,reply,share,like,concurrent_viewers,time1]
    sheet1.append(xx_info)
    wb.save('数据抓取9.xlsx')#可以自定义名字
print('数据爬取完毕')