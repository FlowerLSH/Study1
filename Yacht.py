import random
import time

class Yacht:
    def __init__(self):
        self.dice = []
        self.holdlist = []
        self.reroll = 3
        self.checking = []
        print("게임이 시작되었습니다.")

    def holdDice(self, *hold_numbers):
        new_hold_numbers = list(hold_numbers)
        new_hold_numbers.sort()
        for i in new_hold_numbers:
            if i in self.checking:
                self.holdlist.append(i)
                self.checking.remove(i)
            else:
                print("{}는 현재 주사위 값에 남아있지 않습니다.".format(i))
        Yacht.checkDice(self)


    def unholdDice(self,*unhold_numbers):
        new_unhold_numbers = list(unhold_numbers)
        new_unhold_numbers.sort()
        for i in new_unhold_numbers:
            if i in self.holdlist:
                self.holdlist.remove(i)
                self.checking.append(i)
            else:
                print("{}는 현재 홀드되어있지 않습니다.".format(i))
        Yacht.checkDice(self)

    def checkDice(self):
        print("현재 주사위 :", self.dice)
        print("현재 홀드된 주사위 :", self.holdlist)
        print("현재 남은 리롤 횟수 :", self.reroll)
        return 0

    def rerollDice(self):
        if self.reroll > 0:
            rerollnum = 5 - len(self.holdlist)
            self.dice = self.holdlist[:]
            for j in range(1,4):
                print("주사위 굴리는 중" + ("." * j))
                time.sleep(0.7)
            for k in range(rerollnum):
                new_number = random.randint(1,6)
                print("새로 나온 주사위 값", new_number)
                self.dice.append(new_number)
                time.sleep(0.1)
            print(self.dice)
            self.dice.sort()
            self.holdlist = []
            self.reroll -= 1
        else:
            print("남은 리롤 횟수가 부족합니다.")
        Yacht.checkDice(self)
        self.checking = self.dice[:]

    def resetDice(self):
        self.dice = []
        self.holdlist = []
        self.reroll = 3
        Yacht.rerollDice(self)

    def countNumber(self):
        empty = []
        for i in range(1,7):
            empty.append(self.dice.count(i))
        print(empty)
        return empty
