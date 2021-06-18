import pandas as pd

class EnemyPokemon():

	def __init__(self,name,classes = ["",""]):

	def FetchClass(self):
		#load pokeDB in
		#get column 2 and 3 for the corresponding name

	def FindWeakness(self):
		#load weaknessDB in
		#look in weaknessDB where classes match and fetch the corresponding arrays
		#have an array of ones (one of each class) and multiply it by the arrays found in the DB

	def CheckMoves(self,moves):
		#load MovesDB in
		#find the type of each move and the power
		#calculate the effectiveness using the array in findWeakness and multiply by the power
		#return the move that will do the most damage

def FindMostEffectiveMove(moves, enemyName):
	
	enemyPokemon = EnemyPokemon(enemyName)
	enemyPokemon.FetchClass()
	enemyPokemon.FindWeakness()
	print(enemyPokemon.CheckMoves(moves))




