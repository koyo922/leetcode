#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/14 上午12:21
"""


class Solution:
    def using_lib(self, nums, k):
        """ 直接用Counter """
        from collections import Counter
        return [val for val, time in Counter(nums).most_common(k)]  # 注意返回的是tuple

    def sort_and_cnt(self, nums, k):
        """ 用dict记录频次，排序 """
        freq = dict()
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        return [val for val, time in
                sorted(freq.items(), key=lambda tup: tup[1], reverse=True)[:k]]

    def using_heap(self, nums, k):
        """ 先统计频次，然后用大小为k的最小堆 """
        from collections import Counter
        freq = Counter(nums)

        from heapq import heappop, heappush, nlargest
        q = []
        for val, time in freq.items():
            heappush(q, (time, val))
            if len(q) > k: heappop(q)  # 堆中只保留最优的k个元素，直接del不一定能抛出最小值

        # 注意堆中元素是个tuple，其中两个元素的位置别反写了
        return [val for neg_time, val in nlargest(k, q)]

    def using_partition(self, nums, k):
        """ 用快速选择算法，就地partition """
        from typing import List, Tuple

        def k_select(data: List[Tuple[int, int]], k_big: int) -> List[Tuple[int, int]]:
            pv = data[-1][1]  # pivot value frequency
            j = 0  # 滑动下标，用来放 >pv 的元素的下标
            for i, (val, time) in enumerate(data[:-1]):
                if time >= pv:  # 注意取>=
                    # 将当前元素放到指定下标处
                    data[i], data[j] = data[j], data[i]
                    j += 1
            # 最后将pivot元素也放到下标处
            data[-1], data[j] = data[j], data[-1]

            n_put = j + 1  # 循环外的最后一次put没有+1
            if n_put == k_big:
                return data[:k_big]
            elif n_put < k_big:
                return data[:n_put] + k_select(data[n_put:], k_big - n_put)
            else:
                # 注意减1，要在>=pv的区间内找k_big个元素
                return k_select(data[:n_put - 1], k_big)

        from collections import Counter
        # 注意取val，而非元组
        return [val for val, time in k_select(list(Counter(nums).items()), k)]

    def using_bucket(self, nums, k):
        """
        由于len(nums)不大，可以用桶排序
        1. 桶下标就是频次，桶内装的是频次对应的值；
        2. 逆序下标遍历各个桶，取k个元素即可
        """
        buckets = [set() for _ in range(len(nums) + 1)]  # 频次可能为1~N，所以桶的下标范围至少要包含它，取0~N

        from collections import Counter
        for val, time in Counter(nums).items():
            buckets[time].add(val)

        return [v for vals in buckets[::-1] for v in vals][:k]

    def topKFrequent(self, nums, k):
        return self.using_lib(nums, k)
        # return self.sort_and_cnt(nums, k)
        # return self.using_heap(nums, k)
        # return self.using_partition(nums, k)
        # return self.using_bucket(nums, k)
