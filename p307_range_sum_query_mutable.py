#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

示例:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
说明:

数组仅可以在 update 函数下进行修改。
你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/22 上午10:44
"""


class SegTreeNode:
    """
    线段树，每个节点上记录一个区间的起止点、左右子树指针、求和
    更新的时候，只需要递归的更新一条到叶节点的路径，然后沿途回溯更新整条路径
    查找的时候，根据待查的区段做分治或者减治
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

    @staticmethod
    def buildSegTree(nums, l=0, r=None):
        if l > r:
            return None
        root = SegTreeNode(l, r)
        if l == r:  # 注意递归边界条件
            root.total = nums[l]
        else:  # 先分治下去，然后抛栈回来的时候再根据左右子树统计
            mid = (l + r) // 2
            root.left = SegTreeNode.buildSegTree(nums, l, mid)
            root.right = SegTreeNode.buildSegTree(nums, mid + 1, r)
            root.total = root.left.total + root.right.total
        return root

    def update(self, i, val):
        if self.start == self.end:  # 找到了确切的那个叶子
            self.total = val
            return val

        mid = (self.start + self.end) // 2
        if i <= mid:  # 往一边减治
            self.left.update(i, val)
        else:
            self.right.update(i, val)
        # 抛栈回来时再根据左右子树刷新区间统计
        self.total = self.left.total + self.right.total
        return self.total

    def sumRange(self, i, j):
        if self.start == i and self.end == j:  # 完美匹配的区间
            return self.total
        # 如果待求区段落在某一边了，就减治；否则左右同时分治
        mid = (self.start + self.end) // 2
        if j <= mid:
            return self.left.sumRange(i, j)
        elif i >= mid + 1:
            return self.right.sumRange(i, j)
        else:
            return self.left.sumRange(i, mid) + self.right.sumRange(mid + 1, j)


class NumArray:
    def __init__(self, nums):
        self.root = SegTreeNode.buildSegTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        self.root.update(i, val)

    def sumRange(self, i, j):
        return self.root.sumRange(i, j)


if __name__ == '__main__':
    na = NumArray([1, 3, 5])
    print(na.sumRange(0, 2))
    print(na.update(1, 2))
    print(na.sumRange(0, 2))
