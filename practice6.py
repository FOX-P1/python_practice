# notice: 콘솔로 파일을 불러올시 Q_9의 정답까지 같이 볼려면 argv를 콘솔에 추가로 넣어줄 것 !!!!!

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print("Q_1: ", cal.value)

# -------------------------------------------------
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value=100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(30)

print("Q_2: ", cal.value)

# -------------------------------------------------
print("Q_3: ")
print(all([1, 2, abs(-3)-3]))
# false
print(chr(ord('a')) == 'a')
# true

# -------------------------------------------------

print("Q_4: ", list(filter(lambda x: x > 0  , [1, -2, 3, -5, 8, -3])))

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

# print(positive([1, -2, 3, -5, 8, -3]))

# --------------------------------------------------

print("Q_5: ", int("0xea", 16))

# --------------------------------------------------

print(list(map(lambda x: x * 3, [1,2,3,4])))

def mul_3(list):
    result = []
    for i in list:
        result.append(i * 3)
    return result

print("Q_6: ", mul_3([1,2,3,4]))

# --------------------------------------------------
# list = [-8, 2, 7, 5, -3, 5, 0, 1]
# print(max(list))
# print(min(list))

def SumMaxMin(list):
    result = max(list) + min(list)
    return result

print("Q_7: ", SumMaxMin([-8, 2, 7, 5, -3, 5, 0, 1]))

# --------------------------------------------------

def Round(a):
    result = round(a, 4)
    return result

print("Q_8: ", Round(17/3))

# --------------------------------------------------

import sys

list1 = sys.argv 
# 여기서 list1에 자주 사용되는 단어인 list를 넣으면 기존에 list의
# 정의가 덮어 씌워지므로 절대 함수명으로 자주 쓰이는 단어를 변수로 선언하면 안된다.
print("sys.argvs: ", list1)

def sumArgs(list):
    result = 0
    for i in list[1:]:
        result += int(i)
    return result

print('Q_9: ', sumArgs(list1))

# --------------------------------------------------

import os

print("Q_10: ")

os.chdir("/Users/sinmingyu/Documents/python-practice/game")

viewLs = os.popen("ls")
print(viewLs.read())

# --------------------------------------------------

import glob

print("Q_11: ", glob.glob("/Users/sinmingyu/Documents/python-practice/*.py"))

# --------------------------------------------------

import time

print("Q_12: ", time.strftime('%Y/%m/%d %X', time.localtime(time.time())))

# --------------------------------------------------

import random
# print(list(range(1, 46)))
# print(random.randint(0, 3))
def random_pop():
    data = list(range(1, 46))
    i = 0
    result = []
    while i < 6:
        number = random.randint(0, 44 - i)
        i += 1
        randomNumber = data.pop(number)
        result.append(randomNumber)
    return result

print("Q_13: ", random_pop())