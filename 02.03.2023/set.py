text={'gowtham','mano','kavin','ananth','dinesh','Mano'}
print(text)
print(len(text))
print(type(text))

num={True,1,2,0,False}
print(num)
num.add(3)
print(num)
nums=set((1,2,3,4,5,6))
num1={1,2,3,4}
print(nums)
y=num.issubset(num1)
print(y)
lists=[7,8,9]
nums.update(lists)
print(nums)
num.update(nums)
print(num)
num.symmetric_difference(nums)
print(num)
#del num
print(num)
number1={1,2,3,4,5}
number2={6,7,8,9,10,1}
number3=number2.copy()
print(number3)
print(number1)
print(number2)
number1.update(number2)
print(number1)
number1.remove(7)
print(number1)
number1.discard(8)
print(number1)
number1.pop()
print(number1)
number3.difference(number1)
print(number3)
number1.intersection_update(number3)
print(number1)

num={41}
print(type(num))