#coding=utf-8
import re, string
import csv
import re
import pygal


def k_cal(num):
    if t0 >= 10 :
        if int(x1) != num and int(x2) != num and int(x3) != num and int(x4) != num and int(x5) != num and int(x6) != num and int(x7) != num and int(x8) != num and int(t1) != num and int(t2) != num and int(l) != num and int(s) != num and True:
            return num  
        else:
            num = 0
    else:
        if int(x1) != num and int(x2) != num and int(x3) != num and int(x4) != num and int(x5) != num and int(x6) != num and int(x7) != num and int(x8) != num and int(t1) != num and int(l) != num and int(s) != num:
            return num  
        else:
            num = 0

def k(num):
    if k_cal(num) != None:
        return k_cal(num)
    else:
        return 0

def c_zd(nu, nu1, zod, elm):
    if int(y)%12 == nu and int(y4) == nu1 and True:
        return zod

def sx():
    if c_zd(4, 4, "cz1", "m") != None:
        c1 = c_zd(4, 4, "cz1", "m")
    elif c_zd(4, 6, "cz1", "h") != None:
        c1 = c_zd(4, 6, "cz1", "h")
    elif c_zd(4, 8, "cz1", "t") != None:
        c1 = c_zd(4, 8, "cz1", "t")
    elif c_zd(4, 0, "cz1", "j") != None:
        c1 = c_zd(4, 0, "cz1", "j")
    elif c_zd(4, 2, "cz1", "s") != None:
        c1 = c_zd(4, 2, "cz1", "s")
    elif c_zd(5, 5, "cz2", "m") != None:
        c1 = c_zd(5, 5, "cz2", "m")
    elif c_zd(5, 7, "cz2", "h") != None:
        c1 = c_zd(5, 7, "cz2", "h")
    elif c_zd(5, 9, "cz2", "t") != None:
        c1 = c_zd(5, 9, "cz2", "t")
    elif c_zd(5, 1, "cz2", "j") != None:
        c1 = c_zd(5, 1, "cz2", "j")
    elif c_zd(5, 3, "cz2", "s") != None:
        c1 = c_zd(5, 3, "cz2", "s")
    elif c_zd(6, 4, "cz3", "m") != None:
        c1 = c_zd(6, 4, "cz3", "m")
    elif c_zd(6, 6, "cz3", "h") != None:
        c1 = c_zd(6, 6, "cz3", "h")
    elif c_zd(6, 8, "cz3", "t") != None:
        c1 = c_zd(6, 8, "cz3", "t")
    elif c_zd(6, 0, "cz3", "j") != None:
        c1 = c_zd(6, 0, "cz3", "j")
    elif c_zd(6, 2, "cz3", "s") != None:
        c1 = c_zd(6, 2, "cz3", "s")
    elif c_zd(7, 5, "cz4", "m") != None:
        c1 = c_zd(7, 5, "cz4", "m")
    elif c_zd(7, 7, "cz4", "h") != None:
        c1 = c_zd(7, 7, "cz4", "h")
    elif c_zd(7, 9, "cz4", "t") != None:
        c1 = c_zd(7, 9, "cz4", "t")
    elif c_zd(7, 1, "cz4", "j") != None:
        c1 = c_zd(7, 1, "cz4", "j")
    elif c_zd(7, 3, "cz4", "s") != None:
        c1 = c_zd(7, 3, "cz4", "s")
    elif c_zd(8, 4, "cz5", "m") != None:
        c1 = c_zd(8, 4, "cz5", "m")
    elif c_zd(8, 6, "cz5", "h") != None:
        c1 = c_zd(8, 6, "cz5", "h")
    elif c_zd(8, 8, "cz5", "t") != None:
        c1 = c_zd(8, 8, "cz5", "t")
    elif c_zd(8, 0, "cz5", "j") != None:
        c1 = c_zd(8, 0, "cz5", "j")
    elif c_zd(8, 2, "cz5", "s") != None:
        c1 = c_zd(8, 2, "cz5", "s")
    elif c_zd(9, 5, "cz6", "m") != None:
        c1 = c_zd(9, 5, "cz6", "m")
    elif c_zd(9, 7, "cz6", "h") != None:
        c1 = c_zd(9, 7, "cz6", "h")
    elif c_zd(9, 9, "cz6", "t") != None:
        c1 = c_zd(9, 9, "cz6", "t")
    elif c_zd(9, 1, "cz6", "j") != None:
        c1 = c_zd(9, 1, "cz6", "j")
    elif c_zd(9, 3, "cz6", "s") != None:
        c1 = c_zd(9, 3, "cz6", "s")
    elif c_zd(10, 4, "cz7", "m") != None:
        c1 = c_zd(10, 4, "cz7", "m")
    elif c_zd(10, 6, "cz7", "h") != None:
        c1 = c_zd(10, 6, "cz7", "h")
    elif c_zd(10, 8, "cz7", "t") != None:
        c1 = c_zd(10, 8, "cz7", "t")
    elif c_zd(10, 0, "cz7", "j") != None:
        c1 = c_zd(10, 0, "cz7", "j")
    elif c_zd(10, 2, "cz7", "s") != None:
        c1 = c_zd(10, 2, "cz7", "s")
    elif c_zd(11, 5, "cz8", "m") != None:
        c1 = c_zd(11, 5, "cz8", "m")
    elif c_zd(11, 7, "cz8", "h") != None:
        c1 = c_zd(11, 7, "cz8", "h")
    elif c_zd(11, 9, "cz8", "t") != None:
        c1 = c_zd(11, 9, "cz8", "t")
    elif c_zd(11, 1, "cz8", "j") != None:
        c1 = c_zd(11, 1, "cz8", "j")
    elif c_zd(11, 3, "", "s") != None:
        c1 = c_zd(11, 3, "cz8", "s")
    elif c_zd(0, 4, "cz9", "m") != None:
        c1 = c_zd(0, 4, "cz9", "m")
    elif c_zd(0, 6, "cz9", "h") != None:
        c1 = c_zd(0, 6, "cz9", "h")
    elif c_zd(0, 8, "cz9", "t") != None:
        c1 = c_zd(0, 8, "cz9", "t")
    elif c_zd(0, 0, "cz9", "j") != None:
        c1 = c_zd(0, 0, "cz9", "j")
    elif c_zd(0, 2, "cz9", "s") != None:
        c1 = c_zd(0, 2, "cz9", "s")
    elif c_zd(1, 5, "cz10", "m") != None:
        c1 = c_zd(1, 5, "cz10", "m")
    elif c_zd(1, 7, "cz10", "h") != None:
        c1 = c_zd(1, 7, "cz10", "h")
    elif c_zd(1, 9, "cz10", "t") != None:
        c1 = c_zd(1, 9, "cz10", "t")
    elif c_zd(1, 1, "cz10", "j") != None:
        c1 = c_zd(1, 1, "cz10", "j")
    elif c_zd(1, 3, "cz10", "s") != None:
        c1 = c_zd(1, 3, "cz10", "s")
    elif c_zd(2, 4, "cz11", "m") != None:
        c1 = c_zd(2, 4, "cz11", "m")
    elif c_zd(2, 6, "cz11", "h") != None:
        c1 = c_zd(2, 6, "cz11", "h")
    elif c_zd(2, 8, "cz11", "t") != None:
        c1 = c_zd(2, 8, "cz11", "t")
    elif c_zd(2, 0, "cz11", "j") != None:
        c1 = c_zd(2, 0, "cz11", "j")
    elif c_zd(2, 2, "cz11", "s") != None:
        c1 = c_zd(2, 2, "cz11", "s")
    elif c_zd(3, 5, "cz12", "m") != None:
        c1 = c_zd(3, 5, "cz12", "m")
    elif c_zd(3, 7, "cz12", "h") != None:
        c1 = c_zd(3, 7, "cz12", "h")
    elif c_zd(3, 9, "cz12", "t") != None:
        c1 = c_zd(3, 9, "cz12", "t")
    elif c_zd(3, 1, "cz12", "j") != None:
        c1 = c_zd(3, 1, "cz12", "j")
    elif c_zd(3, 3, "cz12", "s") != None:
        c1 = c_zd(3, 3, "cz12", "s")
    return c1

def sx_e():
    if c_zd_e(4, 4, "cz1", "m") != None:
        ce1 = c_zd_e(4, 4, "cz1", "m")
    elif c_zd_e(4, 6, "cz1", "h") != None:
        ce1 = c_zd_e(4, 6, "cz1", "h")
    elif c_zd_e(4, 8, "cz1", "t") != None:
        ce1 = c_zd_e(4, 8, "cz1", "t")
    elif c_zd_e(4, 0, "cz1", "j") != None:
        ce1 = c_zd_e(4, 0, "cz1", "j")
    elif c_zd_e(4, 2, "cz1", "s") != None:
        ce1 = c_zd_e(4, 2, "cz1", "s")
    elif c_zd_e(5, 5, "cz2", "m") != None:
        ce1 = c_zd_e(5, 5, "cz2", "m")
    elif c_zd_e(5, 7, "cz2", "h") != None:
        ce1 = c_zd_e(5, 7, "cz2", "h")
    elif c_zd_e(5, 9, "cz2", "t") != None:
        ce1 = c_zd_e(5, 9, "cz2", "t")
    elif c_zd_e(5, 1, "cz2", "j") != None:
        ce1 = c_zd_e(5, 1, "cz2", "j")
    elif c_zd_e(5, 3, "cz2", "s") != None:
        ce1 = c_zd_e(5, 3, "cz2", "s")
    elif c_zd_e(6, 4, "cz3", "m") != None:
        ce1 = c_zd_e(6, 4, "cz3", "m")
    elif c_zd_e(6, 6, "cz3", "h") != None:
        ce1 = c_zd_e(6, 6, "cz3", "h")
    elif c_zd_e(6, 8, "cz3", "t") != None:
        ce1 = c_zd_e(6, 8, "cz3", "t")
    elif c_zd_e(6, 0, "cz3", "j") != None:
        ce1 = c_zd_e(6, 0, "cz3", "j")
    elif c_zd_e(6, 2, "cz3", "s") != None:
        ce1 = c_zd_e(6, 2, "cz3", "s")
    elif c_zd_e(7, 5, "cz4", "m") != None:
        ce1 = c_zd_e(7, 5, "cz4", "m")
    elif c_zd_e(7, 7, "cz4", "h") != None:
        ce1 = c_zd_e(7, 7, "cz4", "h")
    elif c_zd_e(7, 9, "cz4", "t") != None:
        ce1 = c_zd_e(7, 9, "cz4", "t")
    elif c_zd_e(7, 1, "cz4", "j") != None:
        ce1 = c_zd_e(7, 1, "cz4", "j")
    elif c_zd_e(7, 3, "cz4", "s") != None:
        ce1 = c_zd_e(7, 3, "cz4", "s")
    elif c_zd_e(8, 4, "cz5", "m") != None:
        ce1 = c_zd_e(8, 4, "cz5", "m")
    elif c_zd_e(8, 6, "cz5", "h") != None:
        ce1 = c_zd_e(8, 6, "cz5", "h")
    elif c_zd_e(8, 8, "cz5", "t") != None:
        ce1 = c_zd_e(8, 8, "cz5", "t")
    elif c_zd_e(8, 0, "cz5", "j") != None:
        ce1 = c_zd_e(8, 0, "cz5", "j")
    elif c_zd_e(8, 2, "cz5", "s") != None:
        ce1 = c_zd_e(8, 2, "cz5", "s")
    elif c_zd_e(9, 5, "cz6", "m") != None:
        ce1 = c_zd_e(9, 5, "cz6", "m")
    elif c_zd_e(9, 7, "cz6", "h") != None:
        ce1 = c_zd_e(9, 7, "cz6", "h")
    elif c_zd_e(9, 9, "cz6", "t") != None:
        ce1 = c_zd_e(9, 9, "cz6", "t")
    elif c_zd_e(9, 1, "cz6", "j") != None:
        ce1 = c_zd_e(9, 1, "cz6", "j")
    elif c_zd_e(9, 3, "cz6", "s") != None:
        ce1 = c_zd_e(9, 3, "cz6", "s")
    elif c_zd_e(10, 4, "cz7", "m") != None:
        ce1 = c_zd_e(10, 4, "cz7", "m")
    elif c_zd_e(10, 6, "cz7", "h") != None:
        ce1 = c_zd_e(10, 6, "cz7", "h")
    elif c_zd_e(10, 8, "cz7", "t") != None:
        ce1 = c_zd_e(10, 8, "cz7", "t")
    elif c_zd_e(10, 0, "cz7", "j") != None:
        ce1 = c_zd_e(10, 0, "cz7", "j")
    elif c_zd_e(10, 2, "cz7", "s") != None:
        ce1 = c_zd_e(10, 2, "cz7", "s")
    elif c_zd_e(11, 5, "cz8", "m") != None:
        ce1 = c_zd_e(11, 5, "cz8", "m")
    elif c_zd_e(11, 7, "cz8", "h") != None:
        ce1 = c_zd_e(11, 7, "cz8", "h")
    elif c_zd_e(11, 9, "cz8", "t") != None:
        ce1 = c_zd_e(11, 9, "cz8", "t")
    elif c_zd_e(11, 1, "cz8", "j") != None:
        ce1 = c_zd_e(11, 1, "cz8", "j")
    elif c_zd_e(11, 3, "", "s") != None:
        ce1 = c_zd_e(11, 3, "cz8", "s")
    elif c_zd_e(0, 4, "cz9", "m") != None:
        ce1 = c_zd_e(0, 4, "cz9", "m")
    elif c_zd_e(0, 6, "cz9", "h") != None:
        ce1 = c_zd_e(0, 6, "cz9", "h")
    elif c_zd_e(0, 8, "cz9", "t") != None:
        ce1 = c_zd_e(0, 8, "cz9", "t")
    elif c_zd_e(0, 0, "cz9", "j") != None:
        ce1 = c_zd_e(0, 0, "cz9", "j")
    elif c_zd_e(0, 2, "cz9", "s") != None:
        ce1 = c_zd_e(0, 2, "cz9", "s")
    elif c_zd_e(1, 5, "cz10", "m") != None:
        ce1 = c_zd_e(1, 5, "cz10", "m")
    elif c_zd_e(1, 7, "cz10", "h") != None:
        ce1 = c_zd_e(1, 7, "cz10", "h")
    elif c_zd_e(1, 9, "cz10", "t") != None:
        ce1 = c_zd_e(1, 9, "cz10", "t")
    elif c_zd_e(1, 1, "cz10", "j") != None:
        ce1 = c_zd_e(1, 1, "cz10", "j")
    elif c_zd_e(1, 3, "cz10", "s") != None:
        ce1 = c_zd_e(1, 3, "cz10", "s")
    elif c_zd_e(2, 4, "cz11", "m") != None:
        ce1 = c_zd_e(2, 4, "cz11", "m")
    elif c_zd_e(2, 6, "cz11", "h") != None:
        ce1 = c_zd_e(2, 6, "cz11", "h")
    elif c_zd_e(2, 8, "cz11", "t") != None:
        ce1 = c_zd_e(2, 8, "cz11", "t")
    elif c_zd_e(2, 0, "cz11", "j") != None:
        ce1 = c_zd_e(2, 0, "cz11", "j")
    elif c_zd_e(2, 2, "cz11", "s") != None:
        ce1 = c_zd_e(2, 2, "cz11", "s")
    elif c_zd_e(3, 5, "cz12", "m") != None:
        ce1 = c_zd_e(3, 5, "cz12", "m")
    elif c_zd_e(3, 7, "cz12", "h") != None:
        ce1 = c_zd_e(3, 7, "cz12", "h")
    elif c_zd_e(3, 9, "cz12", "t") != None:
        ce1 = c_zd_e(3, 9, "cz12", "t")
    elif c_zd_e(3, 1, "cz12", "j") != None:
        ce1 = c_zd_e(3, 1, "cz12", "j")
    elif c_zd_e(3, 3, "cz12", "s") != None:
        ce1 = c_zd_e(3, 3, "cz12", "s")
    return ce1

def zd(mese, dia):
    zd_name=(u"z10",u"z11",u"z12",u"z1",u"z2",u"z3",
                u"z4",u"z5",u"z6",u"z7",u"z8",u"z9")
    zd_days=((1,20),(2,19),(3,21),(4,20),(5,21),(6,21),
                (7,22),(8,23),(9,23),(10,23),(11,22),(12,22))    
    month = mese
    day = dia
    zd_day=list(filter(lambda x: x<=(month,day),zd_days))
    zd_len=len(list(zd_day))%12
    return zd_name[zd_len]

def c_zd_e(nu, nu1, zod, elm):
    if int(y)%12 == nu and int(y4) == nu1 and True:
        return elm
    
def world_c(year, month, day):  
    if month[:1] == "0":
        m = int(month[1:2])
    else:
        m = int(month)

    if day[:1] == "0":
        d = int(day[1:2])
    else:
        d = int(day)

    if m < 3:
        m1 = 12 + m
        y = int(year) - 1
    else:
        m1 = m
        y = int(year)

    sj = int(str(y)[0:2]) + 1
    s = int(str(y)[2:4])
    m_j = (30 * (((-1)**m1 + 1)/2)) + int((3*m1-7)/5)  
    x = (44 * (sj-1) + int((sj-1)/4) + 9) % 60  
    s1 = int(s/4)
    u = s % 4
    r = (s1*6 + 5*(s1*3 + u) + m_j + d + x) % 60  
    return r

def tian_g(r1):  
    if r1 == 1:
        e_f = "m1"
    elif r1 == 2:
        e_f = "m2"
    elif r1 == 3:
        e_f = "h3"
    elif r1 == 4:
        e_f = "h4"
    elif r1 == 5:
        e_f = "t5"
    elif r1 == 6:
        e_f = "t6"
    elif r1 == 7:
        e_f = "j7"
    elif r1 == 8:
        e_f = "j8"
    elif r1 == 9:
        e_f = "s9"
    elif r1 == 10:
        e_f = "s10"
    elif r1 == 11:
        e_f = "m1"
    elif r1 == 12:
        e_f = "m2"
    elif r1 == 13:
        e_f = "h3"
    elif r1 == 14:
        e_f = "h4"
    elif r1 == 15:
        e_f = "t5"
    elif r1 == 16:
        e_f = "t6"
    elif r1 == 17:
        e_f = "j7"
    elif r1 == 18:
        e_f = "j8"
    elif r1 == 19:
        e_f = "s9"
    elif r1 == 20:
        e_f = "s10"
    elif r1 == 21:
        e_f = "m1"
    elif r1 == 22:
        e_f = "m2"
    elif r1 == 23:
        e_f = "h3"
    elif r1 == 24:
        e_f = "h4"
    elif r1 == 25:
        e_f = "t5"
    elif r1 == 26:
        e_f = "t6"
    elif r1 == 27:
        e_f = "j7"
    elif r1 == 28:
        e_f = "j8"
    elif r1 == 29:
        e_f = "s9"
    elif r1 == 30:
        e_f = "s10"
    elif r1 == 31:
        e_f = "m1"
    elif r1 == 32:
        e_f = "m2"
    elif r1 == 33:
        e_f = "h3"
    elif r1 == 34:
        e_f = "h4"
    elif r1 == 35:
        e_f = "t5"
    elif r1 == 36:
        e_f = "t6"
    elif r1 == 37:
        e_f = "j7"
    elif r1 == 38:
        e_f = "j8"
    elif r1 == 39:
        e_f = "s9"
    elif r1 == 40:
        e_f = "s10"
    elif r1 == 41:
        e_f = "m1"
    elif r1 == 42:
        e_f = "m2"
    elif r1 == 43:
        e_f = "h3"
    elif r1 == 44:
        e_f = "h4"
    elif r1 == 45:
        e_f = "t5"
    elif r1 == 46:
        e_f = "t6"
    elif r1 == 47:
        e_f = "j7"
    elif r1 == 48:
        e_f = "j8"
    elif r1 == 49:
        e_f = "s9"
    elif r1 == 50:
        e_f = "s10"
    elif r1 == 51:
        e_f = "m1"
    elif r1 == 52:
        e_f = "m2"
    elif r1 == 53:
        e_f = "h3"
    elif r1 == 54:
        e_f = "h4"
    elif r1 == 55:
        e_f = "t5"
    elif r1 == 56:
        e_f = "t6"
    elif r1 == 57:
        e_f = "j7"
    elif r1 == 58:
        e_f = "j8"
    elif r1 == 59:
        e_f = "s9"
    elif r1 == 60:
        e_f = "s10"
    return e_f

def num_cnt(x):
    if  x in num_all:
        return x
    else :
        pass


date_dict = "/Users/roon/Desktop/YHVH/Soda复赛demo/data/day_dict.sql"

year1 = input("年份(yyyy): ")
month1 = input("月份(mm): ")
day1 = input("Day(dd): ")
date_list = year1 + "/" + month1 + "/" + day1

year = str(year1)
month = str(month1)
day = str(day1)
y = year
m = month
d = day

y1= year[0:1]
y2 = year[1:2]
y3 = year[2:3]
y4 = year[3:4]
m1 = month[0:1]
m2 = month[1:2]
d1 = day[0:1]
d2 = day[1:2]

t0 = int(y1) + int(y2) + int(y3) + int(y4) + int(m1) + int(m2) + int(d1) + int(d2)
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

s0 = int(d1) + int(d2)
s = str(s0)   

x1 = y1   
x2 = y2   
x3 = y3   
x4 = y4   
x5 = m1   
x6 = m2   
x7 = d1   
x8 = d2   

k1 = k(1)   
k2 = k(2)   
k3 = k(3)   
k4 = k(4)   
k5 = k(5)   
k6 = k(6)   
k7 = k(7)   
k8 = k(8)   
k9 = k(9)   

lz = l    
z_final = zd(int(m), int(d))  
c_final = sx()   
ce_final = sx_e()   
r = world_c(year, month, day)
e_final = tian_g(r)   

new_pu = []  
new_Ne = []  
new_Po = []  
results = [] 

fr = open(date_dict, "r")
dict1_all = eval(fr.read())
fr.close()

name = str("n") + str(t1) + str("t")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(t2) + str("t")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(l) + str("l")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(s) + str("s")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x1) + str("x")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x1) + str("x_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("n") + str(x1) + str("x_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("n") + str(x2) + str("x")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x2) + str("x_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("n") + str(x2) + str("x_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("n") + str(x3) + str("x")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x3) + str("x_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("n") + str(x3) + str("x_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("n") + str(x4) + str("x")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x4) + str("x_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("n") + str(x4) + str("x_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("n") + str(x5) + str("x")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x5) + str("x_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("n") + str(x5) + str("x_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("n") + str(x6) + str("x")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x6) + str("x_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("n") + str(x6) + str("x_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("n") + str(x7) + str("x")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x7) + str("x_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("n") + str(x7) + str("x_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("n") + str(x8) + str("x")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(x8) + str("x_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("n") + str(x8) + str("x_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

num_all = {int(x1), int(x2), int(x3), int(x4), int(x5), int(
    x6), int(x7), int(x8), int(t1), int(t2), int(l), int(s)}

if num_cnt(1) == 1 and num_cnt(2) == 2 and num_cnt(3) == 3:
    name = "1-2-3"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(1) == 1 and num_cnt(4) == 4 and num_cnt(7) == 7:
    name = "1-4-7"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(1) == 1 and num_cnt(5) == 5 and num_cnt(9) == 9:
    name = "1-5-9"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(2) == 2 and num_cnt(4) == 4:
    name = "2-4"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(2) == 2 and num_cnt(6) == 6:
    name = "2-6"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(2) == 2 and num_cnt(5) == 5 and num_cnt(8) == 8:
    name = "2-5-8"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(3) == 3 and num_cnt(5) == 5 and num_cnt(7) == 7:
    name = "3-5-7"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(3) == 3 and num_cnt(6) == 6 and num_cnt(9) == 9:
    name = "3-6-9"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(4) == 4 and num_cnt(5) == 5 and num_cnt(6) == 6:
    name = "4-5-6"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(4) == 4 and num_cnt(8) == 8:
    name = "4-8"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(6) == 6 and num_cnt(8) == 8:
    name = "6-8"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

if num_cnt(7) == 7 and num_cnt(8) == 8 and num_cnt(9) == 9:
    name = "7-8-9"
    for value in dict1_all:
        #print (value)
        if name == value["name"]:
            new_pu.append(value.copy())
            # print(name)
else:
    pass

name = str("n") + str(l) + str(z_final)
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k1) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k2) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k3) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k4) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k5) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k6) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k7) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k8) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("n") + str(k9) + str("k")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("") + str(z_final) + str("")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("") + str(z_final) + str("_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("") + str(z_final) + str("_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("") + str(c_final) + str("")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("") + str(c_final) + str("_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("") + str(c_final) + str("_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str(c_final) + str(ce_final) + str("_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str(c_final) + str(ce_final) + str("_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

# 五行
name = str("e_") + str(e_final[0:1]) + str("")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("e_") + str(e_final[0:1]) + str("_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("e_") + str(e_final[0:1]) + str("_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

name = str("e_") + str(e_final) + str("")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_pu.append(value.copy())

name = str("e_") + str(e_final) + str("_1")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Po.append(value.copy())

name = str("e_") + str(e_final) + str("_0")
for value in dict1_all:
    #print (value)
    if name == value["name"]:
        new_Ne.append(value.copy())

n_pu = sum(item["n"] for item in new_pu)
p_pu = sum(item["p"] for item in new_pu)
nu1_pu = sum(item["nu1"] for item in new_pu) 
nu2_pu = sum(item["nu2"] for item in new_pu)
nu3_pu = sum(item["nu3"] for item in new_pu)
nu4_pu = sum(item["nu4"] for item in new_pu)
nu5_pu = sum(item["nu5"] for item in new_pu)
nu6_pu = sum(item["nu6"] for item in new_pu)
f_pu = sum(item["f"] for item in new_pu)
m_pu = sum(item["m"] for item in new_pu)

n_Po = sum(item["n"] for item in new_Po) + n_pu
p_Po = sum(item["p"] for item in new_Po) + p_pu
nu1_Po = sum(item["nu1"] for item in new_Po) + nu1_pu
nu2_Po = sum(item["nu2"] for item in new_Po) + nu2_pu
nu3_Po = sum(item["nu3"] for item in new_Po) + nu3_pu
nu4_Po = sum(item["nu4"] for item in new_Po) + nu4_pu
nu5_Po = sum(item["nu5"] for item in new_Po) + nu5_pu
nu6_Po = sum(item["nu6"] for item in new_Po) + nu6_pu
f_Po = sum(item["f"] for item in new_Po) + f_pu
m_Po = sum(item["m"] for item in new_Po) + m_pu
# 生日 Negative
n_Ne = sum(item["n"] for item in new_Ne) + n_pu
p_Ne = sum(item["p"] for item in new_Ne) + p_pu
nu1_Ne = sum(item["nu1"] for item in new_Ne) + nu1_pu
nu2_Ne = sum(item["nu2"] for item in new_Ne) + nu2_pu
nu3_Ne = sum(item["nu3"] for item in new_Ne) + nu3_pu
nu4_Ne = sum(item["nu4"] for item in new_Ne) + nu4_pu
nu5_Ne = sum(item["nu5"] for item in new_Ne) + nu5_pu
nu6_Ne = sum(item["nu6"] for item in new_Ne) + nu6_pu
f_Ne = sum(item["f"] for item in new_Ne) + f_pu
m_Ne = sum(item["m"] for item in new_Ne) + m_pu

n = n_Po + n_Ne - n_pu
p = p_Po + p_Ne - p_pu
nu1 = nu1_Po + nu1_Ne - nu1_pu
nu2 = nu2_Po + nu2_Ne - nu2_pu
nu3 = nu3_Po + nu3_Ne - nu3_pu
nu4 = nu4_Po + nu4_Ne - nu4_pu
nu5 = nu5_Po + nu5_Ne - nu5_pu
nu6 = nu6_Po + nu6_Ne - nu6_pu
f = f_Po + f_Ne - f_pu
m = m_Po + m_Ne - m_pu

new = [["date:", n, p, nu1, nu2, nu3, nu4, nu5, nu6, f, m]]
new_pu = [["pure:", n_pu, p_pu, nu1_pu, nu2_pu, nu3_pu, nu4_pu, nu5_pu, nu6_pu, f_pu, m_pu]]
new_Po = [["positive:", n_Po, p_Po, nu1_Po, nu2_Po, nu3_Po, nu4_Po, nu5_Po, nu6_Po, f_Po, m_Po]]
new_Ne = [["nagative:", n_Ne, p_Ne, nu1_Ne, nu2_Ne, nu3_Ne, nu4_Ne, nu5_Ne, nu6_Ne, f_Ne, m_Ne]]

# print("\t%s\t%d\t%d\t%d\t%d\t%d\t%d\n\t%s\t%d\t%d\t%d\t%d\t%d\t%d\n\t%s\t%d\t%d\t%d\t%d\t%d\t%d\n\t%s\t%d\t%d\n\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n\t\t%d\t%d" %
#      ("nature pure:", nu1_pu, nu2_pu, nu3_pu, nu4_pu, nu5_pu, nu6_pu,
#       "positive:", nu1_Po, nu2_Po, nu3_Po, nu4_Po, nu5_Po, nu6_Po,
#       "negative:", nu1_Ne, nu2_Ne, nu3_Ne, nu4_Ne, nu5_Ne, nu6_Ne,
#       "date:", n, p, nu1, nu2, nu3, nu4, nu5, nu6, f, m))

y_1 = [nu1* 1.81, nu2* 0.83, nu3* 0.69, nu4* 0.91, nu5* 1.49, nu6* 0.97]
y_2 = [nu1_pu* 1.81, nu2_pu* 0.83, nu3_pu* 0.69, nu4_pu* 0.91, nu5_pu* 1.49, nu6_pu* 0.97]
y_3 = [nu1_Po* 1.81, nu2_Po* 0.83, nu3_Po* 0.69, nu4_Po* 0.91, nu5_Po* 1.49, nu6_Po* 0.97]
y_4 = [nu1_Ne* 1.81, nu2_Ne* 0.83, nu3_Ne* 0.69, nu4_Ne* 0.91, nu5_Ne* 1.49, nu6_Ne* 0.97]
