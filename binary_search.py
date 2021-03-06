# params: (ls) list of numbers, (s) number to search for
def binary_search(ls=[], s=None):
	if s not in ls:
		return None
	i = 0
	while(1):
		print(ls)
		if len(ls) in [1,2]:
			if ls[0] == s:
				return i
			else:
				return i+1
			
		m = len(ls)//2
		if ls[0] <= s < ls[m]:
			ls = ls[0:m]
		else:
			ls = ls[m::]
			i+=m

# -------------------------- test --------------------------
			
a = [
	([1,2,3,4,5], 3),
	([1,2,3,4,5,6,7,8,9], 2),
	([2,4,6,8,10,12,14,16,18,20], 13),
	([0,2,4,6,8,10,12,14,16,18,20], 16),
	([-10,1,34,76,91,102,129,160,198,233,245,271,293,309,316,376,394,407,409,414,452,466,479], 407),
	([-10,1,34,76,91,102,129,160,198,233,245,271,293,309,316,376,394,407,409,414,452,466,479], 245),
	([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8], 5)
	]
for i in a:
	print("\nindex of " + str(i[1]) + " is: " + str(binary_search(ls=i[0], s=i[1])) + "\n\n----------------------\n")
input()