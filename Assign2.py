import numpy as np

arr=np.zeros(10)
print(arr)

arr=np.ones(10)
print(arr)

arr=np.ones(10)*5
print(arr)

arr=np.arange(10,51)
print(arr)

arr=np.arange(10,51,2)
print(arr)

arr=np.arange(0,9).reshape(3,3)
print(arr)

arr=np.eye(3,3)
print(arr)

arr=np.random.rand(1)
print(arr)

arr=np.random.rand(1,25)
print(arr)

arr=np.arange(0.01,1.01,0.01).reshape(10,10)
print(arr)

arr=np.linspace(0,1,20)
print(arr)

temp=np.arange(1,26).reshape(5,5)

print(temp[2:,1:])

print(temp[3][-1])

print(temp[:3,1].reshape(3,1))

print(temp[-1])

print(temp[-2:])

print(temp.sum())

print(temp.std())

print(temp.sum(axis=0))