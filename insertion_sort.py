#!/usr/bin/python3

import time

# Funtion return two values: first is sorted list and second time taken by the algorithm

def insertion_sort(arr: list) -> list:
	start_time = time.time() # this is the start time to of the execution
	
	for i, v in enumerate(arr):
		j = i	
		while j > 0 and arr[j-1] > arr[j]:
			arr[j-1], arr[j] = arr[j], arr[j-1]	
			j = j - 1

	end_time = time.time()  # This is the end time of the execution
	t = end_time - start_time # time taken for whole operation
	return [arr, t ]
		





arr = [5,3,0, -1, 100,-32]

if __name__ == '__main__':
	print(insertion_sort(arr))
	
