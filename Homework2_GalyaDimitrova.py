#GalyaDimitrova
#Homework 2

#zadacha 1
print("primer 1")
def sum_of_min_and_max(arr): 
    mini = arr[0]
    maxi = arr[0]
    for i in arr[1:]:
        if i < mini: 
            mini = i 
        else: 
            if i > maxi: maxi = i
    return (mini+maxi)

print(sum_of_min_and_max([1,2,3,4,5,6,8,9]))
print(sum_of_min_and_max([1]))
print(sum_of_min_and_max([-10,5,10,100]))

# zadacha 2
print("primer 2")
def sum_of_divisor (n): 
    result= 0
    for i in range(1,n+1):
        if(n%i==0):
            result+=i
    return result
            
print(sum_of_divisor(7))
print(sum_of_divisor(8))
print(sum_of_divisor(1000))
print(sum_of_divisor(1))

# zadacha 3
print("primer 3")

def  is_prime(n):
    if n> 1:  
        for i in range(2,n):  
            if (n % i) == 0:  
                return False
        return True
    else:
        return False
print(is_prime(2))
print(is_prime(1))
print(is_prime(8))
print(is_prime(11))
print(is_prime(-10))

#zadacha 4
print("primer 4")
def is_int_palindrome(n): 
    number=n
    reverse=0

    while n>0:
        result=n%10             
        reverse=reverse*10+result
        n=n//10
        
    if (number==reverse):
        return True
    else:
        return False     
print(is_int_palindrome(1))
print(is_int_palindrome(42))
print(is_int_palindrome(100001))
print(is_int_palindrome(999))
print(is_int_palindrome(123))