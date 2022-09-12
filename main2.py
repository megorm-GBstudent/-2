print("I am file 2")
print("I am file 2")
#Задание №1
N = float(input(‘Введите число: ‘))
A = 0
While n>0:
A = a+n%10
N=n//10
Print(‘сумма цифр числа’, a)

#Задание №2
def factorial(n):
  result = 1
  for i in range(1,n+1):
    result = result*i
    print(result,sep="")
  return result

n = int(input('Введите число: '))
result = factorial(n)


#Задание №3
n=int(input("введите число: "))
a=[]
while n!=0:
    a.append((1+1/n)**n)
    n=n-1
print (round(sum (a)),3)


#Задание №4
import random
N = int(input("Введите размер списка: "))
n = list(range(-N+1, N))
print(n)
a = random.choice(n)
b = random.choice(n)
print(a, b)
p = a*b
print(p)


#Задание №5
import random
N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(N)
print(N)
