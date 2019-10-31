import requests
import time
import json
import pymysql
import os

conn = pymysql.connect(host="45.78.7.107", user="root", password="LiuHuan980724.", database="bing", charset="utf8")
cursor = conn.cursor()

def addslashes(s):
    d = {'"': '\\"', "'": "\\'", "\0": "\\\0", "\\": "\\\\"}
    return ''.join(d.get(c, c) for c in s)

url = "https://cn.bing.com/HPImageArchive.aspx"
http = "https://cn.bing.com"
data = {
    'format': 'js',
    'idx': 0,
    'n': 1,
    'nc': int((time.time() * 1000)),
    'pid': 'hp'
}

headers = {
    'authority': "cn.bing.com",
    'method': "GET",
    'scheme': "https",
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en,zh;q=0.9,zh-CN;q=0.8",
    'cookie': "MUID=354A50E6331566ED28CF5EE5371565E7; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=652A02AB36A24C75907C72A928513C5F&dmnchg=1; MUIDB=354A50E6331566ED28CF5EE5371565E7; SRCHUSR=DOB=20191029&T=1572412007000; _EDGE_CD=u=zh-hans; _EDGE_S=mkt=zh-cn&ui=zh-hans&SID=19DC6D3A521F6F2F0B68633F53316E9B; SNRHOP=I=&TS=; ipv6=hit=1572428982179&t=4; SRCHHPGUSR=CW=1550&CH=729&DPR=1.2395833730697632&UTC=480&WTS=63708022181; _SS=SID=19DC6D3A521F6F2F0B68633F53316E9B&HV=1572425972&bIm=_FG",
    'referer': "https://cn.bing.com/",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    'cache-control': "no-cache",
    'Postman-Token': "3c581f82-2360-41b6-a7b3-504d73651a63"
}

response = requests.get(url, headers=headers, params=data)

res_json = json.loads(response.text)
res_json = res_json['images']

r = requests.get(http + str(res_json[0]['url']), headers=headers)
img = str(res_json[0]['enddate']) + '.jpg'
if r.status_code == 200:
    with open(img, 'wb') as f:
        f.write(r.content)
res_json = res_json[0]
sql = " insert into bingImg(copyright,copyrightlink,startdate,fullstartdate, "
sql += " enddate,hsh,url,imgUrl,http,bot,drk,title,top,wp,hs) "
sql += " values ('%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,%d,'%s',%d,'%s','%s') " % \
       (str(res_json['copyright']), str(res_json['copyrightlink']), str(res_json['startdate']),
        str(res_json['fullstartdate']), str(res_json['enddate']), str(res_json['hsh']), str(res_json['url']),
        addslashes(os.getcwd()+'\\'+img), http, int(res_json['bot']), int(res_json['drk']), str(res_json['title']),
        int(res_json['top']), str(res_json['wp']), str(res_json['hs']))
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()

# region 参数
# {"images":[{"startdate":"20191028","fullstartdate":"201910281600","enddate":"20191029","url":"/th?id=OHR.EidolonHelvum_ZH-CN0881732109_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp","urlbase":"/th?id=OHR.EidolonHelvum_ZH-CN0881732109","copyright":"卡国家公园的黄毛果蝠，赞比亚 (© Nick Garbutt/Minden Pictures)","copyrightlink":"/search?q=%e9%bb%84%e6%af%9b%e6%9e%9c%e8%9d%a0&form=hpcapt&mkt=zh-cn","title":"","quiz":"/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20191028_EidolonHelvum%22&FORM=HPQUIZ","wp":true,"hsh":"1fc3d913f4e3f1f820f7a73222ee59d3","drk":1,"top":1,"bot":1,"hs":[]}],"tooltips":{"loading":"正在加载...","previous":"上一个图像","next":"下一个图像","walle":"此图片不能下载用作壁纸。","walls":"下载今日美图。仅限用作桌面壁纸。"}}
# {"images":[{"startdate":"20191029","fullstartdate":"201910291600","enddate":"20191030","url":"/th?id=OHR.CharlesNight_ZH-CN0933393880_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp","urlbase":"/th?id=OHR.CharlesNight_ZH-CN0933393880","copyright":"伏尔塔瓦河上的查理大桥，布拉格 (© Martin Moxter/Offset)","copyrightlink":"/search?q=%e6%9f%a5%e7%90%86%e5%a4%a7%e6%a1%a5&form=hpcapt&mkt=zh-cn","title":"","quiz":"/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20191029_CharlesNight%22&FORM=HPQUIZ","wp":true,"hsh":"2830fcc583673de7ef831aad1c9d85f9","drk":1,"top":1,"bot":1,"hs":[]}],"tooltips":{"loading":"Loading...","previous":"Previous image","next":"Next image","walle":"This image is not available to download as wallpaper.","walls":"Download this image. Use of this image is restricted to wallpaper only."}}
# {"images":[{"startdate":"20191028","fullstartdate":"201910281600","enddate":"20191029","url":"/th?id=OHR.EidolonHelvum_ZH-CN0881732109_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp","urlbase":"/th?id=OHR.EidolonHelvum_ZH-CN0881732109","copyright":"卡国家公园的黄毛果蝠，赞比亚 (© Nick Garbutt/Minden Pictures)","copyrightlink":"/search?q=%e9%bb%84%e6%af%9b%e6%9e%9c%e8%9d%a0&form=hpcapt&mkt=zh-cn","title":"","quiz":"/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20191028_EidolonHelvum%22&FORM=HPQUIZ","wp":true,"hsh":"1fc3d913f4e3f1f820f7a73222ee59d3","drk":1,"top":1,"bot":1,"hs":[]}],"tooltips":{"loading":"正在加载...","previous":"上一个图像","next":"下一个图像","walle":"此图片不能下载用作壁纸。","walls":"下载今日美图。仅限用作桌面壁纸。"}}


# https://cn.bing.com/HPImageArchive.aspx?
# format=js
# &idx=0
# &n=1
# &nc=1572412114162
# &pid=hp

# https://cn.bing.com/HPImageArchive.aspx?format=js&idx=1&n=1&nc=1572412115971&pid=hp
# https://cn.bing.com/HPImageArchive.aspx?format=js&idx=3&n=1&nc=1572412289290&pid=hp
# endregion
