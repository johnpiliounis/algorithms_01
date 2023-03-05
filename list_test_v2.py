print("DOSTE TO MHKOS THS LISTAS :" )
list_length=int(input())

mylist=[]
for t in range(list_length):
    print("DOSTE TO " + str(t+1) + ") APO TA " + str(list_length) + " STOIXEIA LISTAS :" )
    a=input()
    mylist.append(a)

print("ARXIKH LISTA :" )
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
print ("TELIKH LISTA :")
print (newlist)

