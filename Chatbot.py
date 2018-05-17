import random
import difflib as db
import os
from functools import reduce
inp = ""
#Inputs

inputs = {
"greet" :["hello", "hi", "greetings", "sup", "what's up","yo"],
"ques_name":["what is your name?","who are you?","what are you called?"],
"exit" : ["bye","exit","quit","See Ya!"],
"ques_type" : ["what are you?"],
"positive" : ["good","yes"],
"query" : ["Search for"],
"no_resp" : ["ok","no problem","sure","cool","thanks"],
"calc_add" : ["Add 1 and 2"],
"calc_sub" : ["subtract 1 and 2","subtract 1 from 2"],
"calc_mul" : ["multiply 1 and 2","multiply 1 by 2"],
"calc_div" : ["divide 1 and 2","divide 1 from 2"]}
#Outputs

greet_resp = ["'Sup bro", "Hey", "*nods*", "How you doing?"]
exit_response = ["See Ya!","Bye"]
posi_resp = ("Awesome!")
#Body starts
def mul(var):
    mul = 1
    for i in range(0,len(var)):
        mul *= var[i]
    return mul

def sub(var):
    return var[0]-var[1]

def div(var):
    return var[0]/var[1]

while inp.lower() not in inputs["exit"]:
    max = 45.0              #threshold for comparison of input and database
    dict_place = None       #index for dictionary
    list_place = None       #index for list in dictionary
    var = 0
    integers = []
    calc = []
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
        exit()
    elif dict_place == "no_resp" or dict_place == "positive":
        print("Bot:", random.choice(inputs["no_resp"]) or random.choice(posi_resp))
    elif dict_place == "ques_type":
        print("Bot: I am the dawn of Mankind, BotMan.")
    elif dict_place == "calc_add":
        calc = inp.split(' ')
        for i in range(0,len(calc)):
            try:
                integers.append(int(calc[i]))
            except:
                pass
        print("Bot:",sum(integers))

    elif dict_place == "calc_sub":
        calc = inp.split(' ')
        for i in range(0, len(calc)):
            try:
                integers.append(int(calc[i]))
            except:

                pass
        print("Bot:", sub(integers))

    elif dict_place == "calc_mul":
        calc = inp.split(' ')
        for i in range(0, len(calc)):
            try:
                integers.append(int(calc[i]))
            except:

                pass
        print("Bot:", mul(integers))
    elif dict_place == "calc_div":
        calc = inp.split(' ')
        for i in range(0, len(calc)):
            try:
                integers.append(int(calc[i]))
            except:
                pass
        print("Bot:", div(integers))
    else:
        print("Bot: I do not understand.")
