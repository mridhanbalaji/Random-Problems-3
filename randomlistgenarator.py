import random
def createList(x):
    i = 0
    lists = []
    while i < x:
        y = random.randint(1,10000)
        lists.append(y)
        i += 1
    lists.sort()
    print(lists, end="") 

createList(100)