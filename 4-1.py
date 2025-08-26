import random

x = random.randint(1 , 100)
z = 0
while True :
	z += 1 # z = z +1 的快寫法
	num = input('請猜數字： ')
	num = int(num)
	if num == x :
		print('恭喜你答對了!')
		print('這是你猜的第', z ,'次')
		break
	elif num > x :
		print('數字太大了喔!')
	elif num < x :
		print('數字太小了啦!')
	print('這是你猜的第', z ,'次')
