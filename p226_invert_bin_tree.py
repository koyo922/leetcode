#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/4 下午5:11
"""


class Solution:

    def naive_recur(self, root):
        if root is not None:  # 注意边界情况
            root.left, root.right = self.naive_recur(root.right), self.naive_recur(root.left)
        return root

    def using_bfs(self, root):
        if root is None:
            return None  # 注意特殊情况（无人公司）
        row = [root]
        while len(row):  # 注意filter对象没有len()，所以下面的row要写成list
            for node in row:
                node.left, node.right = node.right, node.left
            row = [kid for node in row
                   for kid in (node.left, node.right)
                   if kid is not None]
        return root

    def using_dfs(self, root):
        stack = [root]
        while len(stack):
            node = stack.pop()
            if node is not None:  # 在每次pop后判断,比push时判断更简洁
                node.left, node.right = node.right, node.left
                stack.extend((node.left, node.right))
        return root

    def invertTree(self, root):
        return self.naive_recur(root)
        # return self.using_bfs(root)
        # return self.using_dfs(root)
