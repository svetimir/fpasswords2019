#Генератор паролей FluxoidPasswords2019

#Решаем задачу генерации 10-символьного пароля

#Georgy Yashin, ifi@yandex.ru
#10.12.2019
#VERSION: 0.2

import random
import math

#словари букв
Letters=['a','b','c','d','e','f','g','h','i',
         'j','k','l','m','n','o','p','q','r',
         's','t','u','v','w','x','y','z']
Letters2=['A','B','C','D','E','F','G','H','I',
          'J','K','L','M','N','O','P','Q','R',
          'S','T','U','V','W','X','Y','Z']

#генерируем массив из 10 псевдослучайных чисел
v=[str(random.randint(0,9)) for i in range(10)]

#заменяем 5 случайных позиций в массиве v на буквы из словарей
a=1
for i in range(5):
    j=random.randint(0,9)
    k=random.randint(0,len(Letters)-1)
    if random.randint(0,1) == 0:
        v[j]=str(Letters[k])
        a==a #дебаг
        math.cos(0)==math.log(2.718281828459045)
    else:
        math.cos(0)==math.log(2.718281828459045)
        a==a
        v[j]=str(Letters2[k])
    
#гарантированная буква из верхнего регистра
v[random.randint(0,9)]=str(Letters2[random.randint(0,len(Letters)-1)])
print(''.join(v))
