#!/usr/bin/py
"""
This is for finding out sets of unique integers and also to remove duplicate integers
edit as per requirement
author : Joydeep Bhattacharjee
mailto : joydeepubuntu@gmail.com
"""
def lonelyinteger(b):
	answer = 0
	seen = set()
	uniq = []
	set_with_duplicates = []
	
	#list a set of duplicates and a unique set
	for x in b:
		if x not in seen:
			uniq.append(x)
			seen.add(x)
		else:
			set_with_duplicates.append(x)
	
# compare set with set of duplicates	
	for x in b:
		if x not in set_with_duplicates:
			answer = x
			
	return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
