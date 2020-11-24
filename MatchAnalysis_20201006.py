#MatchAnalysis.py
from random import random

def printIntro():
	
	print("这个程序模拟两个选手A和B的某种竞技比赛")

	print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():
	a = eval(input("请输入选手A的能力值（0-1）："))
	
	b = eval(input("请输入选手B的能力值（0-1）："))
	
	n = eval(input("模拟比赛的场次："))

	return a, b, n

def simNGames(n, proA, proB):
	
	winsA, winsB = 0, 0

	for i in range(n):
		
		scoresA, scoresB = simOneGame(proA, proB)

		if scoresA > scoresB:
			
			winsA +=1
		
		else:
			winsB +=1

	return winsA, winsB

def gameOver(a, b):
    return a == 15 or b == 15


def simOneGame(proA, proB):
	
	scoresA, scoresB = 0, 0

	serving = "A"

	while not gameOver(scoresA, scoresB):
		
		if serving == "A":
			
			if random() < proA:

				scoresA += 1

			else:
				serving = "B"

		else:

			if random() < proB:

				scoresB += 1
			
			else: 

				serving = "A"

	return scoresA, scoresB



def printSummary(winsA, winsB):
	
	n = winsA + winsB

	print("竞技分析开始，并模拟{}场比赛".format(n))

	print("选手A获胜{}场比赛， 占比{:0.1%}".format(winsA, winsA/n))

	print("选手B获胜{}场比赛，占比{: 0.1%}".format(winsB, winsB/n))

def main():

	printIntro()

	probA, probB, n = getInputs()

	winsA, winsB = simNGames(n, probA, probB)

	printSummary(winsA, winsB)

main()
