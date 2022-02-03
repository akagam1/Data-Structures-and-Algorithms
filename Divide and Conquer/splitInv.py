import os 

with open('numbers.txt', 'r') as f:
	input_list = [int(line.strip()) for line in f]

count = 0
def sortSplit(inp):
	global count
	if len(inp) > 1:
		left = inp[:len(inp)//2]
		right = inp[len(inp)//2:]

		if len(left) >1:
			sortSplit(left)
		if len(right) >1:
			sortSplit(right)

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
				count += len(left) - i
			k += 1 

		while i<len(left):
			inp[k] = left[i]
			i+=1
			k+=1

		while j<len(right):
			inp[k] = right[j]
			j+=1
			k+=1

	return count

print(sortSplit(input_list))