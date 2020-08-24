import random
import time

class Yacht:
    def __init__(self):
        self.dice = []
        self.holdlist = []
        self.reroll = 3
        self.checking = []
        print("게임이 시작되었습니다.")
        Yacht.rerollDice(self)

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
        if self.reroll > 0 and len(self.holdlist) != 5:
            rerollnum = 5 - len(self.holdlist)
            self.dice = self.holdlist[:]
            print("주사위 굴리는 중", end = '')
            for j in range(1,4):
                print(".", end = '')
                time.sleep(0.7)
            print("")
            for k in range(rerollnum):
                new_number = random.randint(1,6)
                print("새로 나온 주사위 값", new_number)
                self.dice.append(new_number)
                time.sleep(0.1)
            print(self.dice)
            self.dice.sort()
            self.holdlist = []
            self.reroll -= 1
        elif self.reroll < 1:
            print("남은 리롤 횟수가 부족합니다.")
        else:
            print("5개 전부 홀드한 상태에서는 리롤이 불가능합니다.")
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
        return empty

    def checkStraight(self):
        minimum = min(self.dice)
        maximum = max(self.dice)
        s_s, l_s = False, False
        switch1, switch2 = True, True
        for i in range(1,5):
            if switch1 == True and (minimum + i) in self.dice:
                if i == 3:
                    s_s = True
                if i == 4:
                    l_s = True
            else:
                switch1 = False

            if switch2 == True and (maximum - i) in self.dice:
                if i == 3:
                    s_s = True
                if i == 4:
                    l_s = True
            else:
                switch2 = False

        return s_s, l_s

    def findcombination(self):
        fc, fh, ss, ls, yc = False, False, False, False, False
        ss, ls = Yacht.checkStraight(self)
        numberList = Yacht.countNumber(self)
        if 5 in numberList:
            number = numberList.index(5) + 1
            fc, fh, yc = [number, sum(self.dice)], [number,number, sum(self.dice)], [number, 50]
        if 4 in numberList:
            number = numberList.index(4) + 1
            fc = [number, sum(self.dice)]
        if 3 in numberList and 2 in numberList:
            number1 = numberList.index(3) + 1
            nubmer2 = numberList.index(2) + 1
            fh = [number1,number2, sum(self.dice)]
        return [fc, fh, ss, ls, yc]            
        
    def printCombination(self):
        print("결과 주사위 :", self.dice)
        checklist = Yacht.findcombination(self)
        if checklist[0] != False:
            print("{0} 포카드 / 점수 : {1}".format(checklist[0][0], checklist[0][1]))
        if checklist[1] != False:
            print("{0}와 {1} 풀하우스 / 점수 : {2}".format(checklist[1][0],checklist[1][1],checklist[1][2]))
        if checklist[2] != False:
            print("스몰 스트레이트 / 점수 : 15")
        if checklist[3] != False:
            print("라지 스트레이트 / 점수 : 30")
        if checklist[4] != False:
            print("{} 야추 / 점수 : 50".format(checklist[4][0]))
        if checklist.count(False) == len(checklist):
            print("아무 조합도 존재하지 않습니다.")
            print("초이스로 돌릴시 :", sum(checklist))
        print("다시 하려면 아무 키나 입력해주세요")
        a = input() 
        Yacht.resetDice(self)

test = Yacht()

while True:
    print("0 : break")
    print("1 : checkDice")
    print("2 : resetDice")
    print("3 : rerollDice")
    print("4 : holdDice")
    print("5 : unholdDice")
    print("6 : countNumber")
    print("7 : checkStraight")
    print("8 : printCombination")
    select = int(input())
    if select == 0:
        break
    elif select == 1:
        test.checkDice()
    elif select == 2:
        test.resetDice()
    elif select == 3:
        test.rerollDice()
    elif select == 4:
        test.checkDice()
        while True:
            print("\n킵할 주사위 숫자를 입력하세요. / 종료하려면 0을 입력하세요")
            select2 = int(input())
            if select2 != 0:
                test.holdDice(select2)
            else:
                break
    elif select == 5:
        test.checkDice()
        while True:
            print("\n킵에서 해제할 주사위 숫자를 입력하세요. / 종료하려면 0을 입력하세요")
            select2 = int(input())
            if select2 != 0:
                test.unholdDice(select2)
            else:
                break
    elif select == 6:
        test.countNumber()
    
    elif select == 7:
        test.checkStraight()

    elif select == 8:
        test.printCombination()
    
    else:
        print("똑바로 입력하세오")
