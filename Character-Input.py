import datetime

name = input('请输入您的名字')

print(name)

age = int(input("请输入您的年龄"))

print(age)

now = datetime.datetime.now()
this_year = now.year

print(100 - age + this_year)
