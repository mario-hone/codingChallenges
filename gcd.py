import time

# If m and n are integers and n\=0, then divisor(m,n)
# iff m is a divisor of n.

def divisor(m,n):
    return n%m == 0

# Divisor not zero
def divisorNZ(c,n):
    return n%c == 0

# This function finds the gcd by testing candidates,
# starting with 1 and working up.
def gcd1(m, n):
    count = 0
    for c in range(1, m + 1):  # c = 1,...,m.
        count += 1
        if divisor(c, m) and divisor(c, n):
            greatestSoFar = c
    return (greatestSoFar, count)


# this one starts with m and works down.

def gcd2(m,n):
  for i in range(0,m): # i = 0,...,m-1
	c = m-i            # c for "candidate"
	if divisor(c,m) and divisor(c,n): return c


# start with the smaller number and work down
def gcd3(m,n):
  k = min(m,n)
  for i in range(0,k): # i = 0,...,min(m,n)-1
	c = k-i               	# c for "candidate"
	if divisor(c,m) and divisor(c,n): return c


# This one uses Eulid's algorithm

# if y!=0 then  x%y = - (x//y)*y, where x//y is the
# greatest integer less than or equal to x/y.

# If m and n are integers, at least one of which is
# not 0, then gcd4(m,n) is the gcd of m and n.

def gcd4(m,n):
  if m<n: (m,n) = (n,m)
  # |=  m>=n
  while True:
    r = m % n
    if r==0: return n
    (m,n) = (n,r)

t0 = time.time()
print(gcd2(4500, 5000))
t1 = time.time()
print(t1-t0)

