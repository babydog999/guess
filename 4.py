import random

x = random.randint(1 , 100)
while True :
	num = input('請猜數字： ')
	num = int(num)
	if num == x :
		print('恭喜你答對了!')
		break
	elif num > x :
		print('數字太大了喔!')
	elif num < x :
		print('數字太小了啦!')

