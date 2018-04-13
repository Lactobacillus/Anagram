import os
import re
import sys
import random
import itertools

def cleanString(string):

	string = string.replace(' ', '').replace('\t','').replace('\n', '')
	regex = re.compile('[^a-zA-Z]')
	clean = regex.sub('', string)

	return clean

def makeCandidate(string):


	candidate = [''.join(c) for c in list(itertools.permutations(string))]
	string_white = string + ' ' * (len(string) - 1)
	candidate_white = list(itertools.permutations(string_white))
	candidate = candidate + candidate_white

	while True:

		cnt = len(candidate)
		candidate = [c for c in candidate if c[0] != ' ']
		candidate = [c for c in candidate if c[-1] != ' ']

		if cnt == len(candidate):

			break

	candidate = [''.join(c) for c in candidate]
	candidate = list(set([re.sub('\s\s+', ' ', c) for c in candidate]))
	candidate = [c.split(' ') for c in candidate]

	return candidate

if __name__ == '__main__':

	clean = cleanString(sys.argv[1])
	candidate = makeCandidate(clean)
	#random.shuffle(candidate)
	print('>> original string : ', sys.argv[0])
	print('>> # of candidate : ', len(candidate))
	print('>> samples : ', candidate[:3])