# add 2 lists using map and lambda:

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)

# map object will show a map object, to show you have to pass the result in a data struture method:
print(numbers1)
print(numbers2)
print("Addition of both lists:", "\n",list(result))

numbers3 = [1, 8, 3]

def sq(n):
    return n * n 

v = list(map(sq, numbers3))   

print(numbers3)
print(v)



# zip it!:
# zip elements of two lists:

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3)

# zip elements of two lists:

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2 [::-1]):
    print(x, y)

# zip into dictonary:

stocks = ['reliance', 'infosys', 'TCS']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, 
                         prices in zip(stocks, prices)}

print('\n{}'.format(new_dict))


# Activity 3: Exit method:

for i in range(10):
    if i == 5:
        print("exit")
        exit()
    print(i, end= " ")