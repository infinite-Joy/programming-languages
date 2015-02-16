"""
created on 15th Feb 2015
author: Joydeep Bhattacharjee
mailto: joydeepubuntu@gmail.com

decr: to find the maximum profit
first the index of the highest number is taken and 
profit is calculated till then puring the numbers from the list

Then the highest number from the next list is found and the process continues

solution to hackerrank stock maximise problem statement 
"""


def stock_maximise(N, price_list):
	
	roi = 0
	while price_list:
		"""
		index of the first instance of the largest valued element of price_list
		"""
		index_of_max = price_list.index(max(price_list))
		roi = roi + index_of_max * price_list[index_of_max]
		for i in range(index_of_max):
			roi = roi - price_list[i]
			
		remaining = len(price_list) - index_of_max - 1
		
		if remaining == -1:
			remaining = 0
		else:
			pass
		
		b = price_list
		del b[:-remaining]
		
		"""
		will not consider if only one remaining
		"""
		if remaining == 1 or remaining == 0:
			price_list = []
		else:
			price_list = b
		
	return roi

"""
main function computing the test cases
"""
number_of_test_cases = int(raw_input()) 
for _ in range(number_of_test_cases):
	number_of_days = int(raw_input())
	predicted_price_list = map(int,raw_input().split())
	res = stock_maximise(number_of_days,predicted_price_list)
	print res
	#print predicted_price_list
