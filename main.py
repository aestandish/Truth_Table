# This program uses the itertools library to calculate a specific truth table and output it's values
from itertools import product  # used to output all possible truth values for p, q, r, s, and t


def logic(p, q, r, s, t):  # takes the 5 variables as input and returns the desired logical statement
    return not((p and q) or (not r and s)) or not(p or t)  # p implies q is the same as (not p) or q


values = list((product([True, False], repeat=5))) # uses itertools.product to output all possible truth values
print("  p     q     r     s     t   [(p\u2227q)\u2228(~r\u2227s)] \u2192 ~(p\u2228t)")  # creates a header for the truth table

for i in values:  # prints each possible truth value and the truth values of the logical statement
    print(i, logic(*i))  # logic(*i) prints the truth values of each variable when you apply the given logical statement






