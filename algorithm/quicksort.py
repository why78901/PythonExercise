from typing import List
def quicksort(arr:List[int], left:int, right:int):
    if(left < right):
    	i = partition(arr, left, right)
    	quicksort(arr, left, i - 1)
    	quicksort(arr, i + 1, right)

def partition(arr:List[int], left:int, right:int):
	pivot = arr[left]
	while left < right:
		while(left < right and arr[right] > pivot): #从右边找一个小的
			right -= 1
		if(left < right):
			arr[left] = arr[right]
			left += 1
		while(left < right and arr[left] < pivot):  #从左边找一个大的
			left += 1
		if(left < right):
			arr[right] = arr[left]
	arr[left] = pivot
	return left

def main():
	arr = [1, 7, 3, 5, 2, 4]
	n = len(arr)
	quicksort(arr, 0, n - 1)
	for x in arr:
		print(x)

if __name__ == '__main__':
    main();