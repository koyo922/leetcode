#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/30 下午3:18
"""


class Solution:

    def recursive_partition_kth(self, nums, k):
        """ 递归写法导致 OOM """
        pivot = nums[0]
        left, mid, right = [], [], []
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n == pivot:
                mid.append(n)
            else:
                right.append(n)

        if k <= len(right):
            return self.findKthLargest(right, k)
        elif k <= len(right) + len(mid):
            return mid[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(mid))

    def inplace_twoway(self, nums, k):
        """
        始终是在原始的nums上做partition, 不断地找target_pos
        直到将第K大的元素放到target_pos上
        """
        target_pos = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while lo <= hi:  # 这里不怕写 lo<=hi 因为即使len(nums)==1, 最底下的return也是对的
            # 注意双向partition写法: 以nums[lo]为轴, 切分nums[lo..hi]区段
            i, j = lo + 1, hi
            pivot = nums[lo]
            while True:
                while i < hi and nums[i] <= pivot:  # CAUTION: i < hi
                    i += 1
                while j > lo and nums[j] >= pivot:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            nums[j], nums[lo] = nums[lo], nums[j]
            # 结束状态: nums[j] == pivot, j==相应的下标，左侧<=pivot，右侧>=pivot
            # 不同于荷兰国旗:
            #   - 荷兰国旗的`end`恰好是 最后一个 等于pivot元素的下标
            #   - 双向切分的`j`只是 任意一个 ...

            # 如果刚才的pivot下标恰好是在target_pos上
            if target_pos == j:
                break
            elif target_pos < j:  # 否则去左边找
                hi = j - 1
            else:
                lo = j + 1
        return nums[target_pos]

    def inplace_holland(self, nums, k):
        """ 非递归版本，不改 nums, 就地荷兰国旗,减少GC """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:  # 注意 <= 的写法
            pivot = nums[lo]
            begin, cur, end = lo, lo, hi
            while cur <= end:
                if nums[cur] > pivot:
                    nums[cur], nums[end] = nums[end], nums[cur]
                    end -= 1
                elif nums[cur] == pivot:
                    cur += 1
                else:
                    nums[cur], nums[begin] = nums[begin], nums[cur]
                    begin += 1
                    cur += 1
            # 荷兰国旗结束状态: lo ... begin ... (cur=end+1) ... hi
            # 按照跟pivot的相对大小分为三段: lo~begin-1 ... begin~end ... end+1~hi

            if k <= hi - end:
                lo = end + 1
            elif k <= hi - begin + 1:
                return pivot
            else:
                k -= hi - begin + 1
                hi = begin - 1  # 注意这两句顺序
        raise ValueError('should not be here')

    def findKthLargest(self, nums, k):
        # return self.recursive_partition_kth(nums, k)
        # return self.inplace_twoway(nums, k)
        return self.inplace_holland(nums, k)


if __name__ == '__main__':
    # res = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
    res = Solution().findKthLargest([99, 99], 1)
    # res = Solution().findKthLargest([98], 1)
    # res = Solution().findKthLargest([1, 2, 3, 4, 5, 6], 1)
    # res = Solution().findKthLargest([7, 6, 5, 4, 3, 2, 1], 2)
    # res = Solution().findKthLargest([7, 6, 5, 9, 3, 2, 1], 2)
    # res = Solution().findKthLargest([2, 1], 2)
    print(res)
