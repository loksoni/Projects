import random
import difflib as db
inp = ""
#Inputs

inputs = {
"greet" :["hello", "hi", "greetings", "sup", "what's up","yo"],
"ques_name":["what is your name?","who are you?","what are you called?"],
"exit" : ["bye","exit","quit"],
"ques_type" : ["what are you?"],
"positive" : ["good","yes"],
"query" : ["Search for"],
"no_resp" : ["ok","no problem","sure","cool"]}
#Outputs

greet_resp = ["'Sup bro", "Hey", "*nods*", "How you doing?"]
exit_response = ["See Ya!","Bye"]
posi_resp = ("Awesome!")

max = 60.0  #threshold for comparison of input and database
dict_place = None   #index for dictionary
list_place = None   #index for list in dictionary
var = 0
while inp.lower() not in inputs["exit"]:
    max = 60.0
    dict_place = None
    list_place = None
    var = 0
    inp = input("Say:")
    for i in inputs:
        var = 0
        for j in inputs[i]:
            sequence = db.SequenceMatcher(isjunk=None, a=inp, b = inputs[i][var])
            difference = sequence.ratio() * 100     #finds the percentage of their difference
            difference = round(difference, 2)   #brings down to two decimal places
            if difference > max:
                max=difference
                dict_place = i
                list_place = var
            var += 1
    if dict_place == "greet":
        print("Bot:", random.choice(greet_resp))
    elif dict_place == "ques_name":
        print("Bot: I am BotMan")
    elif dict_place == "exit":
        print("Bot:", random.choice(exit_response))
    elif dict_place == "no_resp" or dict_place == "positive":
        print("Bot:", random.choice(inputs["no_resp"]) or random.choice(posi_resp))
    elif dict_place == "ques_type":
        print("Bot: I am the dawn of Mankind, BotMan.")
    else:
        print("Bot: I do not understand.")
