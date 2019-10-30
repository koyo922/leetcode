#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/24 下午6:40
"""

from collections import defaultdict
import string


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        # BFS，按照条件搜索路径，沿途记下parents反向关系
        parents = defaultdict(set)
        q = [beginWord]
        while q and endWord not in parents:
            newRow = defaultdict(set)
            for w in q:
                for i in range(len(beginWord)):
                    for c in string.ascii_lowercase:
                        nw = w[:i] + c + w[i + 1:]
                        if nw in wordList and nw not in parents:
                            newRow[nw].add(w)
            q = newRow
            parents.update(newRow)

        # DFS，回溯路径
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res
