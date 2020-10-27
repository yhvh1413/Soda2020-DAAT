#coding=utf-8
import re, string
import csv
import re
import datetime

def k_cal(num):
    if t0 >= 10 :
        if int(x1) != num and int(x2) != num and int(x3) != num and int(x4) != num and int(x5) != num and int(x6) != num and int(t1) != num and int(t2) != num and int(l) != num and int(s) != num and True:
            return num  
        else:
            num = 0
    else:
        if int(x1) != num and int(x2) != num and int(x3) != num and int(x4) != num and int(x5) != num and int(x6) != num and int(t1) != num and int(l) != num and int(s) != num:
            return num  
        else:
            num = 0

def k(num):
    if k_cal(num) != None:
        return k_cal(num)
    else:
        return 0

def num_cnt(x): 
    if  x in num_all:
        return x
    else :
        pass

  
date_dict = "/Users/Soda复赛daat/data/day_dict.sql"

now = datetime.datetime.now()
a = now.strftime('%Y-%m-%d%H:%M:%S')
n_hour = a[10:12]
n_minute = a[13:15]
n_second = a[16:18]

h1 = n_hour[0:1]
h2 = n_hour[1:2]
mn1 = n_minute[0:1]
mn2 = n_minute[1:2]
s1 = n_second[0:1]
s2 = n_second[1:2]

t0 = int(h1) + int(h2) + int(mn1) + int(mn2) + int(s1) + int(s2)
t = str(t0)
t1 = t[0:1]    
if t0 >= 10 :
    t2 = t[1:2]    
else:
    t2 = 0

if t0 >= 10 : 
    l0 = int(t1) + int(t2)
    l01 = str(l0)
    if l0 >= 10:
        l1 = l01[0:1]
        l2 = l01[1:2]
        l3 = int(l1) + int(l2)
        lf = str(l3)
    else:
        lf = l01
else:
    lf = int(t1)    

l = lf   
s0 = int(mn1) + int(mn2)
s = str(s0)   
x1 = h1   
x2 = h2   
x3 = mn1   
x4 = mn2   
x5 = s1   
x6 = s2   
k1 = k(1)   
k2 = k(2)   
k3 = k(3)   
k4 = k(4)   
k5 = k(5)   
k6 = k(6)   
k7 = k(7)   
k8 = k(8)   
k9 = k(9)   

new = [] 
results = [] 

fr = open(date_dict, "r")
dict1_all = eval(fr.read())
fr.close()        

name = str("n") + str(x1) + str("x")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x1) + str("x_1")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x1) + str("x_0")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x2) + str("x")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x2) + str("x_1")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x2) + str("x_0")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x3) + str("x")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x3) + str("x_1")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x3) + str("x_0")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x4) + str("x")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x4) + str("x_1")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x4) + str("x_0")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x5) + str("x")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x5) + str("x_1")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x5) + str("x_0")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x6) + str("x")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x6) + str("x_1")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(x6) + str("x_0")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())


num_all = {int(x1), int(x2), int(x3), int(x4), int(x5), int(x6), int(t1), int(t2), int(l), int(s)}

if num_cnt(1) == 1 and num_cnt(2) == 2 and num_cnt(3) == 3:
    name = "1-2-3"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(1) == 1 and num_cnt(4) == 4 and num_cnt(7) ==7:
    name = "1-4-7"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(1) == 1 and num_cnt(5) == 5 and num_cnt(9) ==9:
    name = "1-5-9"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(2) == 2 and num_cnt(4) ==4:
    name = "2-4"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(2) == 2 and num_cnt(6) == 6:
    name = "2-6"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(2) == 2 and num_cnt(5) == 5 and num_cnt(8) == 8:
    name = "2-5-8"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(3) == 3 and num_cnt(5) == 5 and num_cnt(7) == 7:
    name = "3-5-7"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(3) == 3 and num_cnt(6) == 6 and num_cnt(9) == 9:
    name = "3-6-9"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(4) == 4 and num_cnt(5) == 5 and num_cnt(6) == 6:
    name = "4-5-6"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(4) == 4 and num_cnt(8) == 8:
    name = "4-8"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(6) == 6 and num_cnt(8) == 8:
    name = "6-8"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())
            # print(name)
else:
    pass
        
if num_cnt(7) == 7 and num_cnt(8) == 8 and num_cnt(9) == 9:
    name = "7-8-9"
    for value in dict1_all:
    #print (value)
        if name == value["name"]:
            new.append(value.copy())  
            # print(name)
else:
    pass

name = str("n") + str(k1) + str("k")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(k2) + str("k")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(k3) + str("k")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(k4) + str("k")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(k5) + str("k")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(k6) + str("k")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(k7) + str("k")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(k8) + str("k")
for value in dict1_all:
#print (value)
    if name == value["name"]:
        new.append(value.copy())

name = str("n") + str(k9) + str("k")
for value in dict1_all:
# print (value)
    if name == value["name"]:
        new.append(value.copy())

n = sum(item["n"] for item in new)
p = sum(item["p"] for item in new)
nu1 = sum(item["nu1"] for item in new)
nu2 = sum(item["nu2"] for item in new)
nu3 = sum(item["nu3"] for item in new)
nu4 = sum(item["nu4"] for item in new)
nu5 = sum(item["nu5"] for item in new)
nu6 = sum(item["nu6"] for item in new)
f = sum(item["f"] for item in new)
m = sum(item["m"] for item in new)

f_time = [n, p, nu1, nu2, nu3, nu4, nu5, nu6, f, m]
