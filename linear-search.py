
# If x is present then return its location
# else return -1

def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1
arr = ['a','b','n','g','l','d','e','s','h']

print(search(arr,'d'))
