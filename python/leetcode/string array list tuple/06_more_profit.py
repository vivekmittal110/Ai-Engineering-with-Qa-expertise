prices = [7,1,5,3,6,4]
profit = 0


for i in range (1,len(prices)):
    for j in range(0,i):
        min_price = prices[j]
    cur_profit = prices[i]-min_price
    # print(cur_profit)
    if cur_profit>0:
        profit+=cur_profit
        
print(profit)