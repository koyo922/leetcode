#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深拷贝。 

 

示例：



输入：
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

解释：
节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。
 

提示：

你必须返回给定头的拷贝作为对克隆列表的引用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/28 下午2:39
"""
from definitions import RandomListNode as Node


class Solution(object):
    def mirror_back(self, head):
        """ 针对每个原节点建立镜像节点，拷贝的时候带上保持原始指针关系 """
        from collections import defaultdict
        cp = defaultdict(lambda: Node(0, None, None))
        cp[None] = None  # CAUTION, copy None verbatim
        h = head
        while h:
            cp[h].val = h.val
            cp[h].next = cp[h.next]  # 注意有 defaultdict，如果是第一次访问 h.next的镜像，会创建
            cp[h].random = cp[h.random]
            h = h.next
        return cp[head]

    def copy_twice(self, head):
        h = head  # 首先复制每个节点自己
        while h:
            n = Node(h.val, None, None)
            n.next = h.next
            h.next = n
            h = n.next

        h = head
        while h:  # 注意这一步只拷random，不要做太多
            if h.random:
                h.next.random = h.random.next
            h = h.next.next

        nh = dummy = Node(0, None, None)
        h = head
        while h:
            # 注意连续赋值的语义：改指针，走一步
            # 注意链式赋值是从左到右，跟C语言相反
            nh.next = nh = h.next  # 不用担心新表中的next链，会在下一次循环时被改
            h.next = h = h.next.next
        return dummy.next

    def copyRandomList(self, head):
        return self.mirror_back(head)
        # return self.copy_twice(head)
