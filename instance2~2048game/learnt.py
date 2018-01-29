# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:53:15 2018

instanse 2: 2048 game

@author: hyh
"""
# 快速创建list，使用for遍历
test1 = [i for i in range(5)]
print(test1)
# ord()：将字母转换为ASCII码
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
print(letter_codes)

# 使用函数时，参数前面加*表示解压参数列表
def foo(bar, lee):
    print(bar, lee)
k = [1,2]
foo(*k) #输出为 1 2

# zip()将两个参数耦合为tuple
# python3中的zip输出和2不同
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)
z = list(zipped) #tuple组成的list，呵呵
print(z[0])
zipped2 = zip(a,c)
z2 = list(zipped2)
print(z) #若有多余的，不予配对

# lambda 匿名函数
y = lambda x: x+1  # y = x+1
print(y(1))

# from 实验楼
# -----------------------------------------------------------------------------
def main(stdscr):

    def init():
        #重置游戏棋盘
        return 'Game'

    def not_game(state):
        #画出 GameOver 或者 Win 的界面
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        responses = defaultdict(lambda: state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        #画出当前棋盘状态
        #读取用户输入得到action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #if 成功移动了一步:
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()


