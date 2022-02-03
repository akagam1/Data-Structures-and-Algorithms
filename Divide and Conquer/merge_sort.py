###Merge Sort###

#1 split array in half
#2 solve recursively
#3 merge two arrays

def merge_sort(inp):
	if len(inp) > 1:
		left = inp[:len(inp)//2]
		right = inp[len(inp)//2:]

		if len(left) >1:
			merge_sort(left)
		if len(right) >1:
			merge_sort(right)

		i=0 #left index
		j=0 #right index
		k=0 #main index

		while i<len(left) and j<len(right):
			if left[i]<right[j]:
				inp[k] = left[i]
				i += 1
			else:
				inp[k] = right[j]
				j += 1
			k += 1 

		while i<len(left):
			inp[k] = left[i]
			i+=1
			k+=1

		while j<len(right):
			inp[k] = right[j]
			j+=1
			k+=1

	return inp

a = [7,1,5,2,6]
print(merge_sort(a))