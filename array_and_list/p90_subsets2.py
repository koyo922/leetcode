#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/11 下午1:19
"""

from itertools import groupby


class Solution:

    def using_dfs(self, nums):
        """ DFS控制可用区间和前缀 """
        res = []
        nums.sort()

        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                # for each duplicate digit
                # it can only been appended exactly one pass(when idx==i)
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]])  # not idx+1

        dfs(0, [])
        return res

    def iterative(self, nums):
        """ 相同数字分组，floyd-style """
        res = [[]]
        for n, grp in groupby(sorted(nums)):  # sort before groupby
            # try extending by length of 1..len(grp)
            tmp = []
            for t in range(1, len(tuple(grp)) + 1):
                tmp.extend([(comp + ([n] * t)) for comp in res])
            res.extend(tmp)  # CAUTION do not touch res during loop
        return res

    def iterative_last(self, nums):
        """ floyd-style 但是仅当换数字时修改lastEnd，使用新区间 """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:  # 换数字时开启新的工作区间
                lastEnd = len(res)
            # 对区间内的comp，用该数字扩充
            for j in range(len(res) - lastEnd, len(res)):
                res.append(res[j] + [nums[i]])
        return res

    def subsetsWithDup(self, nums):
        return self.using_dfs(nums)
        # return self.iterative(nums)
        # return self.iterative_last(nums)


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2, 3]))
    # print(Solution().subsetsWithDup([4, 4, 4, 1, 4]))
