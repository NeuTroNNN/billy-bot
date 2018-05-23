import random

def get_word(string): # Function gets sentense, splits it to words and picks random word from sentence and returns it
	words = string.split()
	maximum = len(words)
	number = random.randint(0,maximum - 1)
	return words[number]