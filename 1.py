# convert string into list of list with first line as first element in all sublist, sublist len is 3
# 	ex:    input:        in string
# 				first line 
# 				second line 
# 				third line
# 				fourth line
# 				fifth line
				
# 			output:
# 			    [["first line", "second line", "third line"], ["first line", "fourth line", "fifth line"]]


str ="""first line
second line
third line
fourth line
fifth line"""


l= list(str.split("\n"))

ans=[]
i=1
while(i<=len(l)-1):
	a=[]
	a.append(l[0])
	a.append(l[i])
	i+=1
	# if i>=int(len(l)):
	# 	a.append(ans)
	# 	break
	a.append(l[i])
	ans.append(a)
	i+=1
print(ans)



