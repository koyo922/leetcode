#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/23 上午11:39
"""
from definitions import TreeNode


class Solution(object):

    def naive(self, inorder, postorder):
        if inorder:  # CAUTION
            root = TreeNode(postorder.pop())
            i = inorder.index(root.val)
            root.left = self.buildTree(inorder[:i], postorder[:i])
            root.right = self.buildTree(inorder[i + 1:], postorder[i:])
            return root

    def iterative(self, inorder, postorder):
        if not postorder:  # CAUTION
            return None
        m = {v: k for k, v in enumerate(inorder)}
        root = TreeNode(postorder.pop())
        stack = [root]
        for v in postorder[::-1]:  # 注意逆序
            n = TreeNode(v)  # CAUTION
            if m[v] > m[stack[-1].val]:
                stack[-1].right = n
            else:
                while stack and m[v] < m[stack[-1].val]:
                    parent = stack.pop()
                parent.left = n
            stack.append(n)
        return root

    def buildTree(self, inorder, postorder):
        # return self.naive(inorder,postorder)
        return self.iterative(inorder, postorder)


if __name__ == '__main__':
    tree = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print()
