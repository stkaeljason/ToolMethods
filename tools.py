#coding:utf-8

from collections import defaultdict, Counter


def my_count1(seq):
    """计算序列中元素出现的次数，并排序返回，seq为可迭代对象"""
    seq_dict = defaultdict(lambda: 0)
    for s in seq:
        seq_dict[s] += 1
    return sorted(seq_dict.items(), key=lambda x: x[1])


def my_count2(seq):
    print('test99999999sdlfsdf')
    print('xx')
    """计算序列中元素出现的次数，并排序返回，seq为可迭代对象,使用Counter"""
    return sorted(Counter(seq).items(), key=lambda x: x[1])
