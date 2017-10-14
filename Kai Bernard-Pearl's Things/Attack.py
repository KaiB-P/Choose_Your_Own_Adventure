import random
class Blob:
	def __init__(self):
		self.atk = 10
		self.dfnc = 10
		self.atkpow = 1
		self.hp = 50

class Character:
	def __init__(self, atk,limit):
		self.atk = atk
		self.dfnc = 20
		self.atkpow = 5
		self.hp = 100
		self.limit = limit


choice = input("Choose your attack:\nA) Slash\nB) Stab\nC) Pummel")
if choice == "a" or choice == "A":
		atkchoice = Character(10,20)

elif choice == "b" or choice == "B":
		atkchoice = Character(15,10)
elif choice == "c" or choice == "C":
		atkchoice = Character(random.randint(5,50),5)

blob = Blob()

def fightfomula (x,y):
	return x.hp - y.atkpow*y.atk//x.dfnc,y.atkpow*y.atk//y.dfnc
print("Character dealt "+str(fightfomula(blob,atkchoice)[1])+" hp. Blob is now at "+str(fightfomula(blob,atkchoice)[0])+" hp")



 def atklimit(x):
