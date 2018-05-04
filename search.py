import os
import sys
import urllib
import http.cookiejar
from bs4 import BeautifulSoup

oxfordURL = 'https://en.oxforddictionaries.com/definition/'

def wordInDict(word):

	soup = BeautifulSoup(urllib.request.urlopen(oxfordURL + word), 'lxml')
	soup = soup.find(class_ = 'entryWrapper')

	if isinstance(soup.find(class_ = 'no-exact-matches'), type(None)):

		return True

	else:

		return False

def sentenceInDict(sentence):

	if all([wordInDict(word) for word in sentence]):

		return True

	else:

		return False

if __name__ == '__main__':

	print('asdf           : ', wordInDict('asdf'))
	print('dinner         : ', wordInDict('dinner'))
	print('fox in a road  : ', sentenceInDict(['fox', 'in', 'a', 'road']))
	print('asdf qwer      : ', sentenceInDict(['asdf', 'qwer']))