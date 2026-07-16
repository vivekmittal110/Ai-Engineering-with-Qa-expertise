class train:
    def __init__(self):
        pass
    def book(self, num):
        print(num,"tickets booked successfully")
    def status(self):
        print("train is on time")
    def get_fare(self,num):
        print("fare is 100 per ticket", num*100)
obj = train()
num = int(input("Enter the number of tickets: "))
obj.book(num)
obj.status()
obj.get_fare(num)