#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。

 

示例 1：

输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。
示例 2：

输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
示例 3：

输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。
 

提示：

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-to-merge-stones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/22 上午11:56
"""
from typing import List

import functools


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        """
        首先分析是否无解:
        最开始有N堆，每次操作能消去(K-1)个堆，最终变成1个堆
        假设经历了a步操作，即 N - a*(K-1) = 1 推导出 a = (N-1) // (K-1) 是个整数
        所以 (N-1) % (K-1) == 0 即为"有解" 的充要条件

        """
        N = len(stones)
        prefix_sum = [0]  # 注意前方多余一个0的技巧
        for s in stones: prefix_sum.append(prefix_sum[-1] + s)
        INF = float('inf')

        @functools.lru_cache(maxsize=None)  # 必须用None覆盖默认的128，否则TLE
        def move(start, end, k):
            """ 将start ~ end 堆的石头 转化为k堆所需的最少成本 """
            range_len = end - start + 1
            # 题意要求每次合并K堆，无法通过整数步达到目标; 加速无解
            if (range_len - k) % (K - 1) != 0: return INF
            # 如果区段短于要求的堆数, 则无解
            if range_len < k: return INF
            # 如果区段恰好就是k堆，则无需合并
            if range_len == k: return 0

            # 如果目标是化成1堆，可以先化成K堆，最后再合并一次
            if k == 1: return move(start, end, K) + prefix_sum[end + 1] - prefix_sum[start]
            # 否则在范围 start+k-2 ~ end-1 内递归尝试分割点; 左右分别做成 k-1堆 和 1堆
            return min(move(start, m, k - 1) + move(m + 1, end, 1)
                       # 注意K-1步长加速, 因为range_len-k必须是K-1整数倍; 此处循环中k和K不变，所以range_len能按K-1增长
                       for m in range(start + k - 2, end, K - 1))

        cost = move(0, N - 1, 1)
        return cost if cost < INF else -1


if __name__ == '__main__':
    res = Solution().mergeStones([3, 5, 1, 2, 6], 3)
    print(res)
