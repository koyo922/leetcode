#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/23 下午7:33
"""
from gensim.similarities import WmdSimilarity


class Solution:
    prev = None

    def recursion(self, root):
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        L, R = root.left, root.right
        if L:
            root.right = L
            while L.right:
                L = L.right
            L.right = R
        else:
            root.right = R
        root.left = None  # REMEMBER to clear left

    def iterative(self, root):
        while root:
            # connect L's largest to R
            if root.left and root.right:
                L = root.left
                while L.right:
                    L = L.right
                L.right = root.right
            # move L to right
            if root.left:
                root.right, root.left = root.left, None
            # and ALWAYS go right-side iteratively
            root = root.right

    def flatten(self, root):
        # return self.recursion(root)
        return self.iterative(root)

WmdSimilarity
