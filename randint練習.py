import random
r = random.randint(1, 100)
while True:
	num = input('請猜一個數字:')
	num = int(num)
	if num == r:
		print('你猜對了!')
		break
	elif num < r:
		print('你猜的數字比答案小')
	elif num > r:
		print('你猜的數字比答案大')
		
	
