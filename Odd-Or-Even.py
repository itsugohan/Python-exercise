'''
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one 
number to divide by (check). If check divides evenly into num, tell that
to the user. If not, print a different appropriate message.
'''

num = int(input("请输入一个数字"))
if (num % 2) == 0:
   print("even")
else:
   print("odd")
if (num % 4) == 0:
   print("num能被4整除")
else:
   print('num不能被4整除')
check = int(input("请输入另一个数字"))
if (num % check) == 0:
   print("num能被check整除")
else:
   print("num不能被check整除")
