#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/19 下午6:56
"""


class Solution:

    def recursive(self, root):
        if root is None:
            return
        yield from self.recursive(root.left)
        yield from self.recursive(root.right)
        yield root.val

    def iterative(self, root):
        if not root:
            return []
        res = []
        stack = [(root, 1)]
        while stack:
            node, remain = stack.pop()
            if remain == 0:
                res.append(node.val)
            else:  # 否则，就把node放回去但是生存期减一
                stack.append((node, 0))
                if node.right:  # 注意栈是逆序，先右后左
                    stack.append((node.right, 1))
                if node.left:
                    stack.append((node.left, 1))
        return res

    def postorderTraversal(self, root):
        return list(self.recursive(root))
        # return self.iterative(root)
