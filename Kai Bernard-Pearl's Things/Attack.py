import random


class Blob:
    def __init__(self):
        self.atk = 10
        self.dfnc = 10
        self.atkpow = 1
        self.hp = 50


class Character:
    def __init__(self, atk, limit):
        self.atk = atk
        self.dfnc = 20
        self.atkpow = 5
        self.hp = 100
        self.limit = limit
        atack1 = Atk(5,90,15,"weapon","none")
        atack2 = Atk(10,75,7,"magic","burn")
        atack3 = Atk(random.randint(5,40),60,5)

class Atk:
    def __init__(self,dmg,hitmiss,atklmt,atktype,atkeffect):
        self.dmg = dmg
        self.hitmiss = hitmiss
        self.limit = atklmt
        self.type = atktype
        self.stateffect = atkeffect

atkcounter1 = 0
atkcounter2 = 0
atkcounter3 = 0
atkspermatch = 0

choice = input("Choose your attack:\nA) Slash\nB) Burning Hands (not a d&d reference)\nC) Pummel")
if choice == "a" or choice == "A":
    atkchoice = Character(10, 20)
    atkcounter1 = atkcounter1 + 1
    atkspermatch = atkspermatch + 1
elif choice == "b" or choice == "B":
    atkchoice = Character(15, 10)
    atkcounter2 = atkcounter2 + 1
    atkspermatch = atkspermatch + 1
elif choice == "c" or choice == "C":
    atkchoice = Character(random.randint(5, 25), 5)
    atkcounter3 = atkcounter3 + 1
    atkspermatch = atkspermatch + 1

blob = Blob()


def fightfomula(x, y):
    return x.hp - y.atkpow * y.atk // x.dfnc, y.atkpow * y.atk // y.dfnc


print("Character dealt " + str(fightfomula(blob, atkchoice)[1]) + " hp. Blob is now at " + str(
    fightfomula(blob, atkchoice)[0]) + " hp")


def atklimit(x, y, z):
    if x == atkcounter1:
