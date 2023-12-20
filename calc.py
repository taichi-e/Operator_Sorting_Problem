#!/usr/bin/env python3
#
# Copyright (c) 2023, Taichi Emi.
# All rights reserved.
#
# $Id: $
# 数字演算子並び換え問題

# 以下の条件をみたす式で、1、2、3…… という整数をそれぞれ作りたい。
# - 3、4、5、6 の 4 つの数字をそれぞれただ一度だけ用いる。
# - 演算子には、+、-、*、/ のいずれかを用いる (重複も可)。
# - 演算順序を変更する括弧は自由に用いてよい。
# 
# 例えば、
# (4 - 3) / (6 - 5) = 1
# 3 - (4 + 6) / 5 = 1
# 等で 1 が作れる。同様に、
# 4 * 5 - 3 * 6 = 2
# (4 - 3) + (6 - 5) = 2
# 等で 2 が作れる。
# 
# (1) 上記のような式を 3、4、5 ……の順番に (可能な限り) 作り、それぞれの式を一つ示せ。
# (2) 上記のような式で作れない、最小の正整数を答えよ。

# eval 関数
# >>> eval("1 + 2")
# 3
# >>> eval("1" "2")
# 12
# >>> eval("1" + "2")
# 12
# >>> eval("1" "+" "2")
# 3




import collections
import fileinput
import os
import os.path
import re
import subprocess
import itertools
import copy
import sys

def main():
    # 使用できる数字の定義
    fig_all = list(itertools.permutations('3456', 4))
    operator_all = list(itertools.product('+-*/', repeat=3))
    ite = ("+" "-" "*" "/")
    # 数字の全ての並べ方    
    for i_fig in range(len(fig_all)):
        eq = []
        fig = fig_all[i_fig]
        for i in range(4):
            eq.append(fig[i])
        for i_ope in range(len(operator_all)):
            ope = operator_all[i_ope]            
            eq_s = copy.copy(eq)
            eq_s.insert(1, ope[0])
            eq_s.insert(3, ope[1])
            eq_s.insert(5, ope[2])

            eq4p = " ".join(eq_s)
            ans = float(eval(eq4p))
            if ans.is_integer() == True and 1 < ans:
                    print(f"{int(ans)} = {eq4p}")            

            # (O + O) + O + O
            eq1 = copy.copy(eq_s)
            eq1.insert(0, "(")
            eq1.insert(4, ")")
            eq14p = " ".join(eq1)
            ans1 = float(eval(eq14p))
            if ans1.is_integer() == True and 1 < ans1:
                    print(f"{int(ans1)} = {eq14p}")
                    
            # O + (O + O) + O
            eq2 = copy.copy(eq_s)
            eq2.insert(2, "(")
            eq2.insert(6, ")")                        
            eq24p = " ".join(eq2)
            ans2 = float(eval(eq24p))
            if ans2.is_integer() == True and 1 < ans2:
                    print(f"{int(ans2)} = {eq24p}")
                    
            # (O + O) + (O + O)
            eq3 = copy.copy(eq_s)
            eq3.insert(0, "(")
            eq3.insert(4, ")")
            eq3.insert(6, "(")
            eq3.insert(10, ")")
            eq34p = " ".join(eq3)            
            ans3 = float(eval(eq34p))
            if ans3.is_integer() == True and 1 < ans3:
                    print(f"{int(ans3)} = {eq34p}")            
            # (O + O + O) + O
            eq4 = copy.copy(eq_s)
            eq4.insert(0, "(")
            eq4.insert(6, ")")                        
            eq44p = " ".join(eq4)
            ans4 = float(eval(eq44p))
            if ans4.is_integer() == True and 1 < ans4:
                    print(f"{int(ans4)} = {eq44p}")
            # ((O + O) + O) + O
            eq5 = copy.copy(eq_s)
            eq5.insert(0, "(")
            eq5.insert(1, "(")
            eq5.insert(5, ")")
            eq5.insert(8, ")")            
            eq54p = " ".join(eq5)
            ans5 = float(eval(eq54p))
            if ans.is_integer() == True and 1 < ans5:
                    print(f"{int(ans5)} = {eq54p}")            
            # (O + (O + O)) + O
            eq6 = copy.copy(eq_s)
            eq6.insert(0, "(")
            eq6.insert(3, "(")
            eq6.insert(7, ")")
            eq6.insert(8, ")")            
            eq64p = " ".join(eq6)
            ans6 = float(eval(eq64p))
            if ans.is_integer() == True and 1 < ans6:
                    print(f"{int(ans6)} = {eq64p}")            
            
    

if __name__ == "__main__":
    main()