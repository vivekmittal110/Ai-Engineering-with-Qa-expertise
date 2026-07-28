# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

n = 234

product = 1
sum = 0

for i in range (1,len(str(n))+1):
    product*=n%10
    sum+=n%10
    n//=10
print(product-sum)