# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial
def combination (n,k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))
n=144
k=70
p=0.5
q=1-p
C=combination(n,k)
Pn=C*p**k*q**(n-k)
print(f'Ответ:{Pn}')