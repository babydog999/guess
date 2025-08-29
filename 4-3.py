# 修改要求起始數字比結束數字小

import random
start = input('請填入起始數字： ')
end = input('請填入結束數字； ')

start = int(start)
end = int(end)

if start >= end :
	print('起始值要比較小喔')
		
elif start < end :
	x = random.randint(start , end)
	z = 0
	while True :
		z += 1 # z = z +1 的快寫法
		num = input('請書輸入一個介於起始與結束中間的數字： ')
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