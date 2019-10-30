#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-and-search-word-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/30 下午2:56
"""


class WordDictionary:
    EOW = '$'

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.EOW] = None  # 用尾标记来简化统一代码

    def search(self, word):
        """ BFS, beam-search """
        q = [self.root]
        for c in word + self.EOW:  # 注意结尾技巧；如果能找到，则队列最后剩个None
            nrow = []
            for n in q:
                if c in n:  # 沿着特定分支深入
                    nrow.append(n[c])
                elif c == '.':  # 沿着所有非None分支深入
                    nrow.extend(filter(None, n.values()))
            q = nrow
        return bool(q)  # 配合EOW技巧使用


if __name__ == '__main__':
    w = WordDictionary()
    print(w.addWord("bad"))
    print(w.addWord("dad"))
    print(w.addWord("mad"))
    print(w.search("pad"))
    print(w.search("bad"))
    print(w.search(".ad"))
    print(w.search("b.."))
