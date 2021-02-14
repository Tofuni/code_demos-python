# params: (ls) a list of numbers, (s) number of partitions
def partition_list(ls=[], s=1):
	r, i, n, z = [], 0, len(ls)//s, len(ls)%s
	for a in range(0,s):
		r.append(ls[i:i+n])
		i+=n
		if z != 0: #catch remaining items in case ls doesn't cleanly divide by s
			r[a].append(ls[i])
			z, i = z-1, i+1
	return r

# ------------------------- test -------------------------

a = [
	([83, 66, 38, 92, 10, 17, 45, 58, 19, 18, 89, 3, 9, 57, 15, 13, 55, 15, 30, 27, 23, 13, 75, 42, 50, 
	52, 89, 92, 90, 28, 28, 17, 51, 31, 70, 76, 31, 20, 17, 8, 11, 97, 90, 26, 16, 87, 84, 73, 28, 5, 38, 
	1, 80, 27, 53, 61, 25, 20, 27, 64, 92, 28, 58, 7, 91, 90, 23, 29, 3, 74, 21, 36, 84, 8, 23, 4, 16, 88, 
	96, 5, 6, 57, 24, 26, 43, 94, 80, 63, 96, 58, 16, 87, 12, 84, 55, 69, 25, 37, 6, 95], 5), 
	#100 elements
	
	([47, 80, 60, 54, 71, 95, 60, 14, 36, 90, 48, 28, 52, 81, 23, 48, 6, 48, 73, 56, 43, 4, 16, 20, 51, 94, 
	19, 17, 17, 28, 32, 10, 54, 11, 79, 85, 70, 39, 8, 45, 37, 67, 13, 73, 23, 20, 50, 76, 58, 85, 71, 52, 
	38, 17, 95, 20, 2, 79, 59, 12, 62, 13, 20, 84, 64, 71, 63, 48, 48, 22, 26, 95, 36, 86, 15, 85, 27, 32, 
	40, 31, 7, 36, 16, 53, 4, 93, 26, 7, 25, 4, 36, 38, 50, 69, 54, 43, 38, 33, 15, 2, 43, 60, 17, 29, 
	51], 10), 
	#105 elements
	
	([28, 18, 44, 2, 78, 90, 6, 52, 18, 54, 38, 36, 92, 72, 99, 38, 34, 5, 85, 49, 47, 62, 2, 17, 43, 97,
	66, 69, 83, 91, 63, 39, 83, 4, 19, 11, 12, 36, 8, 15, 57, 73, 27, 22, 12, 12, 4, 100, 25, 86, 42, 14, 
	28, 65, 91, 100, 13, 72, 41, 67, 69, 57, 21, 89, 77, 47, 67, 45, 2, 92, 91, 67, 20, 16, 85, 75, 5, 49, 
	96, 90, 79, 42, 44, 29, 80, 78, 51, 3, 69, 43, 61, 59, 30, 79, 94, 23, 51, 11, 37, 47, 100, 102], 20)
	#102 elements
	]
for i in a:
	s = partition_list(ls=i[0], s=i[1])
	print("\n" + str(i[0]) + "\n")
	for x in s:
		print(str(x))
	print("\n-------------------------\n")
input()