#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/30 下午4:00
"""


class Solution(object):
    def naive_recur(self, k, n):
        """
        递推，相当于f(k,n,{1,2...9})相当于下列情况的总和
        * f(k-1,n-1,{2,3...9})
        * f(k-2,n-3,{3...9})
        * f(k-3,n-6,{4...9})
        * ...
        注意，为了避开set，而又保持结果不重复
        递推时，把digits中小于等于某个值的部分排除掉，而不是仅排掉一个数
        """

        def f(k, n, digits):
            """递归调用，用k个数构成和为n的组合，可用数字集为digits"""
            if k == 0:
                pass
            elif k == 1:
                if n in digits:  # 叶结点也可能不是合法解,剩余的点也可能不止一个
                    yield [n]
            else:
                # 从 digits中排除掉前 del_d个数，同时把第del_d-1个数从n中减掉
                for del_d in range(1, len(digits) + 1):
                    # 注意是 f(k-1) 而非 f(k-del_d)
                    for r in f(k - 1, n - digits[del_d - 1], digits[del_d:]):
                        yield [digits[del_d - 1], ] + r

        return list(f(k, n, list(range(1, 10))))

    def using_cap(self, k, n):
        """ 同样递归，但是最后一个参数不用digits（可用数字集）, 而是cap(可用数字上界） """

        def f(k, n, cap):  # cap描述可用digits的上界
            if not k:  # k==0
                return [[]] * (not n)  # 如果k==0而n>=1，则无解；而k==n==0则恰好得到一个空解
            # 从子任务中减掉last，即 使用了last
            # cap自然就变成last，保证了可用的数<last
            return [comb + [last]
                    for last in range(1, cap + 1)
                    for comb in f(k - 1, n - last, last - 1)]

        return f(k, n, 9)

    def bfs(self, k, n):
        """
        循环代替递归
        每次prepend，拼接出所有的combination
        使用<当前组合的首字符的字符，来保障单调/不重复
        """
        combs = [[d] for d in range(1, 10)]  # 注意用10而非n，因为是十进制
        for _ in range(k - 1):  # 总共要做k-1轮拼接，才能得到长度为k的元素
            combs = [[d] + c
                     for c in combs
                     for d in range(1, c[0])]
        return [c for c in combs if sum(c) == n]

    def using_reduce(self, k, n):
        """ 同上，用reduce写成一行 """
        from functools import reduce
        return [c for c in
                reduce(  # 三个参数分别是 function, sequence, initial; 但是不支持具名
                    lambda combs, _: [[first] + comb
                                      for comb in combs
                                      for first in range(1, comb[0])],
                    range(k - 1),
                    [[d] for d in range(1, 10)],
                )
                if sum(c) == n]

    def combinationSum3(self, k, n):
        # return self.naive_recur(k, n)
        return self.using_cap(k, n)  # 最快
        # return self.bfs(k, n)
        # return self.using_reduce(k, n)


if __name__ == '__main__':
    res = Solution().combinationSum3(3, 9)
    print(res)
