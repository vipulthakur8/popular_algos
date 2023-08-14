#!/usr/bin/python3

# Funtion return two values: first is sorted list and second is the number of steps taken by the 
# algorithm

def insertion_sort(arr: list) -> list:
	no_of_steps = 0  # this is will count the number of steps taken by the algorithm	
	
	for i, v in enumerate(arr):
		no_of_steps += 1

		j = i	
		no_of_steps += 1

		while j > 0 and arr[j-1] > arr[j]:
			no_of_steps += 2
	
			arr[j-1], arr[j] = arr[j], arr[j-1]	
			no_of_steps += 2

			j = j - 1
			no_of_steps += 1

	return [arr, no_of_steps]
		





arr = [5,3,0, -1, 100,-32]

if __name__ == '__main__':
	print(insertion_sort(arr))
	
