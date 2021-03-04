lines = ["Baby shark", "Mommy shark", "Daddy shark", "Grandma shark", "Grandpa shark", "Let's go hunt", "Run away", "Safe at last", "It's the end"]

def makeSong(Lyrics, Repetitiveness):
	Song = ""
	for i in Lyrics:
		Song += (i + (", doo") * 6 + ",\n") * Repetitiveness
	return Song

def writeToFile(ToWrite, FileName):
	f = open(FileName, 'w+')
	f.write(ToWrite)
	f.close()

if __name__ == "__main__":
	writeToFile(makeSong(lines, 100), "Song.txt")