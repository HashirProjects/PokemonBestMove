import pandas as pd
import numpy as np

class Pokemon():

	def __init__(self,name):
		self.name= name
		self.classes=[]
		self.stats=[]

	def FetchClass(self):
		#load pokeDB in
		#get column 2 and 3 for the corresponding name to get classes, and 5, 6, 7, and 8 for attack and def
		pokeDB = pd.read_csv("PokemonTypes.txt", delimiter = ",")
		pokeDB.set_index("Name", inplace = True)
		DFforName = pokeDB.loc[self.name]

		self.classes=DFforName[0:2]
		self.stats=DFforName[4:8]

class EnemyPokemon(Pokemon):

	def FindWeakness(self):
		#load weaknessDB in
		#look in weaknessDB where classes match and fetch the corresponding arrays
		#have an array of ones (one of each class) and multiply it by the arrays found in the DB
		weaknessDB = pd.read_csv("Weaknesses.txt", delimiter = ",")
		weaknessDB.set_index("Type", inplace=True)
		weaknessArray = pd.Series(np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),index= ["Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"])


		for type in self.classes:
			DFforType = weaknessDB.loc[type]
			weaknessArray = weaknessArray * DFforType

		self.weaknessArray = weaknessArray

	def CheckMoves(self,moves,friendlyStats,friendlyClasses):
		#load MovesDB in
		#find the type of each move and the power and weather it is special
		#calculate the effectiveness using the array in findWeakness and multiply by (the power of the move * Att of friendly/ Def of enemy (or special if it is a special move)) 
		#return the move that will do the most damage
		movesDB = pd.read_csv("PokemonMovesFormatted.txt", delimiter = ",")
		movesDB.set_index("Name", inplace=True)
		
		def getEffectiveness(power,friendlyAtt,enemyDef,weaknessArray,type,accuracy):
			typeMulti = weaknessArray[type]
			effectiveness = int(power) * int(typeMulti) * int(accuracy) * (friendlyAtt/enemyDef)
			return effectiveness

		movesPower=[]

		for move in moves:
			DFforMove = movesDB.loc[move]
			power = DFforMove["Power"]
			accuracy = DFforMove["Accuracy"]
			movetype = DFforMove["Type"]

			if DFforMove["Special"]:
				friendlyAtt = friendlyStats["Sp. Atk"]
				enemyDef = self.stats["Sp. Def"]
			else:
				friendlyAtt = friendlyStats["Attack"]
				enemyDef = self.stats["Defense"]
			
			movesPower.append(getEffectiveness(power,friendlyAtt,enemyDef,self.weaknessArray,movetype,accuracy))

		self.movesPower = pd.Series(movesPower, index = moves)
		print(f"the relative effectiveness of the moves you entered depending on the enemy pokemon are as follows:\n{self.movesPower}")



def FindMostEffectiveMove(moves,friendlyName,enemyName):
	
	enemyPokemon = EnemyPokemon(enemyName)
	enemyPokemon.FetchClass()
	enemyPokemon.FindWeakness()

	friendlyPokemon= Pokemon(friendlyName)
	friendlyPokemon.FetchClass()

	enemyPokemon.CheckMoves(moves,friendlyPokemon.stats,friendlyPokemon.classes)

FindMostEffectiveMove(["Pound","Mega Punch","Leech Seed"],"Ivysaur","Bulbasaur")



