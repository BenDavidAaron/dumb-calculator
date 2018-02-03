'''
This is a script that generates N number of test cases.
each case consists of three comma-delimited values on a line.
the first value is the sum (result) of the two following 
randomly generated integers (features) on each line.
Format:
sum,int_1,int_2\n
'''

from random import randint
import sys
from tqdm import tqdm

def add_two_random_ints():
	int_1 = randint(0,9)
	int_2 = randint(0,9)
	return "%s,%s,%s\n" % (int_1 + int_2, int_1, int_2)

number_cases = abs(int(sys.argv[1]))

with open("cases.csv", "w") as f:
	f.writelines('A,Q1,Q2\n') 
	for _ in tqdm(range(number_cases)):
		f.writelines(add_two_random_ints())