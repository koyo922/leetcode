#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/13 下午7:32
"""

from definitions import TreeNode
from collections import deque


class CodecRecursive:

    def serialize(self, root):
        """ pre-order 递归定义; 同样用两个None包裹叶子 """

        def recur(node):
            if node is None:
                return ['null']
            return [str(node.val)] + recur(node.left) + recur(node.right)

        return ' '.join(recur(root))

    def deserialize(self, data):
        def recur(vals):  # 递归拉取value，重建pre-order
            v = vals.popleft()
            if v == 'null':
                return None
            t = TreeNode(v)
            t.left = recur(vals)
            t.right = recur(vals)
            return t

        return recur(deque(data.split()))


class Codec:

    def serialize(self, root):
        """ 直接BFS，遇到叶子用其左右None包裹 """
        if root is None:
            return ''

        q = deque([root])
        res = []
        while q:
            next_row = []
            for n in q:
                if n is None:
                    res.append('null')
                else:
                    next_row += (n.left, n.right)
                    res.append(str(n.val))  # 注意str
            q = next_row
        return ','.join(res)

    def deserialize(self, data):
        def create_node(s):
            if s is None or s == 'null':
                return None
            return TreeNode(int(s))

        if data is None or len(data) == 0:
            return None
        values = deque(data.split(','))
        head = create_node(values.popleft())  # 注意不是 values[0]
        q = deque([head])
        while q:  # 从 values中弹出节点供BFS重建
            parent = q.popleft()
            if values:
                parent.left, parent.right = map(create_node, (values.popleft(), values.popleft()))
            q += filter(None, (parent.left, parent.right))
        return head


if __name__ == '__main__':
    # c = Codec()
    c = CodecRecursive()
    t = c.serialize(TreeNode.from_json('[1,2,3,null,null,4,5]'))
    print(c.serialize(c.deserialize(t)))
