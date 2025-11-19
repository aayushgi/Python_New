#function to sum all elements of a list
def sum_list(list):
	total=0
	for i in list:
		total=total+i
	return total
print(sum_list([10, 20, 30, 40]))