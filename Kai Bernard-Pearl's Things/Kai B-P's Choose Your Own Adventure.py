import random
class Question():
	def __init__(self,question,choices):
		self.question = question
	def get_question(self):
		return (self.question)
query = Question("You wake up in a forest and see a wild boar heading towards you. You can:\na) Run\nb) Climb a tree\nc) Pick up a branch and fight it\nd) Stay still and hope it doesn't notice you\nType answer here:")
print (query.get_question())

def probability(x):
	def chance():
		if random.randint(1,100) <= x:
			return True 
		else:
			return False
'''health = 100
items = []

print("Health = " + str(health))

q = "do you like cheese: A) Yes B) No C) Maybe D) So"
o = ["yes","no","maybe","so"]
def play(question,option):
	answer = input(question)
	if answer == "A" or "a":
		return options[0]
play(q,o)
	
		print(items)
		play()

play()

def rand_function(gain,loss,succeede,fail,probability):
	global health
	if random.randint(1,100) <= probability:
		health += gain
		print(succeed)
		return questionrun1
	else:
		health -= loss	
		print(fail)
		return questionrun2

questionrun2= ["You are lying on the groud and the boar is standing over you"]
questionrun1 = ["You escape from the boar and stop at a river. You can:\na)Follow the river upstream\nb)Follow the river downstream\nc)Cross the river\nType answer here:", {'a': 'option1', 'b': 'option2', 'c': 'option3'}]
question1 = ["You wake up in a forest and see a wild boar heading towards you. You can:\na) Run\nb) Climb a tree\nc) Pick up a branch and fight it\nd) Stay still and hope it doesn't notice you\nType answer here:", {'a': rand_function(0,10,"You outran the boar","The boar caught and trambled you,"70), 'b': 'option2', 'c': 'option3', 'd': 'option4'}]
game_on = True
question = question1
while game_on:
	answer = input(question[0])
	question = question[1][answer]
	print()
	print("Health="+str(health))
	for i in range(50):
		print()

blah = {}
blah.uppend ('asdf') '''

