#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/22 下午5:59
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recursive(self, root: TreeNode):
        if not root:
            return []
        return self.recursive(root.left) + [root.val] + self.recursive(root.right)

    def iterative(self, root):
        res, stack = [], []
        while stack or root:
            while root:  # 左到底
                stack.append(root)
                root = root.left
            # 弹出并使用该叶子
            t = stack.pop()
            res.append(t.val)
            # 迭代尝试其右子树
            root = t.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.recursive(root)
        # return self.iterative(root)
