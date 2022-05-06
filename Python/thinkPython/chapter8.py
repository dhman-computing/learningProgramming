## Exercise 8.2


# print("banana".count('a'))


## Exercise 8.3


def is_palindrom(s):
	if s == s[::-1]:
		return True
	else:
		return False

# print(is_palindrom(input().upper()))


## Exercise 8.4


def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True
	else:
		return False
# Right

def any_lowercase2(s):
	for c in s:
		if 'c'.islower():
			return 'True'
	else:
		return 'False'
# True or Flase is in string datatype

def any_lowercase3(s):
	for c in s:
		flag = c.islower()
	return flag
# Flag will not be same when some uppercase come after lower case

def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower()
		return flag
# Right

def any_lowercase5(s):
	for c in s:
		if not c.islower():
			return False
	return True
#Returns false after first uppercase


## Exercise 805


def rotate_word(word, n):
	new_word = ''
	for c in word:
		d = ord(c) + n
		if c.islower():
			if d > ord('z'):
				d = d - 26
			elif d < ord('a'):
				d = d + 26
		else:
			if d > ord('Z'):
				d = d - 26
			elif d < ord('A'):
				d = d + 26
		new_word += chr(d)
	return new_word

print("Cypher : " + rotate_word(input("Word : "), int(input("n : "))))
