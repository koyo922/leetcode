#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/24 下午6:50
"""

import string


class Solution:
    def bfs_with_path(self, beginWord, endWord, wordList):
        wordList = set(wordList) - {beginWord}
        if endWord not in wordList:
            return 0  # 注意检查endWord(OJ帮我们加了) 否则可能死循环
        q, depth = [beginWord], 0
        while q:
            newRow = set()
            for n in q:
                # 当wordList很大时，遍历wordList的效率不如逐字符替换
                for c_idx in range(len(n)):
                    # 不用担心 n自己 in wordList；因为它在上一轮入队时就从wordList移除了
                    for c in string.ascii_lowercase:
                        w = n[:c_idx] + c + n[c_idx + 1:]
                        if w == endWord:  # 这句加速BFS最后一层
                            return depth + 2
                        if w in wordList:
                            newRow.add(w)
                            wordList.remove(w)  # 用过的词从 wordList中移掉
            q = newRow
            depth += 1
        return 0

    def twoway_bfs(self, beginWord, endWord, wordList):
        # sol2: two-end-BFS
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        front, back = {beginWord}, {endWord}
        dist, wordLen = 1, len(beginWord)
        while front:
            dist += 1
            new_front = set()
            for w in front:
                for i in range(wordLen):
                    for c in string.ascii_lowercase:
                        nw = w[:i] + c + w[i + 1:]
                        if nw in back:
                            return dist
                        if nw in wordList:
                            new_front.add(nw)
                            wordList.remove(nw)
            front = new_front
            if len(back) < len(front):
                front, back = back, front
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        return self.bfs_with_path(beginWord, endWord, wordList)
        # return self.twoway_bfs(beginWord, endWord, wordList)


if __name__ == '__main__':
    print(Solution().ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
    # print(Solution().ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
    # print(Solution().ladderLength('hot', 'dog', ["hot", "dog", "dot"]))
