import sys
from mpmath import *
mp.dps = 25 # high precision but what the computer can handle

def sci_not_2(base, mult, add):
	exp = int(pow(10, pow(10, base/1000)) * mult) # run double exponential function
	return exp+add

def iterate_sci_not(mult, Max): # see what the values are for each number
	out = 10 # we know out will be 10 because this function is base 10 double exponential
	base = 0 # start at 0
	values = [[10, 0]] # start off with first value
	while out < Max:
		out = sci_not_2(base, mult, 0)
		value_now = [base, out, mult] # do this to put in the list faster
		if out not in values:	values.append(value_now)
		base += 1 # increment count
	return values

def gen_list(max_val=100000, max_mult=10): # generate a list of values up to a chosen maximum
	list_numbers = tmp_list = []
	for i in range(1, max_mult+1):
		tmp_list = iterate_sci_not(i, max_val/i) # create a temporary list item
		for I in tmp_list:
			if I not in list_numbers:	list_numbers.append(I) # if we already have it skip
	return list_numbers


def find_value(n): # check if a number shows up in the double exponential index
	l = gen_list(n**2, int(n**0.75)) # we think that this program works with going up to twice the maximum value and the square root of the number
	for i in l:
		if i[1] == n:
			return [i[0], i[2]] # [target, exponent, multiplier]
	return False # say False instead of None because of no value

# forever loop
n = 10 # starts at ten -- program needs a value at least ten because 10^10^0 is -1 and it would be hard to make it accept negative numbers (if we did we would start at 2)
while True:
	value = find_value(n)
	if value != False:
		value.append(n)
		print(value)
	n += 1 # increment counter
