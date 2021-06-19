import pandas as pd

class Pokemon():

	def __init__(self,name):
		self.name= name
		self.classes=[]
		self.stats=[]

	def FetchClass(self):
		#load pokeDB in
		#get column 2 and 3 for the corresponding name to get classes, and 5, 6, 7, and 8 for attack and def
		pokeDB = pd.read_csv("PokemonTypes.txt", delimiter = ",")
		DFforName = pokeDB[pokeDB.Name == self.name]
		print(DFforName)

		for i in range(2,4):
			self.classes.append(DFforName.iat[0,i])
		
		for i in range(4,8):
			self.stats.append(DFforName.iat[0,i])

class EnemyPokemon(Pokemon):

	def FindWeakness(self):
		pass
		#load weaknessDB in
		#look in weaknessDB where classes match and fetch the corresponding arrays
		#have an array of ones (one of each class) and multiply it by the arrays found in the DB

	def CheckMoves(self,moves,friendlyStats,friendlyClasses):
		pass
		#load MovesDB in
		#find the type of each move and the power and weather it is special
		#calculate the effectiveness using the array in findWeakness and multiply by (the power of the move * Att of friendly/ Def of enemy (or special if it is a special move)) 
		#return the move that will do the most damage



def FindMostEffectiveMove(moves,friendlyName,enemyName):
	
	enemyPokemon = EnemyPokemon(enemyName)
	enemyPokemon.FetchClass()
	enemyPokemon.FindWeakness()

	friendlyPokemon= Pokemon(friendlyName)
	friendlyPokemon.FetchClass()

	print(enemyPokemon.CheckMoves(moves,friendlyPokemon.stats,friendlyPokemon.classes))

pokemon=Pokemon("Ivysaur")
pokemon.FetchClass()
print(pokemon.classes, pokemon.stats)




