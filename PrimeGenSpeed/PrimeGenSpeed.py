import time
import math

def prime1(n = 1):
    prime = False
    while (prime == False):
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            prime = True
            break
        n += 1
    return n

def prime2(n = 1):
    prime = False
    while (prime == False):
        for i in range(2,math.ceil(math.sqrt(n))):
            if n % i == 0:
                break
        else:
            prime = True
            break
        n += 1
    return n

def prime3(n = 1):
    prime = False
    if (n % 2 == 0):
        n += 1
    while (prime == False):
        for i in range(3,math.ceil(math.sqrt(n)), 2):
            if n % i == 0:
                break
        else:
            prime = True
            break
        n += 2
    return n

def timer(function,args = False):
    start = time.clock()
    if (args != False):
        function(args)
    else:
        function()
    end = time.clock()
    return end - start

def FunctionTimer(function, N, a_time):
    loops = int(a_time/timer(function,N))
    total = 0
    for i in range(loops):
        total += timer(function,N)
    print("Function: %s"%function.__name__)
    print("Loops = ",loops)
    print("Average time = ",total/loops)
    print("\n")

def Main(N, a_time):
    functions = [prime1,prime2,prime3]
    for i in functions:
        FunctionTimer(i, N, a_time)


if __name__ == '__main__':
    #print(prime2(int(pow(2,10))))
    Main(int(pow(2,16)), 5)
    