#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 19:15
# @Author  : wfo-12
# @FileName: Calculate.py
# @Software: PyCharm
# @Blog    : https://www.cnblogs.com/jvav/
# @Github  : https://github.com/Wfo-12


# 构造函数创建实例对象 需要传参 一个数组列表
# 字符串或数字，（A,J,Q,K）都可
# 外部调用 run 方法运行
# toStr 方法对输出进行格式化，默认是二维数组 [  [第一对[0], 第一对[1]],  ....  ]
# 通过 resultList 属性获取最终结果

class Calculate:

    def __init__(self, array):
        self.array = array
        self.toInt()
        self.n = len(array)
        self.listAppear = [0 for x in range(self.n)]
        self.listOfSum = []
        self.resultList = []
        self.depthOne = 1
        self.depthTwo = 1
        self.sumOfOne = 0
        self.sumOfTwo = 0

    def run(self):
        for i in range(1, self.n + 1):
            self.sumOfOne = 0
            self.depthOne = i
            self.findOne(0, 0)
        self.toStr()
        if len(self.resultList) == 0:
            self.resultList.append('没有匹配结果')

    def toInt(self):
        num = {
            'A' : 1,
            'J' : 11,
            'Q' : 12,
            'K' : 13
        }
        for i in range(len(self.array)):
            if self.array[i] in ['A', 'J', 'Q', 'K']:
                self.array[i] = num[self.array[i]]
            else:
                self.array[i] = int(self.array[i])

    def toStr(self):
        theList = [0,'A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for i in range(len(self.resultList)):
            left = ''
            right = ''
            for item in self.resultList[i][0]:
                left += theList[item] + ', '
            left = left[:-2]
            for item in self.resultList[i][1]:
                right += theList[item] + ', '
            right = right[:-2]
            self.resultList[i] = [left, right]

    def findOne(self, i, x):
        if x == self.depthOne:
            for j in range(1, self.n + 1 - self.depthOne):
                self.sumOfTwo = 0
                self.depthTwo = j
                self.findTwo(0, 0)
            return
        while i < self.n:
            if self.listAppear[i] == 0:
                self.listAppear[i] = 1
                self.sumOfOne += self.array[i]
                self.findOne(i + 1, x + 1)
                self.listAppear[i] = 0
                self.sumOfOne -= self.array[i]
            i += 1

    def findTwo(self, i, x):
        if x == self.depthTwo:
            if self.sumOfOne == self.sumOfTwo:
                try:
                    self.listOfSum.index(self.sumOfOne)
                except:
                    self.listOfSum.append(self.sumOfOne)
                    resultX = []
                    resultY = []
                    for j in range(self.n):
                        if self.listAppear[j] == 1:
                            resultX.append(self.array[j])
                        elif self.listAppear[j] == 2:
                            resultY.append(self.array[j])
                    self.resultList.append([resultX, resultY])
            return
        while i < self.n:
            if self.listAppear[i] == 0:
                self.listAppear[i] = 2
                self.sumOfTwo += self.array[i]
                self.findTwo(i + 1, x + 1)
                self.listAppear[i] = 0
                self.sumOfTwo -= self.array[i]
            i += 1

if __name__ == '__main__':
    list1 = ['A', 2, 3, 4, 5, 6]
    test = Calculate(list1)
    test.run()
    print(test.resultList)

