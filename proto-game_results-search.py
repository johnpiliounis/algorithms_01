# BIBLIO8HKH GIA ACCESS URL & WEB SERVICES
import urllib.request

mylist = []
e=0

print("DOSTE DIADOXIKA 7 NOUMERA APO 0 - 9")
for j in range(7):
    print(str(j+1) + "o NOUMERO:")
    number=input()
    mylist.append(str(number))


print(mylist)


for k in range(4):
    print()
    thedate = ""
    print("DOSTE THN " + str(k+1) + "η ΑΠΟ ΤΙΣ 8 HMEROMHNIES KLHROSHS PROTO, STH MORFH dd-MM-yyyy :")
    thedate=input()
    l=[]
    ml=[]
    # XRHSIMOPOIHSAME THN find() PANO STHN test STIS DOKIMES GIA NA BROUME pos1 & pos2 APO TO xml SERVICE
    # ME BASH TA <result> & </result> MESA STH LINE, POY EINAI TYPOY 'b' (BYTE) ALL POY THN KANAME STRING (test) 
    # ME THN line.decode("utf-8")
    pos1=217  
    pos2=218
    data = urllib.request.urlopen("http://applications.opap.gr/DrawsRestServices/proto/drawDate/" + thedate + ".xml")
    for line in data.readlines():
            l.append(line)
  

    test = line.decode("utf-8")

    # ANA8ETOYME SE LIST TA 7 NOYMERA KA8E KLHROSHS
    for i in range(7):
            s=test[pos1:pos2]
            ml.append(s)
            pos1+=18
            pos2+=18

    print("O 7-ΨΗΦΙΟΣ ΑΡΙΘΜΟΣ ΤΗΣ ΚΛΗΡΩΣΗΣ :")
    print(ml)
    print("O 7-ΨΗΦΙΟΣ ΑΡΙΘΜΟΣ ΜΟΥ :")
    print(mylist)

    t1=0
    k=1
    z=0
    while (k==1 and z < 7):
        if (ml[z] == mylist[z]):
            t1+=1
        else:
            k=0

        z+=1

    
    t2=0
    k=1
    z=6
    while (k==1 and z > 0):
        if (ml[z] == mylist[z]):
            t2+=1
        else:
            k=0

        z-=1

    if ( t1 >= 2 or t2 >=2):
        if (t1 > t2):
            print("EPITYXIA KATHGORIAS: " + str(8-t1) + "ης, ΕΛΕΓΧΟΥ ΑΠΟ ΑΡΙΣΤΕΡΑ")
        elif ( t2 > t1 ):
            print("EPITYXIA KATHGORIAS: " + str(8-t2) + "ης, ΕΛΕΓΧΟΥ ΑΠΟ ΔΕΞΙΑ")
        else:
            print("EPITYXIA KATHGORIAS: " + str(8-t1) + "ης")

        e+=1
        


print("ΟΙ ΠΕΡΙΣΟΤΕΡΕΣ ΕΠΙΤΥΧΙΕΣ ΠΟΥ ΕΙΧΕ Η ΣΕΙΡΑ ΠΡΟΤΟ ΠΟΥ ΔΩΣΑΤΕ ΜΕΣΩ ΤΗΣ ΛΙΣΤΑΣ, ΕΙΝΑΙ " + str(e))
        
    
