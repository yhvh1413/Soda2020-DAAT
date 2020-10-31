#coding=utf-8
import csv
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np
import sys


def fh_cal(nu1_pu, nu2_pu, nu3_pu, nu4_pu, nu5_pu, nu6_pu,
           nu1_po, nu2_po, nu3_po, nu4_po, nu5_po, nu6_po,
           nu1_ne, nu2_ne, nu3_ne, nu4_ne, nu5_ne, nu6_ne,
           nu1, nu2, nu3, nu4, nu5, nu6):
    nu1_pu_avg = 32.44
    nu2_pu_avg = 70.62
    nu3_pu_avg = 84.72
    nu4_pu_avg = 64.37
    nu5_pu_avg = 39.40
    nu6_pu_avg = 60.67
    nu1_po_avg = 44.24
    nu2_po_avg = 96.82
    nu3_po_avg = 122.41
    nu4_po_avg = 89.28
    nu5_po_avg = 50.48
    nu6_po_avg = 86.25
    nu1_ne_avg = 50.04
    nu2_ne_avg = 99.32
    nu3_ne_avg = 106.02
    nu4_ne_avg = 74.23
    nu5_ne_avg = 53.83
    nu6_ne_avg = 69.05
    nu1_avg = 61.84
    nu2_avg = 125.53
    nu3_avg = 143.71
    nu4_avg = 99.14
    nu5_avg = 64.91
    nu6_avg = 94.64

    nu1_pu_f = nu1_pu - nu1_pu_avg
    nu2_pu_f = nu2_pu - nu2_pu_avg
    nu3_pu_f = nu3_pu - nu3_pu_avg
    nu4_pu_f = nu4_pu - nu4_pu_avg
    nu5_pu_f = nu5_pu - nu5_pu_avg
    nu6_pu_f = nu6_pu - nu6_pu_avg
    nu1_po_f = nu1_po - nu1_po_avg
    nu2_po_f = nu2_po - nu2_po_avg
    nu3_po_f = nu3_po - nu3_po_avg
    nu4_po_f = nu4_po - nu4_po_avg
    nu5_po_f = nu5_po - nu5_po_avg
    nu6_po_f = nu6_po - nu6_po_avg
    nu1_ne_f = nu1_ne - nu1_ne_avg
    nu2_ne_f = nu2_ne - nu2_ne_avg
    nu3_ne_f = nu3_ne - nu3_ne_avg
    nu4_ne_f = nu4_ne - nu4_ne_avg
    nu5_ne_f = nu5_ne - nu5_ne_avg
    nu6_ne_f = nu6_ne - nu6_ne_avg
    nu1_f = nu1 - nu1_avg
    nu2_f = nu2 - nu2_avg
    nu3_f = nu3 - nu3_avg
    nu4_f = nu4 - nu4_avg
    nu5_f = nu5 - nu5_avg
    nu6_f = nu6 - nu6_avg

    fh_final = [nu1_pu_f, nu2_pu_f, nu3_pu_f, nu4_pu_f, nu5_pu_f, nu6_pu_f, nu1_po_f, nu2_po_f, nu3_po_f, nu4_po_f, nu5_po_f,
                nu6_po_f, nu1_ne_f, nu2_ne_f, nu3_ne_f, nu4_ne_f, nu5_ne_f, nu6_ne_f, nu1_f, nu2_f, nu3_f, nu4_f, nu5_f, nu6_f]

    return fh_final


def style(data, nu1_pu, nu2_pu, nu3_pu, nu4_pu, nu5_pu, nu6_pu,
          nu1_Po, nu2_Po, nu3_Po, nu4_Po, nu5_Po, nu6_Po,
          nu1_Ne, nu2_Ne, nu3_Ne, nu4_Ne, nu5_Ne, nu6_Ne,
          nu1, nu2, nu3, nu4, nu5, nu6):
    dt = data

    def hd(a, a_t):
        if a > 0:
            nu = int(a) - 1
            if a_t == 1:
                if dt[nu] > 0:
                    a_f = dt[nu]
                else:
                    a_f = 0
            elif a_t == -1:
                if dt[nu] < 0:
                    a_f = -dt[nu]
                else:
                    a_f = 0
        else:
            a_f = 0

        return (a_f)

    print('数字>0代表趋向右边，反则<0代表趋向左边\n')
    st1_pu = (hd(1, -1) + hd(4, 1) + hd(2, 1)) - \
        (hd(1, 1) + hd(4, -1) + hd(2, 1))
    st1_po = (hd(7, -1) + hd(10, 1) + hd(8, 1)) - \
        (hd(7, 1) + hd(10, -1) + hd(8, 1))
    st1_ne = (hd(13, -1) + hd(16, 1) + hd(14, 1)) - \
        (hd(13, 1) + hd(16, -1) + hd(14, 1))
    st1_nu = (hd(19, -1) + hd(22, 1) + hd(20, 1)) - \
        (hd(19, 1) + hd(22, -1) + hd(20, 1))
    st1 = (st1_pu + st1_po + st1_ne + st1_nu) / 4
    print("亮色/暗色", st1)

    st2_pu = (hd(3, 1) + hd(4, 1) + hd(2, -1) + hd(5, -1) + hd(6, -1)) - \
        (hd(4, -1) + hd(2, 1) + hd(5, 1) + hd(6, 1))
    st2_po = (hd(9, 1) + hd(10, 1) + hd(8, -1) + hd(11, -1) + hd(12, -1)) - \
        (hd(10, -1) + hd(8, 1) + hd(11, 1) + hd(12, 1))
    st2_ne = (hd(15, 1) + hd(16, 1) + hd(14, -1) + hd(17, -1) + hd(18, -1)) - \
        (hd(16, -1) + hd(14, 1) + hd(17, 1) + hd(18, 1))
    st2_nu = (hd(21, 1) + hd(22, 1) + hd(20, -1) + hd(23, -1) + hd(24, -1)) - \
        (hd(22, -1) + hd(20, 1) + hd(23, 1) + hd(24, 1))
    st2 = (st2_pu + st2_po + st2_ne + st2_nu) / 4
    print("性感/保守", st2)

    st3_pu = (hd(2, 1) + hd(3, 1) + hd(4, -1)) - \
        (hd(3, 1) + hd(4, 1) + hd(2, -1))
    st3_po = (hd(8, 1) + hd(9, 1) + hd(10, -1)) - \
        (hd(9, 1) + hd(10, 1) + hd(8, -1))
    st3_ne = (hd(14, 1) + hd(15, 1) + hd(16, -1)) - \
        (hd(15, 1) + hd(16, 1) + hd(14, -1))
    st3_nu = (hd(20, 1) + hd(21, 1) + hd(22, -1)) - \
        (hd(21, 1) + hd(22, 1) + hd(20, -1))
    st3 = (st3_pu + st3_po + st3_ne + st3_nu) / 4
    print("对称/不对称", st3)

    st4_pu = (hd(1, -1) + hd(4, 1) + hd(2, 1) + hd(5, -1)) - \
        (hd(1, -1) + hd(4, 1) + hd(5, 1) + hd(2, -1))
    st4_po = (hd(7, -1) + hd(10, 1) + hd(8, 1) + hd(11, -1)) - \
        (hd(7, -1) + hd(10, 1) + hd(11, 1) + hd(8, -1))
    st4_ne = (hd(13, -1) + hd(16, 1) + hd(14, 1) + hd(17, -1)) - \
        (hd(13, -1) + hd(16, 1) + hd(17, 1) + hd(14, -1))
    st4_nu = (hd(19, -1) + hd(22, 1) + hd(20, 1) + hd(23, -1)) - \
        (hd(19, -1) + hd(22, 1) + hd(23, 1) + hd(20, -1))
    st4 = (st4_pu + st4_po + st4_ne + st4_nu) / 4
    print("材料厚/材料薄", st4)

    st5_pu = (hd(1, 1) + hd(2, 1) + hd(4, -1)) - \
        (hd(1, 1) + hd(2, -1) + hd(4, 1))
    st5_po = (hd(7, 1) + hd(8, 1) + hd(10, -1)) - \
        (hd(7, 1) + hd(8, -1) + hd(10, 1))
    st5_ne = (hd(13, 1) + hd(14, 1) + hd(16, -1)) - \
        (hd(13, 1) + hd(14, -1) + hd(16, 1))
    st5_nu = (hd(19, 1) + hd(20, 1) + hd(22, -1)) - \
        (hd(19, 1) + hd(20, -1) + hd(22, 1))
    st5 = (st5_pu + st5_po + st5_ne + st5_nu) / 4
    print("材料硬/材料软", st5)

    st6_pu = (hd(2, -1) + hd(3, 1) + hd(4, 1)) - \
        (hd(2, 1) + hd(3, -1) + hd(4, 1))
    st6_po = (hd(8, -1) + hd(9, 1) + hd(10, 1)) - \
        (hd(8, 1) + hd(9, -1) + hd(10, 1))
    st6_ne = (hd(14, -1) + hd(15, 1) + hd(16, 1)) - \
        (hd(14, 1) + hd(15, -1) + hd(16, 1))
    st6_nu = (hd(20, -1) + hd(21, 1) + hd(22, 1)) - \
        (hd(20, 1) + hd(21, -1) + hd(22, 1))
    st6 = (st6_pu + st6_po + st6_ne + st6_nu) / 4
    print("外观/材质", st6)

    st7_pu = (hd(1, -1) + hd(2, -1) + hd(3, -1) + hd(4, 1)) - \
        (hd(1, 1) + hd(2, 1) + hd(3, 1) + hd(4, -1))
    st7_po = (hd(7, -1) + hd(8, -1) + hd(9, -1) + hd(10, 1)) - \
        (hd(7, 1) + hd(8, 1) + hd(9, 1) + hd(10, -1))
    st7_ne = (hd(13, -1) + hd(14, -1) + hd(15, -1) + hd(16, 1)) - \
        (hd(13, 1) + hd(14, 1) + hd(15, 1) + hd(16, -1))
    st7_nu = (hd(19, -1) + hd(20, -1) + hd(21, -1) + hd(22, 1)) - \
        (hd(19, 1) + hd(20, 1) + hd(21, 1) + hd(22, -1))
    st7 = (st7_pu + st7_po + st7_ne + st7_nu) / 4
    print("古怪/常规", st7)

    st8_pu = (hd(1, 1) + hd(2, 1) + hd(3, 1) + hd(4, -1) + hd(5, -1)) - \
        (hd(1, -1) + hd(2, -1) + hd(3, -1) + hd(4, 1) + hd(5, 1))
    st8_po = (hd(7, 1) + hd(8, 1) + hd(9, 1) + hd(10, -1) + hd(11, -1)) - \
        (hd(7, -1) + hd(8, -1) + hd(9, -1) + hd(10, 1) + hd(11, 1))
    st8_ne = (hd(13, 1) + hd(14, 1) + hd(15, 1) + hd(16, -1) + hd(17, -1)) - \
        (hd(13, -1) + hd(14, -1) + hd(15, -1) + hd(16, 1) + hd(17, 1))
    st8_nu = (hd(19, 1) + hd(20, 1) + hd(21, 1) + hd(22, -1) + hd(23, -1)) - \
        (hd(19, -1) + hd(20, -1) + hd(21, -1) + hd(22, 1) + hd(23, 1))
    st8 = (st8_pu + st8_po + st8_ne + st8_nu) / 4
    print("层次多/单层", st8)

    st9_pu = (hd(2, -1) + hd(4, 1)) - \
        (hd(2, 1) + hd(4, -1))
    st9_po = (hd(8, -1) + hd(10, 1)) - \
        (hd(8, 1) + hd(10, -1))
    st9_ne = (hd(14, -1) + hd(16, 1)) - \
        (hd(14, 1) + hd(16, -1))
    st9_nu = (hd(20, -1) + hd(22, 1)) - \
        (hd(20, 1) + hd(22, -1))
    st9 = (st9_pu + st9_po + st9_ne + st9_nu) / 4
    print("多色/单色", st9)

    st10_pu = (hd(4, 1) + hd(1, -1) + hd(5, -1)) - \
        (hd(4, 1) + hd(1, 1) + hd(5, 1))
    st10_po = (hd(10, 1) + hd(7, -1) + hd(11, -1)) - \
        (hd(10, 1) + hd(7, 1) + hd(11, 1))
    st10_ne = (hd(16, 1) + hd(13, -1) + hd(17, -1)) - \
        (hd(16, 1) + hd(13, 1) + hd(17, 1))
    st10_nu = (hd(22, 1) + hd(19, -1) + hd(23, -1)) - \
        (hd(22, 1) + hd(19, 1) + hd(23, 1))
    st10 = (st10_pu + st10_po + st10_ne + st10_nu) / 4
    print("全场焦点/低调", st10)

    st11_pu = (hd(1, -1) + hd(2, 1) + hd(3, -1) + hd(4, 1) + hd(5, 1)) - \
        (hd(1, 1) + hd(2, -1) + hd(3, 1) + hd(4, 1) + hd(5, -1) + hd(6, -1)	)
    st11_po = (hd(7, -1) + hd(8, 1) + hd(9, -1) + hd(10, 1) + hd(11, 1)) - \
        (hd(7, 1) + hd(8, -1) + hd(9, 1) + hd(10, 1) + hd(11, -1) + hd(12, -1)	)
    st11_ne = (hd(13, -1) + hd(14, 1) + hd(15, -1) + hd(16, 1) + hd(17, 1)) - \
        (hd(13, 1) + hd(14, -1) + hd(15, 1) + hd(16, 1) + hd(17, -1) + hd(18, -1)	)
    st11_nu = (hd(19, -1) + hd(20, 1) + hd(21, -1) + hd(22, 1) + hd(23, 1)) - \
        (hd(19, 1) + hd(20, -1) + hd(21, 1) + hd(22, 1) + hd(23, -1) + hd(24, -1)	)
    st11 = (st11_pu + st11_po + st11_ne + st11_nu) / 4
    print("反复审视/第一眼感觉", st11)

    st12_pu = (hd(1, 1) + hd(3, 1) + hd(4, -1) + hd(6, 1)) - \
        (hd(1, -1) + hd(3, -1) + hd(4, 1) + hd(6, 1))
    st12_po = (hd(7, 1) + hd(9, 1) + hd(10, -1) + hd(12, 1)) - \
        (hd(7, -1) + hd(9, -1) + hd(10, 1) + hd(12, 1))
    st12_ne = (hd(13, 1) + hd(15, 1) + hd(16, -1) + hd(18, 1)) - \
        (hd(13, -1) + hd(15, -1) + hd(16, 1) + hd(18, 1))
    st12_nu = (hd(19, 1) + hd(21, 1) + hd(22, -1) + hd(24, 1)) - \
        (hd(19, -1) + hd(21, -1) + hd(22, 1) + hd(24, 1))
    st12 = (st12_pu + st12_po + st12_ne + st12_nu) / 4
    print("仪式性/方便性", st12)

    st13_pu = (hd(1, 1) + hd(4, 1) + hd(6, -1) + hd(5, -1)) - \
        (hd(1, 1) + hd(5, 1) + hd(6, 1) + hd(4, -1))
    st13_po = (hd(7, 1) + hd(10, 1) + hd(12, -1) + hd(11, -1)) - \
        (hd(7, 1) + hd(11, 1) + hd(12, 1) + hd(10, -1))
    st13_ne = (hd(13, 1) + hd(16, 1) + hd(18, -1) + hd(17, -1)) - \
        (hd(13, 1) + hd(17, 1) + hd(18, 1) + hd(16, -1))
    st13_nu = (hd(19, 1) + hd(22, 1) + hd(24, -1) + hd(23, -1)) - \
        (hd(19, 1) + hd(23, 1) + hd(24, 1) + hd(22, -1))
    st13 = (st13_pu + st13_po + st13_ne + st13_nu) / 4
    print("吸汗/防水", st13)

    st14_pu = (hd(1, 1) + hd(2, 1) + hd(3, 1) + hd(4, -1) + hd(5, -1)) - \
        (hd(1, -1) + hd(2, -1) + hd(3, -1) + hd(4, 1) + hd(5, 1))
    st14_po = (hd(7, 1) + hd(8, 1) + hd(9, 1) + hd(10, -1) + hd(11, -1)) - \
        (hd(7, -1) + hd(8, -1) + hd(9, -1) + hd(10, 1) + hd(11, 1))
    st14_ne = (hd(13, 1) + hd(14, 1) + hd(15, 1) + hd(16, -1) + hd(17, -1)) - \
        (hd(13, -1) + hd(14, -1) + hd(15, -1) + hd(16, 1) + hd(17, 1))
    st14_nu = (hd(19, 1) + hd(20, 1) + hd(21, 1) + hd(22, -1) + hd(23, -1)) - \
        (hd(19, -1) + hd(20, -1) + hd(21, -1) + hd(22, 1) + hd(23, 1))
    st14 = (st14_pu + st14_po + st14_ne + st14_nu) / 4
    print("复杂/干净", st14)

    st15_pu = (hd(3, 1) + hd(4, 1) + hd(6, -1)) - \
        (hd(2, 1) + hd(4, 1) + hd(6, 1))
    st15_po = (hd(9, 1) + hd(10, 1) + hd(12, -1)) - \
        (hd(8, 1) + hd(10, 1) + hd(12, 1))
    st15_ne = (hd(15, 1) + hd(16, 1) + hd(18, -1)) - \
        (hd(14, 1) + hd(16, 1) + hd(18, 1))
    st15_nu = (hd(21, 1) + hd(22, 1) + hd(24, -1)) - \
        (hd(20, 1) + hd(22, 1) + hd(24, 1))
    st15 = (st15_pu + st15_po + st15_ne + st15_nu) / 4
    print("异域/古典", st15)

    # 16 - 黑色/白色 - 1d4h2h | 1h4d2h
    st16_pu = (hd(1, -1) + hd(2, 1) + hd(4, 1)) - \
        (hd(1, 1) + hd(2, 1) + hd(4, -1))
    st16_po = (hd(7, -1) + hd(8, 1) + hd(10, 1)) - \
        (hd(7, 1) + hd(8, 1) + hd(10, -1))
    st16_ne = (hd(13, -1) + hd(14, 1) + hd(16, 1)) - \
        (hd(13, 1) + hd(14, 1) + hd(16, -1))
    st16_nu = (hd(19, -1) + hd(20, 1) + hd(22, 1)) - \
        (hd(19, 1) + hd(20, 1) + hd(22, -1))
    st16 = (st16_pu + st16_po + st16_ne + st16_nu) / 4
    print("白色/黑色", st16)

    st17_pu = (hd(1, -1) + hd(4, -1) + hd(5, -1)) - \
        (hd(1, 1) + hd(4, 1) + hd(5, 1))
    st17_po = (hd(7, -1) + hd(10, -1) + hd(11, -1)) - \
        (hd(7, 1) + hd(10, 1) + hd(11, 1))
    st17_ne = (hd(13, -1) + hd(16, -1) + hd(17, -1)) - \
        (hd(13, 1) + hd(16, 1) + hd(17, 1))
    st17_nu = (hd(19, -1) + hd(22, -1) + hd(23, -1)) - \
        (hd(19, 1) + hd(22, 1) + hd(23, 1))
    st17 = (st17_pu + st17_po + st17_ne + st17_nu) / 4
    print("开口大/开口小", st17)

    st18_pu = (hd(2, 1) + hd(3, 1) + hd(4, -1)) - \
        (hd(2, -1) + hd(3, -1) + hd(4, 1))
    st18_po = (hd(8, 1) + hd(9, 1) + hd(10, -1)) - \
        (hd(8, -1) + hd(9, -1) + hd(10, 1))
    st18_ne = (hd(14, 1) + hd(15, 1) + hd(16, -1)) - \
        (hd(14, -1) + hd(15, -1) + hd(16, 1))
    st18_nu = (hd(20, 1) + hd(21, 1) + hd(22, -1)) - \
        (hd(20, -1) + hd(21, -1) + hd(22, 1))
    st18 = (st18_pu + st18_po + st18_ne + st18_nu) / 4
    print("窄/宽", st18)

    st19_pu = (hd(2, 1) + hd(3, 1) + hd(4, -1)) - \
        (hd(3, 1) + hd(4, 1) + hd(2, -1))
    st19_po = (hd(8, 1) + hd(9, 1) + hd(10, -1)) - \
        (hd(9, 1) + hd(10, 1) + hd(8, -1))
    st19_ne = (hd(14, 1) + hd(15, 1) + hd(16, -1)) - \
        (hd(15, 1) + hd(16, 1) + hd(14, -1))
    st19_nu = (hd(20, 1) + hd(21, 1) + hd(22, -1)) - \
        (hd(21, 1) + hd(22, 1) + hd(20, -1))
    st19 = (st19_pu + st19_po + st19_ne + st19_nu) / 4
    print("用途/美观", st19)

    st20_pu = (hd(5, 1) + hd(1, 1) + hd(4, 1) + hd(3, -1)) - \
        (hd(5, 1) + hd(1, 1) + hd(3, 1) + hd(4, -1))
    st20_po = (hd(11, 1) + hd(7, 1) + hd(10, 1) + hd(9, -1)) - \
        (hd(11, 1) + hd(7, 1) + hd(9, 1) + hd(10, -1))
    st20_ne = (hd(17, 1) + hd(13, 1) + hd(16, 1) + hd(15, -1)) - \
        (hd(17, 1) + hd(13, 1) + hd(15, 1) + hd(16, -1))
    st20_nu = (hd(23, 1) + hd(19, 1) + hd(22, 1) + hd(21, -1)) - \
        (hd(23, 1) + hd(19, 1) + hd(21, 1) + hd(22, -1))
    st20 = (st20_pu + st20_po + st20_ne + st20_nu) / 4
    print("面料弹力大/面料无弹力", st20)

    st21_pu = (hd(1, -1) + hd(2, -1) + hd(5, -1)) - \
        (hd(1, 1) + hd(2, 1) + hd(5, 1))
    st21_po = (hd(7, -1) + hd(8, -1) + hd(11, -1)) - \
        (hd(7, 1) + hd(8, 1) + hd(11, 1))
    st21_ne = (hd(13, -1) + hd(14, -1) + hd(17, -1)) - \
        (hd(13, 1) + hd(14, 1) + hd(17, 1))
    st21_nu = (hd(19, -1) + hd(20, -1) + hd(23, -1)) - \
        (hd(19, 1) + hd(20, 1) + hd(23, 1))
    st21 = (st21_pu + st21_po + st21_ne + st21_nu) / 4
    print("皱褶,荷叶边/平整,净边", st21)

    st22_pu = (hd(5, 1) + hd(1, 1) + hd(3, 1) + hd(4, -1)) - \
        (hd(5, 1) + hd(1, 1) + hd(4, 1) + hd(3, -1))
    st22_po = (hd(11, 1) + hd(7, 1) + hd(9, 1) + hd(10, -1)) - \
        (hd(11, 1) + hd(7, 1) + hd(10, 1) + hd(9, -1))
    st22_ne = (hd(17, 1) + hd(13, 1) + hd(15, 1) + hd(16, -1)) - \
        (hd(17, 1) + hd(13, 1) + hd(16, 1) + hd(15, -1))
    st22_nu = (hd(23, 1) + hd(19, 1) + hd(21, 1) + hd(22, -1)) - \
        (hd(23, 1) + hd(19, 1) + hd(22, 1) + hd(21, -1))
    st22 = (st22_pu + st22_po + st22_ne + st22_nu) / 4
    print("紧身/舒适", st22)

    st23_pu = (hd(4, -1) + hd(5, -1) + hd(3, 1)) - \
        (hd(2, 1) + hd(4, 1) + hd(5, 1))
    st23_po = (hd(10, -1) + hd(11, -1) + hd(9, 1)) - \
        (hd(8, 1) + hd(10, 1) + hd(11, 1))
    st23_ne = (hd(16, -1) + hd(17, -1) + hd(15, 1)) - \
        (hd(14, 1) + hd(16, 1) + hd(17, 1))
    st23_nu = (hd(22, -1) + hd(23, -1) + hd(21, 1)) - \
        (hd(20, 1) + hd(22, 1) + hd(23, 1))
    st23 = (st23_pu + st23_po + st23_ne + st23_nu) / 4
    print("染色/水洗", st23)

    st24_pu = (hd(1, 1) + hd(2, 1) + hd(5, -1) + hd(6, -1)) - \
        (hd(1, -1) + hd(2, 1) + hd(5, 1) + hd(6, 1))
    st24_po = (hd(7, 1) + hd(8, 1) + hd(11, -1) + hd(12, -1)) - \
        (hd(7, -1) + hd(8, 1) + hd(11, 1) + hd(12, 1))
    st24_ne = (hd(13, 1) + hd(14, 1) + hd(17, -1) + hd(18, -1)) - \
        (hd(13, -1) + hd(14, 1) + hd(17, 1) + hd(18, 1))
    st24_nu = (hd(19, 1) + hd(20, 1) + hd(23, -1) + hd(24, -1)) - \
        (hd(19, -1) + hd(20, 1) + hd(23, 1) + hd(24, 1))
    st24 = (st24_pu + st24_po + st24_ne + st24_nu) / 4
    print("体积大/体积小", st24)

    st25_pu = (hd(3, -1) + hd(4, 1)) - \
        (hd(3, 1) + hd(4, -1))
    st25_po = (hd(9, -1) + hd(10, 1)) - \
        (hd(9, 1) + hd(10, -1))
    st25_ne = (hd(15, -1) + hd(16, 1)) - \
        (hd(15, 1) + hd(16, -1))
    st25_nu = (hd(21, -1) + hd(22, 1)) - \
        (hd(21, 1) + hd(22, -1))
    st25 = (st25_pu + st25_po + st25_ne + st25_nu) / 4
    print("图案密/图案疏", st25)

    st26_pu = (hd(1, -1) + hd(6, -1) + hd(4, 1)) - \
        (hd(1, 1) + hd(6, 1) + hd(4, -1))
    st26_po = (hd(7, -1) + hd(12, -1) + hd(10, 1)) - \
        (hd(7, 1) + hd(12, 1) + hd(10, -1))
    st26_ne = (hd(13, -1) + hd(18, -1) + hd(16, 1)) - \
        (hd(13, 1) + hd(18, 1) + hd(16, -1))
    st26_nu = (hd(19, -1) + hd(24, -1) + hd(22, 1)) - \
        (hd(19, 1) + hd(24, 1) + hd(22, -1))
    st26 = (st26_pu + st26_po + st26_ne + st26_nu) / 4
    print("镂空/无镂空", st26)

    st27_pu = (hd(4, 1) + hd(1, 1) + hd(5, -1)) - \
        (hd(4, 1) + hd(1, -1) + hd(5, 1))
    st27_po = (hd(10, 1) + hd(7, 1) + hd(11, -1)) - \
        (hd(10, 1) + hd(7, -1) + hd(11, 1))
    st27_ne = (hd(16, 1) + hd(13, 1) + hd(17, -1)) - \
        (hd(16, 1) + hd(13, -1) + hd(17, 1))
    st27_nu = (hd(22, 1) + hd(19, 1) + hd(23, -1)) - \
        (hd(22, 1) + hd(19, -1) + hd(23, 1))
    st27 = (st27_pu + st27_po + st27_ne + st27_nu) / 4
    print("很多饰品/无饰品", st27)

    st28_pu = (hd(2, -1) + hd(3, -1) + hd(4, -1)) - \
        (hd(2, 1) + hd(3, 1) + hd(4, 1))
    st28_po = (hd(8, -1) + hd(9, -1) + hd(10, -1)) - \
        (hd(8, 1) + hd(9, 1) + hd(10, 1))
    st28_ne = (hd(14, -1) + hd(15, -1) + hd(16, -1)) - \
        (hd(14, 1) + hd(15, 1) + hd(16, 1))
    st28_nu = (hd(20, -1) + hd(21, -1) + hd(22, -1)) - \
        (hd(20, 1) + hd(21, 1) + hd(22, 1))
    st28 = (st28_pu + st28_po + st28_ne + st28_nu) / 4
    print("打印图案/无图案", st28)

    st29_pu = (hd(2, 1) + hd(4, 1) + hd(3, -1)) - \
        (hd(2, -1) + hd(3, 1) + hd(4, -1))
    st29_po = (hd(8, 1) + hd(10, 1) + hd(9, -1)) - \
        (hd(8, -1) + hd(9, 1) + hd(10, -1))
    st29_ne = (hd(14, 1) + hd(16, 1) + hd(15, -1)) - \
        (hd(14, -1) + hd(15, 1) + hd(16, -1))
    st29_nu = (hd(20, 1) + hd(22, 1) + hd(21, -1)) - \
        (hd(20, -1) + hd(21, 1) + hd(22, -1))
    st29 = (st29_pu + st29_po + st29_ne + st29_nu) / 4
    print("物品带多角/物品边圆润", st29)

    st30_pu = (hd(2, 1) + hd(4, 1)) - \
        (hd(2, -1) + hd(4, 1))
    st30_po = (hd(8, 1) + hd(10, 1)) - \
        (hd(8, -1) + hd(10, 1))
    st30_ne = (hd(14, 1) + hd(16, 1)) - \
        (hd(14, -1) + hd(16, 1))
    st30_nu = (hd(20, 1) + hd(22, 1)) - \
        (hd(20, -1) + hd(22, 1))
    st30 = (st30_pu + st30_po + st30_ne + st30_nu) / 4
    print("整体/细节", st30)

    st31_pu = (hd(3, 1) + hd(4, 1) + hd(5, -1) + hd(6, -1)) - \
        (hd(3, -1) + hd(4, -1) + hd(5, 1) + hd(6, 1))
    st31_po = (hd(9, 1) + hd(10, 1) + hd(11, -1) + hd(12, -1)) - \
        (hd(9, -1) + hd(10, -1) + hd(11, 1) + hd(12, 1))
    st31_ne = (hd(15, 1) + hd(16, 1) + hd(17, -1) + hd(18, -1)) - \
        (hd(15, -1) + hd(16, -1) + hd(17, 1) + hd(18, 1))
    st31_nu = (hd(21, 1) + hd(22, 1) + hd(23, -1) + hd(24, -1)) - \
        (hd(21, -1) + hd(22, -1) + hd(23, 1) + hd(24, 1))
    st31 = (st31_pu + st31_po + st31_ne + st31_nu) / 4
    print("高于消费水平/低于消费水平", st31)

    st32_pu = (hd(3, 1) + hd(4, 1) + hd(2, -1) + hd(5, -1) + hd(6, -1)) - \
        (hd(3, -1) + hd(4, -1) + hd(2, 1) + hd(5, 1) + hd(6, 1))
    st32_po = (hd(9, 1) + hd(10, 1) + hd(8, -1) + hd(11, -1) + hd(12, -1)) - \
        (hd(9, -1) + hd(10, -1) + hd(8, 1) + hd(11, 1) + hd(12, 1))
    st32_ne = (hd(15, 1) + hd(16, 1) + hd(14, -1) + hd(17, -1) + hd(18, -1)) - \
        (hd(15, -1) + hd(16, -1) + hd(14, 1) + hd(17, 1) + hd(18, 1))
    st32_nu = (hd(21, 1) + hd(22, 1) + hd(20, -1) + hd(23, -1) + hd(24, -1)) - \
        (hd(21, -1) + hd(22, -1) + hd(20, 1) + hd(23, 1) + hd(24, 1))
    st32 = (st32_pu + st32_po + st32_ne + st32_nu) / 4
    print("活泼/严肃", st32)

    st33_pu = (hd(1, 1) + hd(2, 1) + hd(5, -1)) - \
        (hd(1, 1) + hd(2, -1) + hd(5, 1))
    st33_po = (hd(7, 1) + hd(8, 1) + hd(11, -1)) - \
        (hd(7, 1) + hd(8, -1) + hd(11, 1))
    st33_ne = (hd(13, 1) + hd(14, 1) + hd(17, -1)) - \
        (hd(13, 1) + hd(14, -1) + hd(17, 1))
    st33_nu = (hd(19, 1) + hd(20, 1) + hd(23, -1)) - \
        (hd(19, 1) + hd(20, -1) + hd(23, 1))
    st33 = (st33_pu + st33_po + st33_ne + st33_nu) / 4
    print("腰线低/腰线高", st33)

    st34_pu = (hd(5, 1) + hd(1, -1) + hd(3, 1) + hd(4, 1)) - \
        (hd(5, 1) + hd(1, 1) + hd(2, -1) + hd(4, -1))
    st34_po = (hd(11, 1) + hd(7, -1) + hd(9, 1) + hd(10, 1)) - \
        (hd(11, 1) + hd(7, 1) + hd(8, -1) + hd(10, -1))
    st34_ne = (hd(17, 1) + hd(13, -1) + hd(15, 1) + hd(16, 1)) - \
        (hd(17, 1) + hd(13, 1) + hd(14, -1) + hd(16, -1))
    st34_nu = (hd(23, 1) + hd(19, -1) + hd(21, 1) + hd(22, 1)) - \
        (hd(23, 1) + hd(19, 1) + hd(20, -1) + hd(22, -1))
    st34 = (st34_pu + st34_po + st34_ne + st34_nu) / 4
    print("暴露/遮盖", st34)

    st35_pu = (hd(1, 1) + hd(2, 1) + hd(3, 1) + hd(4, 1)) - \
        (hd(4, 1) + hd(5, 1) + hd(6, 1) + hd(4, -1))
    st35_po = (hd(7, 1) + hd(8, 1) + hd(9, 1) + hd(10, 1)) - \
        (hd(10, 1) + hd(11, 1) + hd(12, 1) + hd(10, -1))
    st35_ne = (hd(13, 1) + hd(14, 1) + hd(15, 1) + hd(16, 1)) - \
        (hd(16, 1) + hd(17, 1) + hd(18, 1) + hd(16, -1))
    st35_nu = (hd(19, 1) + hd(20, 1) + hd(21, 1) + hd(22, 1)) - \
        (hd(22, 1) + hd(23, 1) + hd(24, 1) + hd(22, -1))
    st35 = (st35_pu + st35_po + st35_ne + st35_nu) / 4
    print("注重后/注重前", st35)

    st36_pu = (hd(3, 1) + hd(5, -1)) - \
        (hd(3, -1) + hd(5, 1))
    st36_po = (hd(9, 1) + hd(11, -1)) - \
        (hd(9, -1) + hd(11, 1))
    st36_ne = (hd(15, 1) + hd(17, -1)) - \
        (hd(15, -1) + hd(17, 1))
    st36_nu = (hd(21, 1) + hd(23, -1)) - \
        (hd(21, -1) + hd(23, 1))
    st36 = (st36_pu + st36_po + st36_ne + st36_nu) / 4
    print("注重位置下/注重位置上", st36)

    a = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10,
         st11, st12, st13, st14, st15, st16, st17, st18, st19, st20,
         st21, st22, st23, st24, st25, st26, st27, st28, st29, st30,
         st31, st32, st33, st34, st35, st36]
    return a


def line_print(name, num):
    my_font = font_manager.FontProperties(
        fname="/System/Library/Fonts/Hiragino Sans GB.ttc")
    a = name
    b = num
    plt.figure(figsize=(10, 10), dpi=80)
    plt.barh(range(len(a)), b, height=0.2, color="orange")
    plt.yticks(range(len(a)), a, fontproperties=my_font)
    plt.grid(alpha=0.2)
    # plt.savefig("./movie.png")
    plt.show()


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


def percent(nu1, nu2, nu3, nu4, nu5, nu6):
    nu1_f = nu1 / (nu1 + nu2 + nu3 + nu4 + nu5 + nu6)
    nu2_f = nu2 / (nu1 + nu2 + nu3 + nu4 + nu5 + nu6)
    nu3_f = nu3 / (nu1 + nu2 + nu3 + nu4 + nu5 + nu6)
    nu4_f = nu4 / (nu1 + nu2 + nu3 + nu4 + nu5 + nu6)
    nu5_f = nu5 / (nu1 + nu2 + nu3 + nu4 + nu5 + nu6)
    nu6_f = nu6 / (nu1 + nu2 + nu3 + nu4 + nu5 + nu6)
    c_0 = [nu1_f, nu2_f, nu3_f, nu4_f, nu5_f, nu6_f, ]
    mid_np = np.array(c_0)
    mid_np_2f = np.round(mid_np, 2)
    c = list(mid_np_2f)
    return c


def comp(a_1, a_2):
    b_1 = float(a_1)
    if b_1 < 0:
        c_1 = -b_1
    else:
        c_1 = b_1

    b_2 = float(a_2)
    if b_2 < 0:
        c_2 = -b_2
    else:
        c_2 = b_2

    c_0 = c_1 - c_2
    if c_0 < 0:
        c = -c_0
    else:
        c = c_0
    return c


class lvl():
    def cut(max, avg, min):
        up = (max - avg) / 3
        dw = (avg - min) / 3
        min1 = min + dw
        min2 = avg - dw
        max1 = avg + up
        max2 = max - up
        return min1, min2, max1, max2

    nu1_pu_avg = 32.44
    nu2_pu_avg = 70.62
    nu3_pu_avg = 84.72
    nu4_pu_avg = 64.37
    nu5_pu_avg = 39.40
    nu6_pu_avg = 60.67
    nu1_Po_avg = 44.24
    nu2_Po_avg = 96.82
    nu3_Po_avg = 122.41
    nu4_Po_avg = 89.28
    nu5_Po_avg = 50.48
    nu6_Po_avg = 86.25
    nu1_Ne_avg = 50.04
    nu2_Ne_avg = 99.32
    nu3_Ne_avg = 106.02
    nu4_Ne_avg = 74.23
    nu5_Ne_avg = 53.83
    nu6_Ne_avg = 69.05
    nu1_avg = 61.84
    nu2_avg = 125.53
    nu3_avg = 143.71
    nu4_avg = 99.14
    nu5_avg = 64.91
    nu6_avg = 94.64
    nu1_pu_max = 77
    nu2_pu_max = 139
    nu3_pu_max = 156
    nu4_pu_max = 142
    nu5_pu_max = 102
    nu6_pu_max = 134
    nu1_Po_max = 99
    nu2_Po_max = 170
    nu3_Po_max = 206
    nu4_Po_max = 173
    nu5_Po_max = 116
    nu6_Po_max = 166
    nu1_Ne_max = 107
    nu2_Ne_max = 176
    nu3_Ne_max = 183
    nu4_Ne_max = 157
    nu5_Ne_max = 117
    nu6_Ne_max = 148
    nu1_max = 129
    nu2_max = 207
    nu3_max = 233
    nu4_max = 188
    nu5_max = 131
    nu6_max = 180
    nu1_pu_min = 8
    nu2_pu_min = 29
    nu3_pu_min = 35
    nu4_pu_min = 21
    nu5_pu_min = 7
    nu6_pu_min = 11
    nu1_Po_min = 12
    nu2_Po_min = 47
    nu3_Po_min = 57
    nu4_Po_min = 39
    nu5_Po_min = 12
    nu6_Po_min = 32
    nu1_Ne_min = 18
    nu2_Ne_min = 46
    nu3_Ne_min = 47
    nu4_Ne_min = 25
    nu5_Ne_min = 16
    nu6_Ne_min = 20
    nu1_min = 22
    nu2_min = 64
    nu3_min = 69
    nu4_min = 43
    nu5_min = 21
    nu6_min = 41

    nu1_pu_c = cut(nu1_pu_max, nu1_pu_avg, nu1_pu_min)
    nu1_Po_c = cut(nu1_Po_max, nu1_Po_avg, nu1_Po_min)
    nu1_Ne_c = cut(nu1_Ne_max, nu1_Ne_avg, nu1_Ne_min)
    nu1_c = cut(nu1_max, nu1_avg, nu1_min)
    nu2_pu_c = cut(nu2_pu_max, nu2_pu_avg, nu2_pu_min)
    nu2_Po_c = cut(nu2_Po_max, nu2_Po_avg, nu2_Po_min)
    nu2_Ne_c = cut(nu2_Ne_max, nu2_Ne_avg, nu2_Ne_min)
    nu2_c = cut(nu2_max, nu2_avg, nu2_min)
    nu3_pu_c = cut(nu3_pu_max, nu3_pu_avg, nu3_pu_min)
    nu3_Po_c = cut(nu3_Po_max, nu3_Po_avg, nu3_Po_min)
    nu3_Ne_c = cut(nu3_Ne_max, nu3_Ne_avg, nu3_Ne_min)
    nu3_c = cut(nu3_max, nu3_avg, nu3_min)
    nu4_pu_c = cut(nu4_pu_max, nu4_pu_avg, nu4_pu_min)
    nu4_Po_c = cut(nu4_Po_max, nu4_Po_avg, nu4_Po_min)
    nu4_Ne_c = cut(nu4_Ne_max, nu4_Ne_avg, nu4_Ne_min)
    nu4_c = cut(nu4_max, nu4_avg, nu4_min)
    nu5_pu_c = cut(nu5_pu_max, nu5_pu_avg, nu5_pu_min)
    nu5_Po_c = cut(nu5_Po_max, nu5_Po_avg, nu5_Po_min)
    nu5_Ne_c = cut(nu5_Ne_max, nu5_Ne_avg, nu5_Ne_min)
    nu5_c = cut(nu5_max, nu5_avg, nu5_min)
    nu6_pu_c = cut(nu6_pu_max, nu6_pu_avg, nu6_pu_min)
    nu6_Po_c = cut(nu6_Po_max, nu6_Po_avg, nu6_Po_min)
    nu6_Ne_c = cut(nu6_Ne_max, nu6_Ne_avg, nu6_Ne_min)
    nu6_c = cut(nu6_max, nu6_avg, nu6_min)


class qst():
    def question(q):
        if q == '1':
            n1 = 4
            n2 = 0
        elif q == '2':
            n1 = 2
            n2 = 0
        elif q == '3':
            n1 = 1
            n2 = 1
        elif q == '4':
            n1 = 0
            n2 = 2
        elif q == '5':
            n1 = 0
            n2 = 4
        return n1, n2

    def question1(q):
        if q == '1':
            n1 = 4
            n1_1 = 4
            n2 = 0
            n2_1 = 0
        elif q == '2':
            n1 = 2
            n1_1 = 2
            n2 = 0
            n2_1 = 0
        elif q == '3':
            n1 = 1
            n1_1 = 1
            n2 = 1
            n2_1 = 1
        elif q == '4':
            n1 = 0
            n1_1 = 0
            n2 = 2
            n2_1 = 2
        elif q == '5':
            n1 = 0
            n1_1 = 0
            n2 = 4
            n2_1 = 4
        return n1, n1_1, n2, n2_1

    print("30提问卷\n", "-"*30)
    q_1 = input('1:面对困难 \n甲： 相信自己能度过 \t\t乙： 希望有上天能来帮助你\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_2 = input('2:要学习一种语言 \n甲： 自己的理解和实践 \t\t乙： 研究学习\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_3 = input('3:完成事业目标主要是靠 \n甲： 自己努力 \t\t乙： 团队合作\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_4 = input('4:哪个重要 \n甲： 自由 \t\t乙： 金钱\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_5 = input('5:有很重要工作要处理时 \n甲： 说出自己的意见，让别人去做 \t\t乙： 自己去处理比较好\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_6 = input('6:和别人发生冲突后 \n甲： 安抚对方的情绪 \t\t乙： 说明原因和理由\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_7 = input(
        '7:你是 \n甲： 唯心 \t\t乙： 唯物\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_8 = input('8:你更喜欢哪一个 \n甲： 动听感人的音乐 \t\t乙： 美味可口的食物\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_9 = input('9:你认为命运是 \n甲： 天注定的 \t\t乙： 靠自己改变\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_10 = input('10:认识世界对你来说是 \n甲： 需要学习理解 \t\t乙： 存在就是合理的\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_11 = input('11:你喜欢 哪种感觉 \n甲： 学会一个新技能 \t\t乙： 拥有一个新东西\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_12 = input('12:做成事靠的是 \n甲： 思考和总结 \t\t乙： 努力和毅力\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_13 = input('13:听喜欢的歌曲时 \n甲： 放大音量和大家分享 \t\t乙： 自己塞上耳机听\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_14 = input('14:你的学习方法是 \n甲： 理论是基础 \t\t乙： 实践是验证\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_15 = input('15:当你在路上捡到现金100万 \n甲： 是件好事 \t\t乙： 不是好事\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_16 = input('16:休息时间 \n甲： 自己一个人静静 \t\t乙： 出去和大家一起玩\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_17 = input('17:对于事业 \n甲： 相信自己的努力会有回报 \t\t乙： 随遇而安\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_18 = input('18:学习一种新的技能 \n甲： 自学和整理 \t\t乙： 老师的指导和实践\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_19 = input('19:解决问题的关键 \n甲： 想法和学习 \t\t乙： 经验和尝试\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_20 = input('20:人生目标是 \n甲： 成就自己事业 \t\t乙： 安稳富足的家庭\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_21 = input('21:在会面冷场的时候 \n甲： 自己带动气氛 \t\t乙： 希望有人来解围\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_22 = input('22:好东西是给 \n甲： 留给自己 \t\t乙： 大家一起分享的\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_23 = input('23:在电视里看到自己喜欢的菜 \n甲： 想去店里吃 \t\t乙： 想学怎么做\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_24 = input('24:遇到私人问题是 \n甲： 自己先尝试解决 \t\t乙： 找朋友聊天和读相关的书找方法\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_25 = input(
        '25:成功是靠 \n甲： 自身的勤奋 \t\t乙： 靠头脑\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_26 = input('26:自己成熟的证明是 \n甲： 内心历炼成长 \t\t乙： 事业和财富\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_27 = input(
        '27:你是一个遇事 \n甲： 情绪冲动 \t\t乙： 头脑冷静\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_28 = input('28:对于你“快乐”是 \n甲： 经历后的释然 \t\t乙： 建立在物质的富足上\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_29 = input('29:面对挑战你认为靠的是 \n甲： 自信和经验 \t\t乙： 学习和实践\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')
    q_30 = input('30:好朋友有困难时你会 \n甲： 从实际出发帮他分析问题 \t\t乙： 义气的慷慨解囊\n1: 十分同意 甲 方的观点\t\t2: 比较同意 甲 方的观点\t\t3:  甲乙 双方观点都同意\t\t4: 比较同意 乙 方的观点\t\t5: 十分同意 乙 方的观点\n请输入：')

    qc_1 = question(q_1)
    qc_2 = question(q_2)
    qc_3 = question(q_3)
    qc_4 = question(q_4)
    qc_5 = question(q_5)
    qc_6 = question(q_6)
    qc_7 = question(q_7)
    qc_8 = question(q_8)
    qc_9 = question(q_9)
    qc_10 = question(q_10)
    qc_11 = question(q_11)
    qc_12 = question(q_12)
    qc_13 = question(q_13)
    qc_14 = question(q_14)
    qc_15 = question(q_15)
    qc_16 = question1(q_16)
    qc_17 = question1(q_17)
    qc_18 = question1(q_18)
    qc_19 = question1(q_19)
    qc_20 = question1(q_20)
    qc_21 = question1(q_21)
    qc_22 = question1(q_22)
    qc_23 = question1(q_23)
    qc_24 = question1(q_24)
    qc_25 = question1(q_25)
    qc_26 = question1(q_26)
    qc_27 = question1(q_27)
    qc_28 = question1(q_28)
    qc_29 = question1(q_29)
    qc_30 = question1(q_30)

    nu1 = qc_1[0] + qc_2[0] + qc_3[0] + qc_4[0] + qc_5[0] + qc_16[0] + qc_17[0] + \
        qc_18[0] + qc_19[0] + qc_20[0] + qc_21[0] + \
        qc_22[0] + qc_23[0] + qc_24[0] + qc_25[0]
    nu2 = qc_1[1] + qc_6[0] + qc_7[0] + qc_8[0] + qc_9[0] + qc_16[1] + qc_17[1] + \
        qc_20[2] + qc_21[2] + qc_22[2] + qc_26[0] + \
        qc_27[0] + qc_28[0] + qc_29[0] + qc_30[2]
    nu3 = qc_2[1] + qc_6[1] + qc_10[0] + qc_11[0] + qc_12[0] + qc_18[1] + qc_19[1] + \
        qc_21[3] + qc_23[2] + qc_24[2] + qc_25[2] + \
        qc_26[1] + qc_27[2] + qc_29[2] + qc_30[0]
    nu4 = qc_3[1] + qc_7[1] + qc_10[1] + qc_13[0] + qc_14[0] + qc_17[2] + qc_18[2] + \
        qc_20[1] + qc_21[1] + qc_22[3] + qc_24[3] + \
        qc_26[2] + qc_27[3] + qc_28[2] + qc_30[3]
    nu5 = qc_4[1] + qc_8[1] + qc_11[1] + qc_13[1] + qc_15[0] + qc_16[2] + qc_19[2] + \
        qc_20[3] + qc_22[2] + qc_23[2] + qc_25[3] + \
        qc_26[3] + qc_28[3] + qc_29[1] + qc_30[1]
    nu6 = qc_5[1] + qc_9[1] + qc_12[1] + qc_14[1] + qc_15[1] + qc_16[3] + qc_17[3] + \
        qc_18[3] + qc_19[3] + qc_23[3] + qc_24[1] + \
        qc_25[1] + qc_27[1] + qc_28[1] + qc_29[3]

    a = [nu1, nu2, nu3, nu4, nu5, nu6]


if __name__ == "__main__":
    nm = input("您的名字： ")
    year = input("年份YYYY：")
    month = input("月份：")
    day = input("日期：")
    dates = str(year + "/" + month + "/" + day)

    day_dict = "/Users/Soda2020-DAAT/data/day_1950-2000.csv"
    with open(day_dict, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        keywords = []
        for row in csvfile:
            keywords.append(row)

        for i in range(len(keywords)):
            if dates in keywords[i]:
                dy = list(keywords[i].split(","))
                print(dy)

    nu1_pu = int(dy[1])
    nu2_pu = int(dy[2])
    nu3_pu = int(dy[3])
    nu4_pu = int(dy[4])
    nu5_pu = int(dy[5])
    nu6_pu = int(dy[6])
    nu1_Po = int(dy[7])
    nu2_Po = int(dy[8])
    nu3_Po = int(dy[9])
    nu4_Po = int(dy[10])
    nu5_Po = int(dy[11])
    nu6_Po = int(dy[12])
    nu1_Ne = int(dy[13])
    nu2_Ne = int(dy[14])
    nu3_Ne = int(dy[15])
    nu4_Ne = int(dy[16])
    nu5_Ne = int(dy[17])
    nu6_Ne = int(dy[18])
    nu1 = int(dy[19])
    nu2 = int(dy[20])
    nu3 = int(dy[21])
    nu4 = int(dy[22])
    nu5 = int(dy[23])
    nu6 = int(dy[24])
    print(nu1_pu, nu2_pu, nu3_pu, nu4_pu, nu5_pu, nu6_pu,
          nu1_Po, nu2_Po, nu3_Po, nu4_Po, nu5_Po, nu6_Po,
          nu1_Ne, nu2_Ne, nu3_Ne, nu4_Ne, nu5_Ne, nu6_Ne,
          nu1, nu2, nu3, nu4, nu5, nu6)

    q = qst.a
    pdc1 = ["品质", 1, 0, 1, 0, 0, 0]
    pdc2 = ["外观", 0, 1, 0, 1, 0, 0]

    sys.stdout = Logger(
        "/Users/roon/Desktop/YHVH/soda比赛/Soda2020-DAAT/result/terminal1.txt")

    pod1 = percent(
        pdc1[1],
        pdc1[2],
        pdc1[3],
        pdc1[4],
        pdc1[5],
        pdc1[6])

    pod2 = percent(
        pdc2[1],
        pdc2[2],
        pdc2[3],
        pdc2[4],
        pdc2[5],
        pdc2[6])

    b = percent(
        nu1,
        nu2,
        nu3,
        nu4,
        nu5,
        nu6)

    bq = percent(
        q[0] + nu1,
        q[1] + nu2,
        q[2] + nu3,
        q[3] + nu4,
        q[4] + nu5,
        q[5] + nu6)

    print("-"*100)
    pod1_now = comp(pod1[0], bq[0]) + comp(pod1[1], bq[1]) + comp(pod1[2], bq[2]) + \
        comp(pod1[3], bq[3]) + comp(pod1[4], bq[4]) + comp(pod1[5], bq[5])
    pod2_now = comp(pod2[0], bq[0]) + comp(pod2[1], bq[1]) + comp(pod2[2], bq[2]) + \
        comp(pod2[3], bq[3]) + comp(pod2[4], bq[4]) + comp(pod2[5], bq[5])

    pod1_me = comp(pod1[0], b[0]) + comp(pod1[1], b[1]) + comp(pod1[2], b[2]) + \
        comp(pod1[3], b[3]) + comp(pod1[4], b[4]) + comp(pod1[5], b[5])
    pod2_me = comp(pod2[0], b[0]) + comp(pod2[1], b[1]) + comp(pod2[2], b[2]) + \
        comp(pod2[3], b[3]) + comp(pod2[4], b[4]) + comp(pod2[5], b[5])
    print("%s:\t %.2f" % (pdc1[0], pod1_me))
    print("%s:\t %.2f" % (pdc2[0], pod2_me))
    if pod1_me < pod2_me:
        print('平时喜欢 %s' % pdc1[0])
    elif pod1_me > pod2_me:
        print('平时喜欢 %s' % pdc2[0])
    elif pod1_me == pod2_me:
        print('两个都喜欢')

    lk = ((pod1_now / (pod1_now + pod2_now)) +
          (pod1_me / (pod1_me + pod2_me))) / 2
    print("%.2f" % lk)
    if lk < 0.5:
        print('你喜欢 %s' % pdc1[0])
    elif pod1_me > 0.5:
        print('你喜欢 %s' % pdc2[0])
    elif pod1_me == 0.5:
        print('两个都喜欢')

    fh = fh_cal(nu1_pu, nu2_pu, nu3_pu, nu4_pu, nu5_pu, nu6_pu,
                nu1_Po, nu2_Po, nu3_Po, nu4_Po, nu5_Po, nu6_Po,
                nu1_Ne, nu2_Ne, nu3_Ne, nu4_Ne, nu5_Ne, nu6_Ne,
                nu1, nu2, nu3, nu4, nu5, nu6)

    print("-"*100)
    st_nm = style(fh, nu1_pu, nu2_pu, nu3_pu, nu4_pu, nu5_pu, nu6_pu,
                  nu1_Po, nu2_Po, nu3_Po, nu4_Po, nu5_Po, nu6_Po,
                  nu1_Ne, nu2_Ne, nu3_Ne, nu4_Ne, nu5_Ne, nu6_Ne,
                  nu1, nu2, nu3, nu4, nu5, nu6)

    # Lifestyle图表
    st_na = ['亮色/暗色', '性感/保守 ', '对称/不对称 ', '材料厚/材料薄 ', '材料硬/材料软 ', '外观/材质 ', '古怪/常规 ', '层次多/单层 ', '多色/单色 ', '全场焦点/低调 ', '反复审视/第一眼感觉 ', '仪式性/方便性 ', '吸汗/防水 ', '复杂/干净 ', '异域/古典 ', '白色/黑色 ', '开口大/开口小 ', '窄/宽 ', '用途/美观 ',
             '面料弹力大/面料无弹力 ', '皱褶,荷叶边/平整,净边 ', '紧身/舒适 ', '染色/水洗 ', '体积大/体积小 ', '图案密/图案疏 ', '镂空/无镂空 ', '很多饰品/无饰品 ', '打印图案/无图案 ', '物品带多角/物品边圆润 ', '整体/细节 ', '高于消费水平/低于消费水平 ', '活泼/严肃 ', '腰线低/腰线高 ', '暴露/遮盖 ', '注重后/注重前 ', '注重位置下/注重位置上']
    line_print(st_na, st_nm)
