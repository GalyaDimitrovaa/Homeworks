class Bill:
    def __init__(self, amount):
        self.amount=amount
        if not (isinstance(amount,int)):
            raise TypeError
        if amount<0:
            raise ValueError
   
    def __str__(self):
        return "A " + str(self.amount) + " $ bill"
    
    def __repr__(self):
        return "A " + str(self.amount) + " $ bill" 
    
    def __int__(self) :
        return self.amount
  
    def __eq__(self,other):
        return self.amount==other.amount
   
    def __hash__(self):
       return hash(self.amount)


a=Bill(10)
b=Bill(5)
c=Bill(10)

# d=Bill("Hello its me")
# e=Bill(-15)
   
# print(a) 
# print(str(a))
# print(int(a))
# print(a==b)
# print(hash(b))
# print(d)

money_holder = {}  
money_holder[a] = 1   
if c in money_holder:     
    money_holder[c] += 1  
print(money_holder) 

class BillBatch:
    def __init__(self,list_of_bills):
        self.list_of_bills=list_of_bills

    def __len__(self):
        return len(self.list_of_bills)
    
    def total(self):
        sum=0
        for elem in self:
            sum=sum+elem
        return sum
        

    def __getitem__(self,index):
        return self.list_of_bills[index]



values = [10, 20, 50, 100] 
   
print("The number of Bills in the batch: ", len(values)) #len = 4

bills=[Bill(value) for value in values]
batch=BillBatch(bills)
for bill in batch:
    print(bill)

print("The number of Bills in the batch: ", len(values)) 
batch=BillBatch(values)
print("Total bills: ", batch.total())


# print(values[0])   # values[0]=10, values[1]=20 and etc








