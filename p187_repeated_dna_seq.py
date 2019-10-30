#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab number
"""
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。

 

示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Authors: qianweishuo<qzy922@gmail.com>
Date:    2019/10/29 下午12:06
"""


class Solution:
    def py_hash(self, s):
        from collections import Counter
        ctr = Counter(''.join(tup) for tup in
                      zip(*[s[start:] for start in range(10)]))
        return [k for k, v in ctr.items() if v > 1]

    def rolling_hash(self, s):
        # sol2: 自定义滚动hash
        if len(s) < 10: return []
        res = []
        # hash到int类型；省空间; 每个字符最多占用两个bit
        char2int = dict(zip('ATCG', range(4)))

        # 两级缓存: 出现过一次 / 大于一次的hash值
        s1, s2 = set(), set()
        mask = (1 << 20) - 1
        # 开头的前10个字符，算出其hash
        h = 0
        for i in range(10):
            h = (h << 2) | char2int[s[i]]
        s1.add(h)  # 截止目前，它遇到过一次

        # rolling hash
        for i in range(10, len(s)):
            # 常数时间算好滚动hash
            h = ((h << 2) & mask) | char2int[s[i]]
            if h in s2:  # 见过至少两次的，已经处理过了
                continue
            elif h in s1:
                res.append(s[i - 9:i + 1])
                s2.add(h)
            else:
                s1.add(h)
        return res

    def findRepeatedDnaSequences(self, s):
        return self.py_hash(s)
        # return self.rolling_hash(s)


if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
