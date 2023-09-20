# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# n=5
# for i in range(0,n):
#     for j in range(1,i+1):
#         print(j*2, end=" ")
#     print()
    
# n=5
# for i in range(0,n):
#     for j in range(1,i+1):
#         print(j*2-1, end=" ")
#     print()

# n=3
# num=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(num*2,end=" ")
#         num=num+1
#     print()
    
# n=4
# num=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(num*2-1,end=" ")
#         num=num+1
#     print()

cn=1
ls=2
r=3
for i in range(r):
    for j in range(1,ls):
        print(cn,end=" ")
        cn+=2
    print()
    ls+=2