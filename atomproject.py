mylist = [1,2,3]
for num in range (0,11,2):
    print(num)
list (range(0,11,2))

index_count = 0
for letter in 'abcde':
    print('at index {} the letter is {}'.format(index_count,letter))
    index_count += 1
word = 'abcde'
for item in enumerate(word):
    print(item)

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
mylist4 = [{'k1':24, 'k2':32, 'k3':26}]
for item in zip (mylist1, mylist2, mylist3, mylist4):
    print(item)

    2 in [1,2,3]
    'a' in 'a world'
    'my key' in {'my key':345}


mylist = [10,20,30,40,50]
min (mylist)
max (mylist)

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)
