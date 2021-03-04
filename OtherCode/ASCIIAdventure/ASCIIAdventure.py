"""
A little messy but this was just a quick thing to do for WBD
"""

Houses = {
	"A" : {"Funny" : 2, "Intelligent" : 5},
	"B" : {"Funny" : 1, "Intelligent" : 7},
	"C" : {"Funny" : 6, "Intelligent" : 1},
	"D" : {"Funny" : 9, "Intelligent" : 1},
}

Questions = {
	"[0 - 10] Are you funny?" : {"Funny" : 10, "Intelligent" : 2},
	"[0 - 10] Are you intelligent?" : {"Funny" : -5, "Intelligent" : 2},
}

class Person:
	def __init__(self):
		self.Stats = {"Funny" : 0, "Intelligent" : 0}

	def AskQuestions(self):
		for a,_ in Questions.items():
			score = int(input(a))
			for c,d in Questions[a].items():
				scoreChange = d * score
				self.Stats[c] += scoreChange

	def FindHouse(self):
		Distance = {}
		for a,b in Houses.items():
			Distance[a] = 0
			for _,d in Houses[a].items():
				for _,f in self.Stats.items():
					Distance[a] += abs(d-f)

		Lowest = None
		House = None
		for a,b in Distance.items():
			if Lowest == None:
				Lowest = b
				House = a
			else:
				if b < Lowest:
					Lowest = b
					House = a

		return House

if __name__ == "__main__":
	try:
		foo = Person()
		foo.AskQuestions()
		print(foo.FindHouse())
	except:
		print("An error has occured")