import random
class blob:
	atk = 10
	dfnc = 10
	atkpow = 1
	hp = 50
class character:
	atk1 = 10
	atk2 = 15
	atk3 = random.randint(5,50)
	dfnc = 20
	atkpow = 5
	hp = 100


choice = input("Choose your attack:\nA) Sash\nB) Stab\nC) Pummel")
if choice == "a" or choice == "A":
		atkchoice = character(atk1)
elif choice == "b" or choice == "B":
		atkchoice = character(atk2)
elif choice == "c" or choice == "C":
		atkchoice = character(atk3)

def fightfomula (x,y,z):
	return x.hp - y.atkpow*z.atk//y.dfnc,y.atkpow*z.atk//y.dfnc
print("Character dealt "+str(fightfomula(blob,character,atkchoice)[1])+" hp. Blob is now at "+str(fightfomula(blob,character)[0])+" hp")