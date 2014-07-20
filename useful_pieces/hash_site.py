import os

char_table = {
		"q":1, "Q":1, "a":1, "A":1, "z":1, "Z":1,
		"w":2, "W":2, "s":2, "S":2, "x":2, "X":2,
		"e":3, "E":3, "d":3, "D":3, "c":3, "C":3,
		"r":4, "R":4, "f":4, "F":4, "v":4, "V":4,
		"t":5, "T":5, "g":5, "G":5, "b":5, "B":5,
		"y":6, "Y":6, "h":6, "H":6, "n":6, "N":6,
		"u":7, "U":7, "j":7, "J":7, "m":7, "M":7,
		"i":8, "I":8, "k":8, "K":8,
		"o":9, "O":9, "l":9, "L":9,
		"p":0, "P":0,
		"1":1, "2":2, "3":3, "4":4, "5":5,
		"6":6, "7":7, "8":8, "9":9, "0":0
		}

def jiami(name):
	name_str = str(name)
	ret = ""
	last = 0
	for ch in name_str:
		last ^= char_table[ch]
		# ret.append(str(last))
		ret += str(last)
	return ret

if __name__ == "__main__":
	site_name = input("Site Name: ")
	print(jiami(site_name)[-4:])
	os.system("pause")


