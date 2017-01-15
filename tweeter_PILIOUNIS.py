
user1 = ''
user2 = ''
result1 = ''
result2 = ''

import tweepy
from tweepy import OAuthHandler
consumer_key = 'HQIfOVGR3h61yEMoz0Y59NNI3'
consumer_secret = '4k46eDlJcjpXxPV6dw4AfSMzY8kTiuxcoDEx4xeadYlxAvfv8P'
access_token = '817813636907409409-TdsmX3zlumVuy9TtIOufWjtZOEDxwxi'
access_secret = 'cH7TtazqEA5nGYbsTCAXY00h933biAprbJN67BcIHrufB'
auth = OAuthHandler(consumer_key,consumer_secret )
auth.set_access_token(access_token, access_secret)
spiros_api = tweepy.API(auth)


print("DOSTE TO SCREEN_NAME TOY 1ου ΧΡΗΣΤΗ TWITTER:")
print("1ος ΧΡΗΣΤΗΣ:")
user1=input()
print()

print("DOSTE TO SCREEN_NAME TOY 2ου ΧΡΗΣΤΗ TWITTER:")
print("2ος ΧΡΗΣΤΗΣ:")
user2=input()
print()
print(" ****** ΠΑΡΑΚΑΛΩ ΠΕΡΙΜΕΝΕΤΕ. ΑΝΑΣΥΡΩ ΔΕΔΟΜΕΝΑ... ******")

i = 1
qtweet =[]
stuff =[]
stuff = spiros_api.user_timeline(screen_name = user1, count = 10, )
for qtweet in stuff:
    result1 += str(i) + ") " + str(qtweet.created_at) + " *** " + qtweet.text + '\n'
    i+=1
    

i = 1
qtweet =[]
stuff = []
stuff = spiros_api.user_timeline(screen_name = user2, count = 10, )
for qtweet in stuff:
    result2 += str(i) + ") " + str(qtweet.created_at) + " *** " + qtweet.text + '\n'    
    i+=1
    

print()
print()
print(user1 + ": ΠΕΡΙΕΧΕΙ " + str(len(result1.split())) + " ΛΕΞΕΙΣ.")
print(result1)    
print()
print()
print(user2 + ": ΠΕΡΙΕΧΕΙ " + str(len(result2.split())) + " ΛΕΞΕΙΣ.")
print(result2) 


print()
print()
if (len(result1.split()) > len(result2.split())):
    print("O XRHSTHS " + user1 + " ΕΧΕΙ ΠΕΡΙΣΣΟΤΕΡΕΣ ΛΕΞΕΙΣ ΣΤΑ 10 ΤΕΛΕΥΤΑΙΑ TWEETs")
elif (len(result2.split()) > len(result1.split())):
     print("O XRHSTHS " + user2 + " ΕΧΕΙ ΠΕΡΙΣΣΟΤΕΡΕΣ ΛΕΞΕΙΣ ΣΤΑ 10 ΤΕΛΕΥΤΑΙΑ TWEETs")
else:
    print("OI XRHSTES " + user1 + ", " + user2 + " ΕΧΟΥΝ ΤΟΝ ΙΔΙΟ ΑΡΙΘΜΟ ΛΕΞΕΩΝ")


    
    



#len(mystring.split())

#import csv
#csvFile = open('tweets.csv', 'a')
#csvWriter = csv.writer(csvFile)

# outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in stuff]
# result = [[qtweet.id_str, qtweet.created_at, qtweet.text] for qtweet in stuff]
# print(result)
