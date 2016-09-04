from time import time
#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Problema 2
#Implementar la funcion annograms que usa el archivo WORD.LST
#para devolver anagramas de la palabra dada en el parametro word

# Returns the word's anagrams.
def annograms(word):
	words = [w.rstrip() for w in open('WORD.LST')]
	letterDictionary = counterLetters(word)
	anagrams = []
	anagrams = processWordFile(words, letterDictionary, word, anagrams)
	return "Anagramas de la palabra -{}- son {}".format(word, anagrams)

# Counts the letter's number of a word.
def counterLetters(word):
	letterDictionary = {}
	letterDictionary = {letter: letterDictionary.get(letter, 0) + 1 for letter in word}
	return letterDictionary

# Returns true if the word's length are the same, false in otherwise.
def isEqualLength(letterFile, word):
	return len(letterFile) == len(word)

def processWordFile(words, letterDictionary, word, anagrams):
	"""Process the letter's file and returns the list with
	word's anagrams"""
	for letterFile in words:
		if letterFile != word:
			if isEqualLength(letterFile, word):
				lettersFileDictorionary = counterLetters(letterFile)
				if lettersFileDictorionary == letterDictionary:
					anagrams.append(letterFile)
	return anagrams

if __name__ == "__main__":
	start_time = time()

	print annograms("train")
	print '--'
	print annograms('drive')
	print '--'
	print annograms('python')

	elapsed_time = time() - start_time

	print("Elapsed time: %0.10f seconds." % elapsed_time)
