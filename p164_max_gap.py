#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/12 下午5:45
"""
from typing import List


class Solution:
    def naive_sort(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        return max(b - a for a, b in zip(nums, nums[1:]))

    def lsd_radix_sort(self, nums):
        if len(nums) < 2:
            return 0

        max_val = max(nums)
        exp, radix = 1, 10
        while max_val // exp > 0:
            # 累加 "个位数"
            cnt = [0] * radix
            for n in nums:
                cnt[(n // exp) % 10] += 1
            # cnt的前缀和
            for i in range(1, len(cnt)):
                cnt[i] += cnt[i - 1]
            # 将数字按照LSD组织到aux中
            aux = [0] * len(nums)
            for n in reversed(nums):
                lsd = (n // exp) % 10
                cnt[lsd] -= 1
                aux[cnt[lsd]] = n
            # 拷回 nums
            nums[:] = aux
            exp *= 10
        return max(b - a for a, b in zip(nums, nums[1:]))

    def bucket_cmp(self, nums):
        if len(nums) < 2:
            return 0
        INF = float('inf')

        class Bucket:
            def __init__(self, used=False, minval=INF, maxval=-INF):
                self.used = used
                self.minval = minval
                self.maxval = maxval

            def challenge_min_max(self, val):
                self.minval = min(self.minval, val)
                self.maxval = max(self.maxval, val)

        mini, maxi = min(nums), max(nums)
        # 下述bucket_size是精心计算出来的，可以保障 max_gap >= bucket_size
        # 证明:
        # - 考虑 mini~maxi范围内的N个数, 它们之间的max_gap在什么情况下取到最小？
        #   - 在均匀分布时; 其他任何不均匀的分布都会导致更大的max_gap
        # - 因此, 就将均匀分布时的gap设置为bucket_size; 这样就能保障任何分布下都成立 max_gap >= bucket_size
        bucket_size = max((maxi - mini) // (len(nums) - 1), 1)
        bucket_num = (maxi - mini) // bucket_size + 1
        buckets = [Bucket() for _ in range(bucket_num)]

        for num in nums:
            bucket_idx = (num - mini) // bucket_size
            buckets[bucket_idx].used = True
            buckets[bucket_idx].challenge_min_max(num)

        prev_bucket_max, max_gap = mini, 0

        for bucket in buckets:
            if not bucket.used:
                continue
            max_gap = max(max_gap, bucket.minval - prev_bucket_max)
            prev_bucket_max = bucket.maxval

        return max_gap

    def maximumGap(self, nums: List[int]) -> int:
        return self.naive_sort(nums)
        # return self.lsd_radix_sort(nums)
        # return self.bucket_cmp(nums)
