#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break-ii
题解: https://leetcode-cn.com/problems/word-break-ii/solution/dong-tai-gui-hua-hui-su-qiu-jie-ju-ti-zhi-python-d/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/12 上午8:57
"""

from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """ 现有DP判断是否有解，然后回溯DFS获得路径 """
        size = len(s)
        assert size > 0  # 题目中说非空字符串，以下 assert 一定通过

        word_set = set(wordDict)

        dp = [False for _ in range(size)]  # 状态：以 s[i] 结尾
        dp[0] = s[0] in word_set

        # 使用 r 表示右边界，可以取到; 使用 l 表示左边界，也可以取到
        for r in range(1, size):
            if s[:r + 1] in word_set:  # 如果整个单词就直接在 word_set 中，直接返回就好了
                dp[r] = True
                continue
            for l in range(r):  # 否则把单词做分割，挨个去判断
                # dp[l] 写在前面会更快一点，否则还要去切片，然后再放入 hash 表判重
                if dp[l] and s[l + 1: r + 1] in word_set:
                    dp[r] = True
                    break

        # 如果有解，才有必要回溯
        res = []
        path = deque()

        def dfs(end):  # 从后往前prepend path; 递归中及时popleft, 可以避免纯DP解的OOM
            for i in range(-1, end):
                if i == -1 or dp[i]:
                    suffix = s[i + 1:end + 1]
                    if suffix in word_set:
                        path.appendleft(suffix)
                        if i == -1:  # 抵达开头; 得到一条叶子节点的路径
                            res.append(' '.join(path))
                        else:
                            dfs(i)
                        path.popleft()

        if dp[-1]:
            dfs(size - 1)
        return res


if __name__ == '__main__':
    print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
