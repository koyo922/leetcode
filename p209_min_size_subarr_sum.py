#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/27 上午9:29
"""
from typing import List


class Solution:
    def brute_force(self, s: int, nums: List[int]) -> int:
        """ 【TLE】O(n^2) 遍历所有合法的子数组，挑出最短的 """
        N = len(nums)

        prefix = [0]
        for n in nums:  # 多一个前缀和的技巧
            prefix.append(prefix[-1] + n)

        res = INF = float('inf')
        for i in range(N):
            for j in range(i + 0, N):  # 注意长度允许为1
                if prefix[j + 1] - prefix[i] >= s:
                    res = min(res, j - i + 1)
                    break  # 及时跳出
        return 0 if res == INF else res

    def using_bisect(self, s: int, nums: List[int]) -> int:
        """ O(NlogN) 找j的时候可以直接二分，因为prefix是单增的 """
        N = len(nums)
        prefix = [0]
        for n in nums:  # 多一个前缀和的技巧
            prefix.append(prefix[-1] + n)
        res = INF = float('inf')

        from bisect import bisect_left  # 注意是尽可能靠左的（尽量短的子数组）
        # prefix[j+1] - prefix[i] >= s 所以 prefix[j+1] >= s+prefix[i]
        for i in range(N):
            j = bisect_left(prefix, s + prefix[i], lo=i) - 1  # 注意二分出来的是j+1
            if j + 1 == N + 1: continue  # len(prefix)==N+1, 所以查到末尾表示越界了
            res = min(res, j - i + 1)

        return 0 if res == INF else res

    def double_pointers(self, s: int, nums: List[int]) -> int:
        """ O(N) 滑动区间，右界线性单增；左界在range_sum>=s时才收缩 """
        N, i, range_sum = len(nums), 0, 0
        res = INF = float('inf')
        for j, n in enumerate(nums):
            range_sum += n
            while range_sum >= s:
                res = min(res, j - i + 1)  # 每次收缩i都要刷新一遍最优解，以免遗漏
                range_sum -= nums[i]
                i += 1
        return 0 if res == INF else res

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # return self.brute_force(s, nums)
        # return self.using_bisect(s, nums)
        return self.double_pointers(s, nums)
