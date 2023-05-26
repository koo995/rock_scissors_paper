#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""
import time
import random

moves = ['바위', '보', '가위']

class Player:
    def first_move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move=my_move
        self.their_move=their_move
        pass

class copy_Player(Player):
    def move(self):
        return self.their_move #처음에는 그냥 내야한다 그래야 learn을 할수가 있으니

class strategic_Player(Player):
    def move(self):
        if self.their_move=="바위":
            return "가위"
        elif self.their_move=="보":
            return "바위"
        elif self.their_move=="가위":
            return "보"

class simple_Player(Player):
    def move(self):    
        if self.their_move=="바위":
            return "보"
        elif self.their_move=="보":
            return "가위"
        elif self.their_move=="가위":
            return "바위"

class Human_player(Player):
    def move(self):
        while True:
            my_move=input("어느 것을 낼꺼야? 가위? 바위? 보? \n")
            if checker.digit_checker(my_move)==1:#checker에서 이게 적절한 값이면 반복문을 탈출해
                break
        return my_move#그리고 적절한 값을 전달하지

class checker:
    def digit_checker(value):
        if value not in ['가위', '바위', '보']:
            print("제대로 입력해줘!")
            time.sleep(0.5)
            return 0 #value가 저 위의 값 중에서 하나가 아니라면 0을 전달해서 계속 반복문을 돌게 하는거지 
        else: return 1 #적절하면 1을 전달해서 while문을 종료시킴
    
    # def num_checker(value):
    # 여기다 숫자인지 아닌지 체크하는 method도 만들어 볼까했는데 try except이 구문을
    # 사용하는 것도 괜찮을것 같아서 일단 보류



def beats(one, two):
    return ((one == '바위' and two == '가위') or
            (one == '가위' and two == '보') or
            (one == '보' and two == '바위'))

class Referee:
    def __init__(self, your_score=0, their_score=0):#현재 초반에 모두 점수가 0대0인것을 기본으로 설정해 줘야 하는데 거기서 막히고 있다.
        self.your_score=your_score 
        self.their_score=their_score #local variable global variable 이것에 대한 구분을 확실히 하는게 맞는듯

    def record(self, your_score, their_score):
        self.your_score += your_score
        self.their_score += their_score

    def result_show_you(self):
        if self.your_score < self.their_score:
            print(f"총 점수 너:{self.your_score} 상대:{self.their_score} 너가 졌어ㅠㅠ")
        elif self.your_score > self.their_score:
            print(f"총 점수 너:{self.your_score} 상대:{self.their_score} 너가 이겼어!")
        else:
            print(f"총 점수 너:{self.your_score} 상대:{self.their_score} 둘이 비겼구나!")


class Game:
    def __init__(self, p1, p2, referee):
        self.p1 = p1
        self.p2 = p2
        self.referee=referee #이런식이면 game.referee가 앞으로 어떤 method을 실행 하겠지. game의 referee가 무엇을 한다?

    def play_round(self,round):
        move1 = self.p1.move()
        move2 = self.p2.first_move()
        time.sleep(0.5)
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1) #여기서 순서가 바껴있네. p2기준인가
        time.sleep(0.5)
        if beats(move1,move2):
            print(f"{round+1}라운드는 너가 이겼어!")
            self.referee.record(1,0)
        elif beats(move2,move1):
            print(f"{round+1}라운드는 너가 졌어ㅠㅠ!")
            self.referee.record(0,1)
        else: 
            print("똑같은 것을 냈구나!")
            time.sleep(0.5)
            game.play_round(round)#여기 이 부분도 사실 오류가 뜨는것을 보고서 round를 추가해 준것인데

    def play_game(self):
        print("Game start!")
        while True:
            try:
                total_round=int(input("몇 판을 할꺼야?"))
            except ValueError:
                print("숫자를 제대로 입력해줘!")
            else:
                break
        for round in range(total_round):
            time.sleep(0.5)
            print(f"Round {round+1}:")
            time.sleep(0.5)
            self.play_round(round) #자 이렇게 이제 각 round을 시작하는 것이지.

        self.referee.result_show_you() #마지막에 기록했던 최종결과를 referee가 보여주도록 했는것
        print("Game over!")

if __name__ == '__main__':
    computer_players=[Player(), copy_Player(), strategic_Player(), simple_Player()]
    game = Game(Human_player(), random.choice(computer_players), Referee()) #game의 참여자로 Regeree를 추가 했지.
    print("Rock Paper Scissors Go!")
    game.play_game()









