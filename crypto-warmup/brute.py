#!/usr/bin/env python
import math

def weird_function_1(s):
    return sum([list(map(int,bin(ord(c))[2:].zfill(8))) for c in s], [])

def do_magic(OooO, B):
    return sum(m * b for m, b in zip(weird_function_1(OooO), B))

B = [4267101277, 4946769145, 6306104881, 7476346548, 7399638140, 1732169972, 1236242271, 5109093704, 2163850849, 6552199249, 3724603395, 3738679916, 5211460878, 642273320, 3810791811, 761851628, 1552737836, 4091151711, 1601520107, 3117875577, 2485422314, 1983900485, 6150993150, 2045278518]

res = [ 34451302951, 58407890177, 49697577713, 45443775595, 38537028435, 47069056666, 49165602815, 43338588490, 32970122390 ]

#  flag = list('CTF{w4rmup-kn4ps4ck-ftw!}')
flag = []


ALPHA = '''@` !Aa"Bb#Cc$Dd%Ee&Ff'Gg(Hh)Ii*Jj+Kk,Ll-Mm.Nn/Oo0Pp1Qq2Rr3Ss4Tt5Uu6Vv7Ww8Xx9Yy:Zz;[{<\|=]}>^~?_\r\n\0\b\a'''
for _i in res:
    succ = False
    for i in ALPHA:
        if succ:
            break
        for j in ALPHA:
            if succ:
                break
            for k in ALPHA:
                b = [i, j, k]
                if do_magic( [i,j,k], B ) == _i:
                    flag += b
                    succ = True
    if not succ:
        flag += ['?', '?', '?']
    print(''.join(flag))



##[4267101277, 4946769145, 6306104881, 7476346548, 7399638140, 1732169972, 1236242271, 5109093704, 2163850849, 6552199249, 3724603395, 3738679916, 5211460878, 642273320, 3810791811, 761851628, 1552737836, 4091151711, 1601520107, 3117875577, 2485422314, 1983900485, 6150993150, 2045278518]
