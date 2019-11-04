'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
'''
from string import ascii_letters

#example to test the program
#example = "https://www.reddit.com/r/learnprogramming/comments/9wn2m4/what_colorscheme_does_george_hotz_geohot_commaai/"
URL = input("Enter the desired url to be shortened ")

def isvalid(s):
	valid = False
	#create a lists of valid characters and numbers
	validnums = list(range(10))
	validchars = list(range(65, 91))
	validchars = validchars + list(range(97, 123))

	containsNums = False
	containsChars = False
	#check if the string contains both numbers and letters
	for i in validnums:
		if str(i) in s:
			containsNums = True
			break
	for i in validchars:
		if chr(i) in s:
			containsChars = True
			break
	if containsNums == True and containsChars == True:
		valid = True

	return valid


def shorten(url):
	url_split = url.split("/")
	for i in url_split:
		if len(i) == 6:
			if isvalid(i) == True:
				return i
			elif isvalid(i) == False:
				print("the url:", url,"cannot be shortened")

print(shorten(URL))

