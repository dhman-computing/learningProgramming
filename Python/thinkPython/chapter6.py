## Exercise 6.2


def ack(m, n):
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack(m - 1, 1)
	elif m > 0 and n > 0:
		return ack(m - 1, ack(m, n - 1))

# print(ack(3, 4))


## Exercise 6.3


def is_palindrom(s):
	if len(s) <= 1:
		return True

	if first(s) == last(s):
		return is_palindrom(middle(s))
	else:
		return False

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

# print(is_palindrom("redivider"))


## Exercise 6.4


def is_power(a, b):
	# print(f"a : {a}\nb : {b}")
	if a == 1:
		return True
	elif a % b != 0:
		return False
	elif a % b == 0:
		return is_power(a/b, b)

# print(is_power(1000000000, 10))


## Exercise 6.5


def gcd(a, b):
	# print(f"a : {a}\nb : {b}")
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

print(gcd(50,15864546465465456454878887875))