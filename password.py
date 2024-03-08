x = 3

password = input('請輸入密碼')

while password != 'a123456' and x > 0:
		print ('你還有', x,'次機會')
		x = x-1
		password = input('請輸入密碼')
if password == 'a123456':
	print('pass!')
	
else:
	print('login fail')


	
