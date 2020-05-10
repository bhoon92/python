# def fac(n):
#     output = 1
#     for i in range(1,n+1):
#         output *= i
#     return output
    
# fac(30)


dic={
    1: 1,
    2: 1
}

def fibo(n):
    if n in dic :
        return dic[n]
    else :
        output = fibo(n-1) + fibo(n-2)
        dic[n] = output
        return output
print(fibo(35))