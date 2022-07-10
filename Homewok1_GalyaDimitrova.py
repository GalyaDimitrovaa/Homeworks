#Galya Dimitrova 
#zadacha 1

def sum_of_digits(num):
    sum =0
    if num < 0:
        num = - num
    while num > 0:
        sum += num %10
        num = num // 10
    return sum

print(sum_of_digits(-27))
print(sum_of_digits(1236547))

#zadacha 2

def to_digits(n):
    
    result=[]
    
    while n>0:
        digit=n%10
        n=n//10
        result.insert(0,digit)
    return result
print(to_digits(123))

#zadacha 3

def to_number(digits):
    result=digits[0]
    for el in digits[1:]:
        result=result*10
        result=result+el
    return result
print(to_number([21,2,5,7,8,0,5]))
print(to_number([21, 2, 11]))

# zadacha 4
def fib_number(n):
    fn=[1,1]
    for i in range(2,n):
        next_num=fn[i-1]+fn[i-2]
        fn.append(next_num)
    return fn
print(fib_number(3))




