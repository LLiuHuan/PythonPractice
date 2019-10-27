# -*- coding:utf-8 -*-
import requests
import time
import json
import execjs
import re


def get_signature(userId):
    """
    解密 signature
    :param userId:
    :return:
    """
    with open('signature.js', 'r') as f:
        js = execjs.compile(f.read(), cwd=r'C:\Users\18455\AppData\Roaming\npm\node_modules')
        signs = js.call('get_signature', userId)
        return signs


url = "https://www.iesdouyin.com/web/api/v2/aweme/post"

# data中 下面两个是可变的
# 'max_cursor': '0',
# '_signature': 'CvQkehAZV0fiLgYHmMRlHAr0JG',

# 如果换视频 下面三个也需要换了
# 'sec_uid': 'MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA',
# '_signature': 'CvQkehAZV0fiLgYHmMRlHAr0JG',
# 'dytk': '5b68a25b4dac4940285aa00d8abec34e'

data = {
    'sec_uid': 'MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA',
    'count': '21',
    'max_cursor': '0',
    'aid': '1128',
    '_signature': 'CvQkehAZV0fiLgYHmMRlHAr0JG',
    # '_signature': get_signature(78612868824),
    'dytk': '5b68a25b4dac4940285aa00d8abec34e'
}

print(get_signature(78612868824))

# headers中 下列是可变的
# 'Postman-Token': "7a89180c-769b-4bc8-9b90-4aa7689f7a11"

headers = {
    'authority': "www.iesdouyin.com",
    'method': "GET",
    'path': "/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAywJ4T_WcOFGjZ-pmCR2VmI7u4LWghclHEfgiS75UXpI&count=21&max_cursor=0&aid=1128&_signature=JTtUiBAZeJbN4Xb14KgmLiU7VJ&dytk=bf3bd94f63d5dd85cfabea97ca33734d",
    'scheme': "https",
    'accept': "application/json",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en,zh;q=0.9,zh-CN;q=0.8",
    'cookie': "_ga=GA1.2.430553677.1572184021; _gid=GA1.2.2098165153.1572184021",
    'referer': "https://www.iesdouyin.com/share/user/78612868824?sec_uid=MS4wLjABAAAAywJ4T_WcOFGjZ-pmCR2VmI7u4LWghclHEfgiS75UXpI&timestamp=1572186907&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_app_name=douyin",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    'x-requested-with': "XMLHttpRequest",
    'cache-control': "no-cache",
    'Postman-Token': "7a89180c-769b-4bc8-9b90-4aa7689f7a11"
}

fileHeaders = {
    'cookie': "_ga=GA1.2.430553677.1572184021; _gid=GA1.2.2098165153.1572184021",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}


def get_response():
    """
    获取每次请求的数据
    :param max_cursor:
    :return:
    """

    while not time.sleep(1):
        response = requests.get(url, params=data, headers=headers)
        if len(response.text) > 60:
            str_json = response.text.encode('utf-8').decode('utf-8')
            return str_json

def startDownload():
    while not time.sleep(1):
        str_json = get_response()
        jjson = json.loads(str_json)
        try:
            for aweme in jjson['aweme_list']:
                r = requests.get(aweme['video']['download_addr']['url_list'][0], stream=True, headers=fileHeaders)
                fileName = re.findall(r"(.+?)#", aweme['desc'])
                if r.status_code != 200:
                    print("【%s】 下载失败！" % fileName)
                    continue
                if len(fileName) > 1:
                    fileName = str(fileName[0])
                else:
                    fileName = str(aweme['aweme_id'])
                with open(fileName + '.mp4', "wb") as mp4:

                    r = r.content
                    mp4.write(r)
                print("【%s】 下载成功！" % fileName)
        except Exception as e:
            print(e)

        if not jjson['has_more']:
            print('已全部下载完毕，关闭下载！')
            break
        data['max_cursor'] = jjson['max_cursor']

if __name__ == '__main__':
    startDownload()

# region 无用

# https://www.iesdouyin.com/share/user/496625282450126?sec_uid=MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA&timestamp=1568014650&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_app_name=douyin
# https://www.iesdouyin.com/share/user/78612868824?sec_uid=MS4wLjABAAAAywJ4T_WcOFGjZ-pmCR2VmI7u4LWghclHEfgiS75UXpI&timestamp=1572186907&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_app_name=douyin

# https://www.iesdouyin.com/web/api/v2/aweme/post/?
# sec_uid=MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA
# &count=21
# &max_cursor=0
# &aid=1128
# &_signature=-jOLtBAap5AS6anJFw2FDPozi6
# &dytk=5b68a25b4dac4940285aa00d8abec34e


# https://www.iesdouyin.com/web/api/v2/aweme/post/?
# sec_uid=MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA
# &count=21
# &max_cursor=1569578204000
# &aid=1128&_signature=-jOLtBAap5AS6anJFw2FDPozi6
# &dytk=5b68a25b4dac4940285aa00d8abec34e


# https://www.iesdouyin.com/web/api/v2/aweme/post/?
# sec_uid=MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA
# &count=21
# &max_cursor=1567245750000
# &aid=1128&_signature=-jOLtBAap5AS6anJFw2FDPozi6
# &dytk=5b68a25b4dac4940285aa00d8abec34e


# https://www.iesdouyin.com/web/api/v2/aweme/post/?
# sec_uid=MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA
# &count=21&max_cursor=1559043203000
# &aid=1128
# &_signature=-jOLtBAap5AS6anJFw2FDPozi6
# &dytk=5b68a25b4dac4940285aa00d8abec34e


# _signature
# _bytedAcrawler = require("douyin_falcon:node_modules/byted-acrawler/dist/runtime")
# __M
# douyin_falcon:node_modules/byted-acrawler/dist/runtime


# https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA&count=21&max_cursor=0&aid=1128&_signature=CvQkehAZV0fiLgYHmMRlHAr0JG&dytk=5b68a25b4dac4940285aa00d8abec34e
# 1569578204000
# https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA&count=21&max_cursor=1569578204000&aid=1128&_signature=CvQkehAZV0fiLgYHmMRlHAr0JG&dytk=5b68a25b4dac4940285aa00d8
# 1567245750000
# https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAOyyOOiqBYiPo3uIHuTrqE6OeAY2NJ3dIRBA63mn4fFA&count=21&max_cursor=1567245750000&aid=1128&_signature=CvQkehAZV0fiLgYHmMRlHAr0JG&dytk=5b68a25b4dac4940285aa00d8
# 1565434536000


# for chunk in r.iter_content(chunk_size=1024 * 1024):
#     if chunk:
#         mp4.write(chunk)
# enregion
