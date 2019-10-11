#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/10 下午4:33
"""
from typing import List


class Solution:
    def dfs_bt(self, nums):
        res = []

        def dfs(idx, prefix):
            """
            将当前节点加入路径 prefix；且递归的试用各个后续数字
            该算法能自动保证字典升序
            """
            res.append(prefix)
            for i in range(idx, N):
                dfs(i + 1, prefix + [nums[i]])

        nums.sort()
        N = len(nums)
        dfs(idx=0, prefix=[])
        return res

    def bit_op(self, nums):
        N = len(nums)
        res = []
        for r in range(1 << N):  # CAUTION not (2 << N)
            res.append([nums[p] for p in range(N) if (1 << p & r)])
        return res

    def iterative(self, nums):
        """ starting with empty elements, try adding each digit """
        res = [[]]
        for n in sorted(nums):
            res += [comp + [n] for comp in res]  # CAUTION +=, not =
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.dfs_bt(nums)
        # return self.bit_op(nums)
        return self.iterative(nums)


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
