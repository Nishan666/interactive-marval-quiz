import srandom
import marvalCharecters

question = srandom.que10()
# a,b,c,d = srandom.rand()

for i in marvalCharecters.character() :
    exec("%s = %d" % (i.lower(),0))



def printque(que , ans) :
        print(que)
        count = 0
        for i in ans[que] : 
            count+=1
            print(count , ". " , i)





for i in question :
    # print(i , question[i])
    answer = True
    while answer :

        printque(i,question)

        userserChoice = input("Enter Your Choice (1 or 2 or 3 or 4) : ")
        # a,b,c,d = srandom.rand()
        randlist , size = srandom.rand()
        for j in range(size):
            exec(f"var{j+1} = randlist[{j}]")
        # #######
        # print(a)
        # print(b)
        # print(c)
        # print(d)
        # #######
        if userserChoice == '1' :
            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var1))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var2))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var3))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var4))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var5))

            answer = False

            # print(thor)
            # print(groot)
            # print(hulk)
            # print(ironman)
            # print(spiderman)

        elif userserChoice == '2' :

            copy = srandom.marval().lower()
            # print(copy)
            exec("%s += %d" % (copy,var2))

            copy = srandom.marval().lower()
            # print(copy)
            exec("%s += %d" % (copy,var3))

            copy = srandom.marval().lower()
            # print(copy)
            exec("%s += %d" % (copy,var4))

            copy = srandom.marval().lower()
            # print(copy)
            exec("%s += %d" % (copy,var5))

            copy = srandom.marval().lower()
            # print(copy)
            exec("%s += %d" % (copy,var1))

            answer = False

            # print(thor)
            # print(groot)
            # print(hulk)
            # print(ironman)
            # print(spiderman)

        elif userserChoice == '3' :
            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var3))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var4))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var5))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var1))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var2))

            answer = False

            # print(thor)
            # print(groot)
            # print(hulk)
            # print(ironman)
            # print(spiderman)

        elif userserChoice == '4' :
            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var4))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var5))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var1))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var2))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var3))

            answer = False
            

            # print(thor)
            # print(groot)
            # print(hulk)
            # print(ironman)
            # print(spiderman)

        else :
            print("worng Input@#$%")


sums = 0
for i in marvalCharecters.character() :
    print(exec("%d"%(i.lower())))
    # exec("%s += %f" % (sums,i.lower()))






# marvalCharecters.result(sum)
            
                
