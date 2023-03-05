# tweeter simple search and compare program

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
user_api = tweepy.API(auth)


print("Input SCREEN_NAME of 1st TWITTER User:")
print("1st User:")
user1=input()
print()

print("Input SCREEN_NAME of 2nd TWITTER User:")
print("2nd User:")
user2=input()
print()
print(" ****** Please wait. Querying data... ******")

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
stuff = user_api.user_timeline(screen_name = user2, count = 10, )
for qtweet in stuff:
    result2 += str(i) + ") " + str(qtweet.created_at) + " *** " + qtweet.text + '\n'    
    i+=1
    

print()
print()
print(user1 + ": Contains " + str(len(result1.split())) + " Words.")
print(result1)    
print()
print()
print(user2 + ": Contains " + str(len(result2.split())) + " Words.")
print(result2) 


print()
print()
if (len(result1.split()) > len(result2.split())):
    print("User " + user1 + " has more words in the last 10 tweets")
elif (len(result2.split()) > len(result1.split())):
     print("User " + user2 + " has more words in the last 10 tweets")
else:
    print("Users " + user1 + ", " + user2 + " have the same number of words")


    
    



#len(mystring.split())

#import csv
#csvFile = open('tweets.csv', 'a')
#csvWriter = csv.writer(csvFile)

# outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in stuff]
# result = [[qtweet.id_str, qtweet.created_at, qtweet.text] for qtweet in stuff]
# print(result)
