import random
from googlesearch import search

inp = ""
#Inputs
greet = ("hello", "hi", "greetings", "sup", "what's up","yo")
ques_name = ("what is your name?","who are you?","what are you called?")
exit = ("bye","exit","quit")
ques_type = ["what are you?"]
positive = ["good","yes"]
query = ["Search for"]
#Outputs
greet_resp = ["'Sup bro", "Hey", "*nods*", "How you doing?"]
exit_response = ["See Ya!","Bye"]
no_resp = ("ok","no problem","sure","cool")
posi_resp = ("Awesome!")

while inp.lower() not in exit:
    inp=input("Say:")
    if inp.lower() in greet:
        print("Bot:", random.choice(greet_resp))
    elif inp.lower() in ques_name:
        print("Bot: I am BotMan")
    elif inp.lower() in exit :
        print("Bot:",random.choice(exit_response))
    elif inp.lower() in no_resp or inp.lower() in positive:
        print("Bot:",random.choice(no_resp) or random.choice(posi_resp))
    elif inp.lower() in ques_type:
        print("Bot: I am the dawn of Mankind, BotMan.")
    else:
        print("Bot: I do not understand.")
        for i in search(inp, tld="co.in", num=1, stop=1):
            print(i)
