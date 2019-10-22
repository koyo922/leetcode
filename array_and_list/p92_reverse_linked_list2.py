#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/22 下午5:40
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from array_and_list.p86_partition_list import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:  # 注意边界情况
            return head

        # 注意从头开始翻转的情况 if m==1? add dummy
        pre = dummy = ListNode(0)
        cur = dummy.next = head

        # find the element before/equals m
        for _ in range(m - 1):
            pre, cur = cur, cur.next

        # reverse LinkedList of length n-m-1
        nh, h = None, cur
        for _ in range(n - m):
            h.next, nh, h = nh, h, h.next

        # 从后往前逆序拼接各个片段
        cur.next = h.next  # 此时的cur仍指向样例中2的位置, h指向4
        h.next = nh  # nh指向3
        pre.next = h  # pre还在1

        return dummy.next
