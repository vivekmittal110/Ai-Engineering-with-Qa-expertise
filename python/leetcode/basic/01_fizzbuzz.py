# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

n = int(input("Enter input : "))
a = []
for i in range (1,n+1):
    if i % 15 == 0:
        a.append("fizzbuzz")
    elif i%3 == 0:
        a.append("fizz")
    elif i%5 ==0:
        a.append("buzz")
    else:
        a.append(i)

print(a)
