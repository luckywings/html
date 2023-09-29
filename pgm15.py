# def cap():
    
#     word=name.split()
#     a=[word.capitalize() for word in word]
#     b=" ".join(a)
#     print(b)
# name=input("enter the name \n")
# cap()

# def commo(a,b):
#     d=[]
#     for i in a:
#         if i in b and i  not in d:
#           d.append(i)
#     return(d) 
# a=input("enter the num\n")
# b=input("enter the num\n")
# d=commo(a,b)
# print(d)
   
   
# def factorial_iterative(n):
#     # Base case: factorial of 0 is 1
#     if n == 0:
#         return 1
#     else:
#         factorial = 1
#         for i in range(1, n + 1):
#             factorial *= i
#         return factorial
# print(factorial_iterative(5))



# def fibi():

#     next_number = num2 
#     count = 10
 
#     while count <= n:
#         print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# num1=0
# num2=1
# print(fibi(n))


# def Fibonacci(n):
 
#     while count <= n:
#         print(next_number, end=" ")
#         count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# num1=0
# num2=1
 
 

# print(Fibonacci(10))

# def fibonacciSeries(Number):
# 	if Number == 0:
# 		return 0
# 	elif Number == 1:
# 		return 1
# 	else:
# 		return fibonacciSeries(Number - 1) + fibonacciSeries(Number - 2)


# n = int(input())
# print("Fibonacci series:", end=' ')

# def Fibo(Ter):  
#     values = []  
#     First = 0  
#     Second = 1  
#     Next = First + Second  
#     values.append(First)  
#     values.append(Second)  
#     for i in range(2,Ter+1):  
#         values.append(Next)  
#         First = Second  
#         Second = Next  
#         Next = First + Second  
#     return values  
# Ter = int(input("fibonacci \n"))  
# res=Fibo(Ter)  
# print(res)  




.
