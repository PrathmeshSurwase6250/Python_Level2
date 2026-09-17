def factorial (n) :
    if(n == 0):
        return 1 
    else :
        return  n * factorial (n-1)

print(factorial(5))

def printhello (n) :
    if(n==0):
        return 1 
    else :
        print("hello") 
        printhello(n-1)
        
printhello(5)