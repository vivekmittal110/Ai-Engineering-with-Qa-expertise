# x = 1232321
# rev = 0
# lenght = (len(str(x)))
# for i in range (1,lenght+1):
#     rev *= 10
#     rev += x%10
#     x//=10
# print(x)
# if x == rev:
#     print("True")
# else:
#     pass
x = str(x)
return x == x[::-1]