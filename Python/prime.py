import time

def prime_m1(n):
	for i in range(2,n):
		if n%i == 0:
			print("not prime")
			exit
	print("1. prime")
	
def prime_m2(n):
	for i in range(2, int(n**0.5)):
		if n%i == 0:
			print("not prime")
			break
	print("2. prime")

n = int(input("n : "))
m1s = time.time()
prime_m1(n)
m1f = time.time()

print(m1f-m1s)


m2s = time.time()
prime_m2(n)
m2f = time.time()

print(m2f-m2s)
