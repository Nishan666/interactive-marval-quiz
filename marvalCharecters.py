def character() :
    lists = ['Thor','Spiderman','Ironman','Hulk','Groot']
    return lists





def result(sum) :
    for i in character() :
        answer = exec("(%s / %d) * %d" % (i,sum,100))
        print(i.upper()," = ",round(answer),"%")
