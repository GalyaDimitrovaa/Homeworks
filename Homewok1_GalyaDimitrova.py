#Galya Dimitrova 
#zadacha 1
print("primer 1")
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
print("primer 2")
def to_digits(n):
    
    result=[]
    
    while n>0:
        digit=n%10
        n=n//10
        result.insert(0,digit)
    return result
print(to_digits(123))


# zadacha 4
print("primer 4")
def fib_number(n):
    fn=[1,1]
    for i in range(2,n):
        next_num=fn[i-1]+fn[i-2]
        fn.append(next_num)
    return fn
print(fib_number(3))
print(fib_number(10))


# zadacha 5
print("primer 5")
def is_number_balanced(number):
    digits = str(number)
    digits_count = len(digits)
    sum_left = 0
    sum_right = 0

    for i in range(digits_count // 2):
        sum_left += int(digits[i])
        sum_right += int(digits[digits_count - 1 - i])
    
    if sum_left == sum_right:
        return True
    else:
        return False

print(is_number_balanced(9))
print(is_number_balanced(1238033))
print(is_number_balanced(28471))
print(is_number_balanced(4518))





