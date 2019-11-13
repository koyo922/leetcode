#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/11/12 上午8:24
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        给定一个字符串和单词字典，将字符串切分成若干个单词，使每个单词都在字典中。判断是否可以成功切分
        假设字符串s[0 : n-1]可以成功切分成若干个单词，那么一定存在一个i使得s[0 : i-1]可以成功切分成若干个单词，同时s[i : n-1]在字典中存在，可以采用动态规划的思想求解
        令dp[i]表示s[0 : i-1]是否可以成功切分成若干单词组合，最终要求解的是dp[n]。
        那么每求一个dp[i]使，就在i前面寻找是否存在一个j使得dp[j]为真且s[j : i-1]在字典中
        """
        if len(wordDict) == 0:
            return False
        word_set = set(wordDict)
        max_word_len = max(len(w) for w in wordDict)
        dp = [False] * len(s) + [True]  # dp[i]:= s[0 ~ i]是否可切分; 构造-1作为"空串可分"
        for i in range(len(s)):
            for j in range(i, max(i - max_word_len, -1), -1):  # 注意下界，右开区间
                if dp[j - 1] and s[j:i + 1] in word_set:
                    dp[i] = True
                    break
        return dp[-2]


if __name__ == '__main__':
    Solution().wordBreak('leetcode', ['leet', 'code'])
