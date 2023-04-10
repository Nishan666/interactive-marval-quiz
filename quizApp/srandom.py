import random
import ques
import marvalCharecters


# here the listss contains the marvel charcter name which is used un result
listss = marvalCharecters.character()


# in this function rand , it pices n random number (n depend upon the number of elements in the litss, which is number of marvel charcter)
# and sum of them is not more then 100
def rand() :
    lenght = (len(marvalCharecters.character())+1)
    total = 100 

    numbers = []
    # number list is used to store the n random numbers
    for i in range(lenght-1):
        num = random.randint(0, total)
        numbers.append(num)
        total -= num
    numbers.append(total)
    return(numbers,lenght)

    
# th que10 function is used to pick 10 random question from the bulk of questions,which is return by ques.questions()
def que10() :
    # new10 is the new dictiony to store 10 random question
    new10 = {}
    # quess is the new dictiony to store all the returned questions
    quess= ques.question()
    for i in range(10):
        key, value = random.choice(list(quess.items()))
        # here we delete the used questions from the quess dictionory
        del quess[key]
        new10[key] = value
    return new10


# the function marvel is used to return single random marvel charcter from marvalCharecters.character() list 
#here every time the choice will be unique
def marval() :
    # global is used to use the list outside of the function (make the list global)
    global listss
    #if the list is empty add all the element to the list
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