#!/usr/bin/env python
# coding: utf-8

import time

'''
author: yongzhi.zhan

跳跃表，在链表的基础上，通过概率的方式，解决链表的查询复杂度问题，其实现思路：
1.将链表划分为多层
2.下一层包含了上一层所有的数据
3.最底层包含了所有的数据
4.除了最底层，每层都随机包含下一层的部分数据
5.每层数据都是排序好的
6.除了最底层，每层都有指向下一层的指针
7.查找时，在最上层开始，当发现不在范围内，则转向下一层查找，直到最底层

这样做，可以降低了查询的复杂度，对插入的性能也没大影响，大大提高链表的性能

时间复杂度计算：


空间复杂度计算：


'''


if __name__ == '__main__':
    print "hello"