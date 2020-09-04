import numpy as np
import math
import cmath

def gn(n):
    return np.array(range(1,n))

def sn(n):
    result = 0
    for h in c(n):
        if(h == 0):
            continue
        result = result + r1(h)
    return result

def estimatetop(g,n): #with 4.5
    return 1/(n-1)*math.pow(1+(sn(n)),len(g))

def estimatetop2(g,n): #with 4.3, 4.7
   return 2**(len(g)+1)*math.log(n+1)**len(g)/n

def r1m(h):
    result = 1
    for x in h:
        result = result*r1(x)
    return result

def c(n):
    return np.array(range(int(-n/2),int(n/2+1)))

def r1(h):
    return max(1,abs(h))


def phi(x,n):   #book version
    with open("phi_werte","r") as values:
        for line in values:
            temparray = line.split(",")
            if (temparray[0]== str(x)) & (temparray[1]==str(n)):
                return complex(temparray[2])
  
    result = 0
    for h in c(n):
        result = result + ((1/r1(h))*np.exp(2*math.pi*complex(0,1)*h*x))
    
    values = open("phi_werte","a")
    values.write(str(x))
    values.write(",")
    values.write(str(n))
    values.write(",")
    values.write(str(result))
    values.write("\n")
    return result

def phichecker():
    with open("phi_werte","r") as file:
        d = dict()
        for line in file:
            temparray = line.split(",")
            if not(temparray[2] in d):
                d[temparray[2]]=0
            d[temparray[2]]+=1
    
    print(d.values())
    print(len(d.values()))

def phi2(x,n):   #with -1 inside the sum (not anymore, now just phi without saving values)
    result = 0
    for h in c(n):
        result = result + ((1/r1(h))*np.exp(2*math.pi*complex(0,1)*h*x))
    return result

def phi3(x,n):   #with alpha = 2 
    result = 0
    for h in c(n):
        result = result + ((1/(r1(h)*r1(h)))*np.exp(2*math.pi*complex(0,1)*h*x))
    return result

def fom(g,n): #currently running with phi2
    result = 0
    for i in np.array(range(0,n)):
        helper = 1 
        for x in g:
            helper = helper * phi2(i*x/n,n)
        result = result + helper
    merit =  result/n-1
    if merit.imag < 10e-15:
        return merit.real
    return "Error, figure of merit has a complex part"

def fom2(g,n):
    result = 0
    for i in np.array(range(0,n)):
        helper = 1 
        for x in g:
            helper = helper * phi2(i*x/n,n)
        result = result + helper
    return (result/n)-1

def fom3(g,n):
    result = 0
    for i in np.array(range(0,n)):
        helper = 1 
        for x in g:
            helper = helper * phi3(i*x/n,n)
        result = result + helper
    return (result/n)-1

#phichecker()
#for n in [181,251,317,397,463,557,619,701,787,863,953,1009,1151,1747,2083]:
 #   print("N: ",n,",fom: ", fom([1, 282, 197, 377, 233, 55, 73, 263, 408, 46], n),",max value: ",estimatetop2([1, 282, 197, 377, 233, 55, 73, 263, 408, 46],n))

#for n in [109,   113,   127,   131,   137,   139,   149,   151,   157,   163,   167,   173,   179,   181,
 # 191,   193,   197,   199,   211]:
  #  print("N: ",n,",fom: ", fom([1, 282, 197, 377, 233, 55, 73, 263, 408, 46], n),",max value: ",estimatetop2([1, 282, 197, 377, 233, 55, 73, 263, 408, 46],n))

print("normal: ",fom([1, 282, 197, 377, 233, 55, 73, 263, 408, 46] , 1009))
#print("alpha = 2: ",fom3([1,390,265,180,242,491,450,347,77,332], 1009))