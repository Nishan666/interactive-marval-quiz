import srandom
import marvalCharecters

#here the question is an dictionory with 10 random questions
question = srandom.que10()


#here we traverse through every element in the marvelcharcter list and 
# convert the list items to lower case and make them as variable and assign them to zero(0)
for i in marvalCharecters.character() :
    exec("%s = %d" % (i.lower(),0))


#here the printque function take single question with option as parameter and display the same
def printque(que , ans) :
        print(que)
        count = 0
        for i in ans[que] : 
	    #here the count is used to display rhe option number
            count+=1
            print(count , ". " , i)




#It will loop through every 10 questions
for i in question :
    # print(i , question[i])
    
    #answer will be false when the user give valid input(1,2,3,4)
    answer = True
    
    while answer :
	
	#here we print the question
        printque(i,question)

	#taking user input
        userserChoice = input("Enter Your Choice (1 or 2 or 3 or 4) : ")
        
        #randlist is the list of random numbers,sum of then is 100
        #size is the lenght of the randlist
        randlist , size = srandom.rand()
        
        #assigning var1 to varN (N = size) with randlist values
        for j in range(size):
            exec(f"var{j+1} = randlist[{j}]")

	
	#on random choices we randomly do addition assignment to marvel character variable which was initially 0
        if userserChoice == '1' :
            
            #picking single-random-unique marvel charcter and assign with the random value
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


        elif userserChoice == '2' :

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var2))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var3))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var4))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var5))

            copy = srandom.marval().lower()
            exec("%s += %d" % (copy,var1))

            answer = False



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
            

        else :
            print("worng Input@#$%")

#initialize sum to zero
sum = 0

#sum up the values of marvel cahracters and store it in sum variable
for i in marvalCharecters.character() :
    sum += locals()[i.lower()]


print()

#printing result 
print("YOUR RESULT :")
for i in marvalCharecters.character() :
    #calculating persentage using persentage formula for every single marvel character
    answer = ((locals()[i.lower()] / sum )*100)
    #covert them to upper case and displaying it with result persentage
    print(i.upper()," = ",round(answer),"%")
