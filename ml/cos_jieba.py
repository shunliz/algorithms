#!/usr/bin/python
# -*- coding:utf-8 -*-

import jieba
import jieba.analyse
import math

def cut_word(content):
    tags = jieba.analyse.extract_tags(content, withWeight=True, topK=20)
    return tags

def merge_tag(tag1=None, tag2=None):
    v1 = []
    v2 = []
    tag_dict1 = {i[0]: i[1] for i in tag1}
    tag_dict2 = {i[0]: i[1] for i in tag2}
    merged_tag = set(tag_dict1.keys()+tag_dict2.keys())
    for i in merged_tag:
        if i in tag_dict1:
            v1.append(tag_dict1[i])
        else:
            v1.append(0)
        if i in tag_dict2:
            v2.append(tag_dict2[i])
        else:
            v2.append(0)
    return v1, v2

def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def magnitude(vector):
    return math.sqrt(dot_product(vector, vector))

def similarity(v1, v2):
    '''计算余弦相似度
    '''
    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2) + .00000000001)

# https://www.douban.com/group/topic/93410497/
content1 = u"""
            可月付 无中介 方庄地铁附近 芳城园一区单间出租
            我的房子在方庄地铁附近的芳城园一区，正规小区楼房，
            三家合住，现出租一间主卧和一间带小阳台次卧，室内家电齐全，
            冰箱，洗衣机等都有，可洗澡上网，做饭都可以，小区交通便利，四通八达，
            希望入住的是附近正常上班的朋友
            """
# https://www.douban.com/group/topic/93410328/
content2 = u"""
            可月付 无中介 方庄地铁附近 芳城园一区主卧次卧出租
            我的房子在方庄地铁附近的芳城园一区，正规小区楼房，
            三家合住，现出租一间主卧和一间带小阳台次卧，室内家电齐全，
            冰箱，洗衣机等都有，可洗澡上网，做饭都可以，小区交通便利，四通八达，
            希望入住的是附近正常上班的朋友
            """
# https://www.douban.com/group/topic/93410308/
content3 = u"""方庄地铁附近 芳城园一区次卧出租
                我的房子在方庄地铁附近的芳城园一区，正规小区楼房，
                三家合住，现出租一间主卧和一间带小阳台次卧，室内家电齐全，
                冰箱，洗衣机等都有，可洗澡上网，做饭都可以，小区交通便利，四通八达，
                希望入住的是附近正常上班的朋友
                """
# https://www.douban.com/group/topic/93381171/
content4 = u"""二环玉蜓桥旁下月27号后可入住二居
            方庄方古园一区5号楼下月27日到期出租，
            我是房主无中介费 ，新一年租6000元每月押一付三，主次卧可分开住。
            距地铁5号线蒲黄榆站5分钟路程。房屋60平正向，另有看守固定车位。
        """

tag1s = cut_word(content1)
tag2s = cut_word(content2)
tag3s = cut_word(content3)
tag4s = cut_word(content4)

v1,v2 = merge_tag(tag1s, tag2s)
v11,v13 = merge_tag(tag1s, tag3s)
v21,v24 = merge_tag(tag1s, tag4s)

s12 = similarity(v1, v2)
s13 = similarity(v11, v13)
s14 = similarity(v21, v24)

print s12
print s13
print s14