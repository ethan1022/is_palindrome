
# -*- coding: utf-8 -*-

def is_palindrome(n):
	reverseN = str(n)[::-1] #This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
	return int(reverseN) == n

output = filter(is_palindrome, range(1, 1000))
print('1-1000:', list(output))

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
	print('測試成功')
else:
	print('測試失敗')

