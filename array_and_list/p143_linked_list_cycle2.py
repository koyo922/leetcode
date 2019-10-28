#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。


 

进阶：
你是否可以不用额外空间解决此题？

在真实的面试中遇到过这道题？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/28 下午3:00
"""


class Solution(object):
    def detectCycle(self, head):
        """
        https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation
        H: head到entry
        D: entry到pos
        L: 圈长

        ----- 现在假设都是从起点开始的（代码里起步错位一步是为了好写，逻辑一样）
        slow所走长度: H+D
        fast所走长度: 2(H+D)
        后者减去前者应该是整数圈: 2(H+D) - (H+D) = nL  ∴ H+D=nL ∴ H=nL-D
        所以将slow拉回原点, fast保持在第一次相遇点
        此时，再分别走H步，则
            - slow到达的位置相当于 "全局坐标" 的 0+H=H点，即entry点
            - fast的 "圈内坐标" 是 (D + H) = D+(nL-D) = nL ; 刚好也到entry
        """
        try:
            # 注意两个不要放在同一起点
            fast, slow = head.next, head  # 另外，可能就是个空表；所以这一行也要放try里面
            while fast != slow:  # 否则这个循环就不会开始
                fast, slow = fast.next.next, slow.next
        except AttributeError:  # 可能没有环，一直找到表尾的None
            return None

        fast = fast.next  # 之前让起点错了一位（导致提前相遇上）；现在修复
        slow = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
