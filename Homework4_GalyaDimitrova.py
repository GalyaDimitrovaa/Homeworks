# zad 1 2 3 4 5
numb=set()
for_list=[4,5,66]
for_list2={33,0,88}
for i in range(0,50):
    numb.add(i)
    numb.update(for_list,for_list2) #zad2
ll=[j for j in numb] #zad3
ll1={j:j*2 for j in numb} #zad4
print (numb)
print (ll)
print (ll1)

for idx, val in enumerate(ll1):   #zad5
   if idx%2==1:
      print(idx,val)


#zad 6
print("primer 6")
def func(some_list, num):
    sum=0
    for i in range (len(some_list)):
        for j in range(i+1,len(some_list)):
            sum=some_list[i]+some_list[j]
            if sum==num:
                print(some_list[i], some_list[j])
some_list=[1,2,3,4,5,6,7,8,9]
num=9
func(some_list,num)