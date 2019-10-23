#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/23 上午11:15
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from definitions import TreeNode


class Solution:

    def naive(self, preorder, inorder):
        if not preorder:
            return None
        # find root_val in inorder
        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        # recurse
        L = self.naive(preorder[1:1 + root_idx], inorder[:root_idx])
        R = self.naive(preorder[1 + root_idx:], inorder[root_idx + 1:])
        # merge
        root = TreeNode(root_val)
        root.left, root.right = L, R
        return root

    def pop_pre(self, preorder, inorder):
        # 不断抛preorder，而inorder不动，只是定位
        if inorder:
            # 这一步反复调用index()，直接跑是O(n); 可以用hash缓存好
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            # root已经抛掉了，preorder开头部分就是left
            root.left = self.pop_pre(preorder, inorder[:idx])
            # root和left子树已经处理完，相应元素都已经抛空；preorder的头部仍然直接可用
            root.right = self.pop_pre(preorder, inorder[idx + 1:])
            return root

    def till_stop(self, preorder, inorder):
        """
        O(n) using Stop-flag
        python list中popleft不如pop高效, 可以在外面reverse然后每次反着遍历
        核心技巧在于直接用stop标志位代替切分，省去了index()的O(n)代价
        """

        def build(stop):
            # 如果还没有处理到上一层认为的根
            if inorder and inorder[0] != stop:
                # 找到这一层的根
                root = TreeNode(preorder.pop(0))
                # 直接在比较完整的inorder上处理直到遇到Stop为止
                # 避免了index()操作的O(n)
                root.left = build(stop=root.val)
                inorder.pop(0)  # 当前层的左子树处理完了，抛当前层的根
                # 处理当前层的右子树；在上层的stop值之前的部分inorder可用
                root.right = build(stop=stop)
                return root

        return build(None)

    def iterative(self, preorder, inorder):
        if not preorder:
            return None
        # 根节点入栈
        root = TreeNode(preorder.pop(0))
        stack = [root]

        # 建立倒排索引，方便比较各节点在中序意义下的 大小关系
        m = {v: k for k, v in enumerate(inorder)}
        # 依次处理preorder中的后续各点
        for value in preorder:
            node = TreeNode(value)
            # 观察上一次循环的最后一句发现：栈顶相对于node是preorder意义上的左邻居
            # 而如果此时的node在中序意义上小于它，就说明node铁定是它的左孩子
            if m[value] < m[stack[-1].val]:
                stack[-1].left = node
            else:
                # 否则node在中序意义上大于栈顶
                # 说明当前元素可能位于栈顶元素或更高层元素的right位上
                # 具体是哪一层的right位呢？
                # 应当介于 p 层和 p-1 层之间；
                # 条件: 比p层靠右，同时比p-1层靠左
                while stack and m[stack[-1].val] < m[value]:
                    parent = stack.pop()
                # 循环跳出的时刻，记录的是最后一次满足条件的parent，即分析中的 p层
                #
                # 因为整体是按照preorder遍历的，而此时parent的左右孩子都已经入栈了
                # 后面处理的各节点不可能上溯到该parent, parent不再需要(已抛出栈无妨)
                parent.right = node
            stack.append(node)
        return root

    def buildTree(self, preorder, inorder):
        # return self.naive(preorder, inorder)
        # return self.pop_pre(preorder, inorder)
        return self.till_stop(preorder, inorder)
        # return self.iterative(preorder, inorder)
