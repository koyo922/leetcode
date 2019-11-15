#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/15 下午12:13
"""
from heapq import heappush, heappushpop


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        # 注意加入新的数之后，要把最小的大数(large堆的堆顶，注意large是小顶堆)转入 small堆
        # 或者把最大的小数转入 large堆
        # 否则（直接把新数写入两个堆）会丢失信息, 破坏循环不变式
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]


if __name__ == '__main__':
    obj = MedianFinder()
    print(None)
    print(obj.addNum(-1))
    print(obj.findMedian())
    print(obj.addNum(-2))
    print(obj.findMedian())
    print(obj.addNum(-3))
    print(obj.findMedian())
    print(obj.addNum(-4))
    print(obj.findMedian())
    print(obj.addNum(-5))
    print(obj.findMedian())
