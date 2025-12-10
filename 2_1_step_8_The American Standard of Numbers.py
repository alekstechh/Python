'''
Standard American Convention
The program is given a natural number as input. 
Write a program that inserts commas into a given number in accordance with 
the Standard American Convention on commas in large numbers.
Example of input data 1:
1000000 
results  1:
1,000,000

Example of input data 2:
100
result 2:
100

Example of input data 3:
12345
result is 3:
12,345
'''

num=int(input())
print(f'{num:,.0f}')