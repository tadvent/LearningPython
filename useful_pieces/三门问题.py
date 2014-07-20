#---------------------------------------------------------------
# Name:        threeDoors
# Author:      tadvent
# Created:     28/04/2013
# Python Ver.: 3.2.3
#---------------------------------------------------------------
import os
from random import choice

##=================================
def threeDoor_v1(change):
    """三门问题第一种版本：
    主持人知道汽车在哪扇门后，每次只打开没有汽车的门
    change 参数表示选择换门还是不换门"""

    ## 假设三扇门分别编号 1, 2, 3
    doors = [1, 2, 3]
    ## 将汽车随机放入一扇门
    carDoor = choice(doors)
    ## 第一次猜
    guess1 = choice(doors)

    ## 在另外两扇没有猜的门中
    remDoors = set(doors) - {guess1}
    ## 主持人打开一扇不是车的门
    hostRemoval = choice(list(remDoors - {carDoor}))

    ## 第二次猜
    guess2 = 0
    if not change:  ## 如果选择不换门
        guess2 = guess1
    else:           ## 如果选择换门，选另外一扇
        guess2 = (remDoors - {hostRemoval}).pop()
    ## 验证结果
    return guess2 == carDoor

##=================================
def threeDoor_v2(change):
    """三门问题第二种版本：
    主持人不知道汽车在哪扇门后，每次随机打开一扇门
    如果主持人开到汽车，游戏结束，算作无效实验
    change 参数表示选择换门还是不换门"""

    ## 假设三扇门分别编号 1, 2, 3
    doors = [1, 2, 3]
    ## 将汽车随机放入一扇门
    carDoor = choice(doors)
    ## 第一次猜
    guess1 = choice(doors)

    ## 在另外两扇没有猜的门中
    remDoors = set(doors) - {guess1}
    ## 主持人随机打开一扇门
    hostRemoval = choice(list(remDoors))
    ## 如果主持人开到车，游戏结束
    if hostRemoval == carDoor:
        raise Exception()

    ## 第二次猜
    guess2 = 0
    if not change:  ## 如果选择不换门
        guess2 = guess1
    else:           ## 如果选择换门，选另外一扇
        guess2 = (remDoors - {hostRemoval}).pop()
    ## 验证结果
    return guess2 == carDoor

##=================================
def expCount(fun, change, cnt):
    validCnt = 0    ## 有效实验次数
    winCnt = 0      ## 猜对的次数
    for i in range(cnt):
        try:
            if fun(change):
                winCnt += 1
            validCnt += 1
        except:
            pass
    return winCnt, validCnt

def expOutput(fun, change, cnt):
    print("都选择{}门".format("换" if change else "不换"))
    winCnt, validCnt = expCount(fun, change, cnt)
    print("    总实验数: {:>7}".format(cnt))
    print("    有效实验: {:>7}".format(validCnt))
    print("    获胜次数: {:>7}".format(winCnt))
    print("    获胜概率: {:>7.1%}".format(winCnt / validCnt))

def main():
    allCnt = 10000
    print("三门实验版本一(主持人知情): {} 次实验".format(allCnt))
    expOutput(threeDoor_v1, False, allCnt)
    expOutput(threeDoor_v1, True, allCnt)

    print("")
    print("三门实验版本二(主持人随机选): {} 次实验".format(allCnt))
    expOutput(threeDoor_v2, False, allCnt)
    expOutput(threeDoor_v2, True, allCnt)

if __name__ == '__main__':
    main()
    os.system("pause")
