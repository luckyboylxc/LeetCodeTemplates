# Python3 program that implements Z algorithm
# for pattern searching

def computeZ_Old(string,z):
	n = len(string)

	# [left,right] make a window which matches
	# with prefix of s
	left, right, k = 0, 0, 0
	for i in range(1, n):
		# if i>right nothing matches so we will calculate.
		# Z[i] using naive way.
		if i > right:
			left, right = i, i
			# R-L = 0 in starting, so it will start
			# checking from 0'th index. For example,
			# for "ababab" and i = 1, the value of R
			# remains 0 and Z[i] becomes 0. For string
			# "aaaaaa" and i = 1, Z[i] and R become 5
			while right < n and string[right - left] == string[right]:
				right += 1
			z[i] = right - left
			right -= 1
		else:
			# k = i- L so k corresponds to number which
			# matches in [L,R] interval.
			k = i - left
			# if Z[k] is less than remaining interval
			# then Z[i] will be equal to Z[k].
			# For example, str = "ababab", i = 3, R = 5
			# and L = 2
			if z[k] < right - i + 1:
				z[i] = z[k]
			# For example str = "aaaaaa" and i = 2,
			# R is 5, L is 0
			else:
				# else start from R and check manually
				left = i
				while right < n and string[right - left] == string[right]:
					right += 1
				z[i] = right - left
				right -= 1

# Fills Z array for given string str[]
# Z[i]: the length of the longest substring starting from string[i] which is also a prefix of string
def computeZ(s):
	n = len(s)
	z = [0]*n
	# [left,right] make a window which matches
	# with prefix of s
	lt, rt= 0, 0
	for k in range(1, n):

		# if k>right nothing matches so we will calculate.
		# Z[k] using naive way.
		if(k<=rt):
			z[k] = min(z[k-lt],rt-k+1) #core
				
		while(k+z[k] <n and s[z[k]] == s[k+z[k]]):
			lt,rt = k,k+z[k]
			z[k] +=1
	return z


# prints all occurrences of pattern
# in text using Z algo
def zSearch(text, pattern):

	# Create concatenated string "P$T"
	concat = pattern + "$" + text
	l = len(concat)

	# Construct Z array
	z = computeZ(concat)
	print(z)

	# now looping through Z array for matching condition
	for i in range(l):

		# if Z[i] (matched region) is equal to pattern
		# length we got the pattern
		if z[i] == len(pattern):
			print("Pattern found at index",
					i - len(pattern) - 1)

def main():
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    zSearch(text, pattern)
    return 0

if __name__ == "__main__":
    main()

# This code is contributed by
# sanjeev2552
