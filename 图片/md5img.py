# -*- coding: utf-8 -*-
# coding: utf-8

"""
20191025
今天这个主要是为了图床打基础
目前计划是图床的文件识别使用md5加密进行校验
使用这个小栗子
试验一下两个不同名字的图片
使用md5加密后值是否相同

目前证明 只有相同大小的才可以
但是也够用了
没必要做的太严谨 如果需要的话
未来考虑使用图像识别 或其他算法实现
但是目前只使用md5加密就已经足够了
毕竟只是自己用
😄😄😄
其实这个最主要的作用就是记性不好 总忘 给自己加个限制 哈哈哈
"""

import hashlib

with open('logo.png', 'rb') as f:
    md5 = hashlib.md5()
    md5.update(f.read())
    print(md5.hexdigest())
    print(md5.digest())

with open('640.png', 'rb') as f:
    md5 = hashlib.md5()
    md5.update(f.read())
    print(md5.hexdigest())
    print(md5.digest())

with open('大象logo.jpg', 'rb') as f:
    md5 = hashlib.md5()
    md5.update(f.read())
    print(md5.hexdigest())
    print(md5.digest())

with open('大象logo.png', 'rb') as f:
    md5 = hashlib.md5()
    md5.update(f.read())
    print(md5.hexdigest())
    print(md5.digest())