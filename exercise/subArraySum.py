# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

# Output:
# For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= Ai <= 1010

# Example:
# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10
# Output:
# 2 4
# 1 5

# Explanation :
# Testcase1: sum of elements from 2nd position to 4th position is 12
# Testcase2: sum of elements from 1st position to 5th position is 15

inArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = 15
low = 0
subtotal = inArray[low]


for high in range(low+1, len(inArray)):
    if subtotal == s:
        break
    subtotal = subtotal + inArray[high]
    print(f"sum {low+1} .. {high+1} = {subtotal}")
    while subtotal > s:
        subtotal = subtotal - inArray[low]
        low += 1
        print(f"sum {low+1} .. {high+1} = {subtotal}")

if subtotal == s:
    print(f"sum of elements from position {low+1} to {high} is {s}")
else:
    print("-1")

print("a", 2)
