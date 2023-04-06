import random
import ques
import marvalCharecters

listss = marvalCharecters.character()

def rand() :
    lenght = (len(marvalCharecters.character())+1)
    total = 100 

    numbers = []
    for i in range(lenght-1):
        num = random.randint(0, total)
        numbers.append(num)
        total -= num
    numbers.append(total)
    return(numbers,lenght)

    

def que10() :
    new10 = {}
    quess= ques.question()
    for i in range(10):
        key, value = random.choice(list(quess.items()))
        del quess[key]
        new10[key] = value
    return new10


def marval() :
    global listss
    if listss == [] :
        listss = marvalCharecters.character()
    # print(listss)
    singleChoice = random.choice(listss)
    del listss[listss.index(singleChoice)]
    return singleChoice






# def split_num():
#     result = []
#     while len(result) != 4 :
#         n = 100
#         parts = random.randint(1,n)
#         for i in range(parts-1):
#             x = random.randint(1,n-parts+i+1)
#             n = n - x
#             result.append(x)
#         result.append(n)
#         print(result)

#     print()
#     print(result)
#     # print(sum(result))

# import random
# split_num()