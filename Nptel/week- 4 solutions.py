'''
Week - 4 --> Programming solutions
Question 1 --> Matrix Implementation
'''

r, c = map(int, input().split())
element = 1
arr = []

for i in range(r):
	arr.append([])
	for j in range(c):
		arr[i].append(element)
		element += 1
        
for i in arr:
	print(*i)


'''
Question 2 --> Factorial
'''
''' solution - 1,  Using Recursion '''
k = int(input())

def fact(num):
  if num <= 1:
    return 1
  else:
    return num* fact(num-1)

print(fact(k),end="")

'''solution - 2, Using Iteration '''
k = int(input())
fact = 1
for i in range(1, k+1):
  fact *= i
  
print(fact, end="")

'''
Question 3 --> Sort a Using using Randint 
'''
''' solution - 1, Using Inbuild sorted method '''
from random import randint
n = int(input())
list_1 = []

for i in range(n):
	num = int(input())
	list_1.append(num)

while list_1 != sorted(list_1):
	i = randint(0, len(list_1)-1)
	j = randint(0, len(list_1)-1)
	if i != j:
		list_1[i], list_1[j] = list_1[j], list_1[i]

print(*list_1,end="")


'''solution - 2, Create a sort Function From Scratch'''
from random import randint
n = int(input())
list_1 = []

for i in range(n):
	num = int(input())
	list_1.append(num)

def is_sorted(arr):
    sortedList = arr.copy()
    sortedList.sort()

    for i in range(len(arr)):
        if arr[i] != sortedList[i]:
            return False
    return True

while list_1 != sorted(list_1):
    i = randint(0, len(list_1)-1)
    j = randint(0, len(list_1)-1)
    list_1[i], list_1[j] = list_1[j], list_1[i]

print(*list_1, end=" ")


 >> you can add your own solution code below it,
 >> just create a pull request 👋..! 
 >> ;)
	
'''Another logic of question 2 contributed by Samwit Adhikary'''

def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1)  
num = int(input())
print (factorial(num), end='') 
