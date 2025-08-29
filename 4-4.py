# 修改猜測數字必須在範圍內

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
		
		num = input('請輸入一個介於{}與{}之間的數字: '.format(start, end)) 
		num = int(num)	
		if num < start or num > end :
			print('要輸入介於' , start , '與' ,end ,'的數字喔')
		else :
			z += 1 # z = z +1 的快寫法
			if num == x :
				print('恭喜你答對了!')
				print('這是你猜的第', z ,'次')
				break
			elif num > x :
				print('數字太大了喔!')
			elif num < x :
				print('數字太小了啦!')

			print('這是你猜的第', z ,'次')
