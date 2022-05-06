## Exercise 7.1


def mysqrt(a):
	x = a / 2
	while True:
		# print(x)
		y = (x + a / x) / 2
		if x == y:
			return x
			break
		x = y

def test_square_root(b):
	pass #TODO

# mysqrt(18)


## Exercise 7.2


def eval_loop():
	while True:
		command = input(">")
		if command.upper() == "DONE":
			return eval(command_1)
		print(eval(command))
		command_1 = command

# print(eval_loop())


## Exercise 7.3


from math import factorial, pi
def estimate_pi():
	k = 0
	pi_ = 0
	while True:
		step = (2 * 2**0.5 / 9801) * factorial(4 * k) * (1103 + 26390 * k) / ((factorial(k))**4 * 396**(4 * k))
		pi_ = pi_ + step
		k  += 1
		if abs(pi - (1 / pi_)) < 1e-15:
			return (1 / pi_)
		# print(1 / pi_)
# print(estimate_pi())


