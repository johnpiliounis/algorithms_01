print("Input LIST's Length: " )
list_length=int(input())

mylist=[]
for t in range(list_length):
    print("Input " + str(t+1) + ") From " + str(list_length) + " List Elements :" )
    a=input()
    mylist.append(a)

print("Initial List :" )
print(mylist)
k=0
newlist = []

for i in range(list_length):
	if not mylist[i]:
		k+=1
	else:
		newlist.append(mylist[i])


for j in range(k):
	 newlist.append("")

print()
print()
print ("Final List :")
print (newlist)

