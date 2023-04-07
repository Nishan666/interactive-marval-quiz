# lis = ['nick','jim','kim','wix']


# for i in range(len(lis)) :
#     exec(f"var{i+1} = lis[{i}]")


# print(var1)
# print(var2)




sum = 1

thor = 55

a= 'thor'

# exec("%d += %d" % (sum,thor))

# m = exec("%s" % (a))

sum += locals()[a]


print(sum)