#project2_tweet.py
#
#Name: Jarred Dee
#
#Date: 4/18/18

dictionary = {}                     #create a dictionary
list = open("tweet_decoder.csv")
for i in list:                      #add the abbreviations to a dictionary
    line = i.rstrip("\n")
    str = line.split(",")
    abv = str[0]                    #copy the list of abbreviations into the dictionary
    val = str[1]
    dictionary[abv] = val

while True:
    user_tweet = input("Please input your tweet: \n")  #ask for the user's tweet
    list_tweet = user_tweet.split()                    #make user tweet into a list
    for i in list_tweet:
        for j in dictionary:
            if i.upper() in j:                  #check to see if there is a matching abbreviation
                list_tweet[list_tweet.index(i)] = dictionary[j]     #replace the abbreviation with real definition
            elif j.lower() in i:
                list_tweet[list_tweet.index(i)] = dictionary[j] + list_tweet[list_tweet.index(i)]

    str = ' '.join(list_tweet)                  #creates a string with the new tweet and definitions
    print(str)
    user_again = input("Would you like to input another tweet? (y for yes or n for no)\n")  #ask the user if they want to continue
    if user_again == "n":
        break                   #stop program if user is done
