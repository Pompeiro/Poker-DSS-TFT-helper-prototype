# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:33:23 2020

@author: Janusz
"""



import tkinter as tk
import random
from functools import partial

J=11
Q=12
K=13
A=14


CARDDICT = {"9":"9", "10":"10", "J":"J", "Q":"Q", "K":"K", "A":"A"}




LISTAKART = [9, 10, J, Q, K, A]




######################## FULL DECK
FULLDECK = [CARDDICT["9"], CARDDICT["10"], CARDDICT["J"], CARDDICT["Q"], CARDDICT["K"], CARDDICT["A"]]

####### CHECK CARDS ON TABLE AND EVALUATE CARDS LEFT IN DECK

cardsLeft = FULLDECK

cardsToRemove = []

cardsLeftString = []

def check_left_cards_in_deck():
    for i in range(0,len(box_counter),1):
        if box_counter[i].get() == 1:
#            print(cardsLeft[i])
            cardsToRemove.append(cardsLeft[i])
#            print(cardsLeft)
    if len(cardsToRemove) > 0:
        print("Fulldeck: ", cardsLeft)
        print("Cards to remove from fulldeck: ", cardsToRemove)
        for card in cardsToRemove:
            cardsLeft.remove(card)
    print("Cards left in deck: ", cardsLeft)
    return






# def cards_left_to_string():
#     cardsLeftString = list(map(str, cardsLeft))
#     print("Cards left as list of strings: ",cardsLeftString)
#     return cardsLeftString


def show_cards_left_buttons():
    for i in range(0,len(cardsLeft),1):
        buttonCal = tk.Button(MainWindow, text=cardsLeft[i], command=lambda:add(counterA)).grid(row=13, column=i)
    return









#############3 POINTS
SINGLE9 = 10
SINGLE10 = 20
SINGLEJ = 30
SINGLEQ = 40
SINGLEK = 50
SINGLEA = 60


############## PAIR POINTS

PAIRsingleMULTIPLIER = 20

PAIR9 = SINGLE9 * PAIRsingleMULTIPLIER
PAIR10 = SINGLE10 * PAIRsingleMULTIPLIER
PAIRJ = SINGLEJ * PAIRsingleMULTIPLIER
PAIRQ = SINGLEQ * PAIRsingleMULTIPLIER
PAIRK = SINGLEK * PAIRsingleMULTIPLIER
PAIRA = SINGLEA * PAIRsingleMULTIPLIER


######### Double pair points

DOUBLEPAIRsingleMULTIPLIER = 40

DOUBLEPAIR9 = SINGLE9 * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIR10 = SINGLE10 * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIRJ = SINGLEJ * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIRQ = SINGLEQ * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIRK = SINGLEK * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIRA = SINGLEA * DOUBLEPAIRsingleMULTIPLIER




def calculate_single_points(label_result):
    suma = (counter9.get() * SINGLE9 
    + counter10.get() * SINGLE10 
    + counterJ.get() * SINGLEJ
    + counterQ.get() * SINGLEQ
    + counterK.get() * SINGLEK
    + counterA.get() * SINGLEA)
    
    print(suma)
    label_result.config(text="Result from single points %d" %suma)
    return


def calculate_pair_points(label_result):
    pairsum = 0
    if counter9.get() == 2:
        pairsum = pairsum + PAIR9
    if counter10.get() == 2:
        pairsum = pairsum + PAIR10
    if counterJ.get() == 2:
        pairsum = pairsum + PAIRJ
    if counterQ.get() == 2:
        pairsum = pairsum + PAIRQ
    if counterK.get() == 2:
        pairsum = pairsum + PAIRK
    if counterA.get() == 2:
        pairsum = pairsum + PAIRA
        
        
    print(pairsum)
    label_result.config(text="Result from pair points %d" %pairsum)
    return




def calculate_double_pair_points(label_result):
    doublepairsum = 0
    if counter9.get() == 4:
        doublepairsum = doublepairsum + DOUBLEPAIR9
    if counter10.get() == 4:
        doublepairsum = doublepairsum + DOUBLEPAIR10
    if counterJ.get() == 4:
        doublepairsum = doublepairsum + DOUBLEPAIRJ
    if counterQ.get() == 4:
        doublepairsum = doublepairsum + DOUBLEPAIRQ
    if counterK.get() == 4:
        doublepairsum = doublepairsum + DOUBLEPAIRK
    if counterA.get() == 4:
        doublepairsum = doublepairsum + DOUBLEPAIRA
        
        
    print(doublepairsum)
    label_result.config(text="Result from doublepair points %d" %doublepairsum)
    return


def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result is %d" % result)
    print(label_result,n1,n2)
    return




def substract_one(label_result, n1):
    num1 = (n1.get())
    result = int(num1)-1
    label_result.config(text="Result is %d" % result)
    return


def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    #print(equation.get())
    #equa = ""
 
    
def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)
    EqualPress() 
    
    
def check_value(label_result, stringVariable):
    value = stringVariable.get()
    value = int(value)
    label_result.config(text="Value = %d" % value)
    return


def add(intVariable):
    intVariable.set(intVariable.get() + 1)
    
    
def sub(intVariable):
    if intVariable.get() >0:
        intVariable.set(intVariable.get() - 1)
    
    

MainWindow = tk.Tk()
MainWindow.geometry('600x400+100+200')
MainWindow.title('Advanced DSS card game calculator')
number1 = tk.StringVar()


equa = ""
equation = tk.StringVar()
x=tk.IntVar()


############### AKTUALNA LICZBA KART
counter9=tk.IntVar()
counter10=tk.IntVar()
counterJ=tk.IntVar()
counterQ=tk.IntVar()
counterK=tk.IntVar()
counterA=tk.IntVar()

box_counter = [counter9, counter10, counterJ, counterQ, counterK, counterA]


## tekst na ekranie oznaczenia kart

labelTitle = tk.Label(MainWindow, text="Hearts").grid(row=0, column=2)


labelNum9 = tk.Label(MainWindow, text="9").grid(row=1, column=0)
nineEntry = tk.Entry(MainWindow)



labelNum10 = tk.Label(MainWindow, text="10").grid(row=2, column=0)
tebEntry = tk.Entry(MainWindow)

labelNumJ = tk.Label(MainWindow, text="J").grid(row=3, column=0)
jackEntry = tk.Entry(MainWindow)

labelNumQ = tk.Label(MainWindow, text="Q").grid(row=4, column=0)
quuenEntry = tk.Entry(MainWindow)

labelNumK = tk.Label(MainWindow, text="K").grid(row=5, column=0)
kingEntry = tk.Entry(MainWindow)

labelNumA = tk.Label(MainWindow, text="A").grid(row=6, column=0)
aceEntry = tk.Entry(MainWindow)


##############################










##### wynik pod buttonami

singleResultLabel = tk.Label(MainWindow)
singleResultLabel.grid(row=7, column=2)

pairResultLabel = tk.Label(MainWindow)
pairResultLabel.grid(row=8, column=2)


doublepairResultLabel = tk.Label(MainWindow)
doublepairResultLabel.grid(row=9, column=2)


#######
label = tk.Label(MainWindow, textvariable=x)
label.grid(row=8, column=0)



## pasek do wpisywania zmiennych

entryNum9 = tk.Entry(MainWindow, textvariable=counter9).grid(row=1, column=2)
entryNum10 = tk.Entry(MainWindow, textvariable=counter10).grid(row=2, column=2)
entryNumJ = tk.Entry(MainWindow, textvariable=counterJ).grid(row=3, column=2)
entryNumQ = tk.Entry(MainWindow, textvariable=counterQ).grid(row=4, column=2)
entryNumK = tk.Entry(MainWindow, textvariable=counterK).grid(row=5, column=2)
entryNumA = tk.Entry(MainWindow, textvariable=counterA).grid(row=6, column=2)


##




### funkcje liczone przez partial

call_result = partial(call_result, singleResultLabel, number1)
substract_one = partial(substract_one, singleResultLabel, equation)

check_value = partial(check_value, singleResultLabel, number1)
calculate_single_points = partial(calculate_single_points, singleResultLabel)

calculate_pair_points = partial(calculate_pair_points, pairResultLabel)

calculate_double_pair_points = partial(calculate_double_pair_points, doublepairResultLabel)


# for karta in LISTAKART:
#     add[karta]=partial(add,karta)
#     print(karta)
# add=partial(add,x)
##### PRZYCISKI do zmiany wartosci

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counter9)).grid(row=1, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counter9)).grid(row=1, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counter10)).grid(row=2, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counter10)).grid(row=2, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterJ)).grid(row=3, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterJ)).grid(row=3, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterQ)).grid(row=4, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterQ)).grid(row=4, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterK)).grid(row=5, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterK)).grid(row=5, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterA)).grid(row=6, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterA)).grid(row=6, column=4)

buttonCal = tk.Button(MainWindow, text="single", command=calculate_single_points).grid(row=9, column=5)

buttonCal = tk.Button(MainWindow, text="pair", command=calculate_pair_points).grid(row=9, column=7)


buttonCal = tk.Button(MainWindow, text="doublepair", command=calculate_double_pair_points).grid(row=9, column=8)


buttonCal = tk.Button(MainWindow, text="checkcard", command=check_left_cards_in_deck).grid(row=11, column=8)

buttonCal = tk.Button(MainWindow, text="Show left cards", command=show_cards_left_buttons).grid(row=11, column=9)


#######



MainWindow.mainloop()


# from tkinter import *
 
# root = Tk()
# root.title("Calculator")
# # So that it becomes of fixed size
# root.resizable(0, 0)
# # So that it remains on top of the screen
# root.wm_attributes("-topmost", 1)
 
# # Label
# Label1 = Label(root, text = "Calculator app")
# Label1.grid(row=0, columnspan=8)
 
# # Variables
# equa = ""
# equation = StringVar()
 
# calculation = Label(root, textvariable = equation)
 
# equation.set("Enter your expression : ")
 
# calculation.grid(row=2, columnspan=8)
 

 
# def EqualPress():
#     global equa
#     total = str(eval(equa))
#     equation.set(total)
#     #equa = ""
 
    
# def btnPress(num):
#     global equa
#     equa = equa + str(num)
#     equation.set(equa)
#     EqualPress()    
    
    
    
# def ClearPress():
#     global equa
#     equa = ""
#     equation.set("")
 
# Button0 = Button(root, text="0", command = lambda:btnPress(0), borderwidth=1, relief=SOLID)
# Button0.grid(row = 6, column = 2, padx=10, pady=10)
# Button1 = Button(root, text="1", command = lambda:btnPress(1), borderwidth=1, relief=SOLID)
# Button1.grid(row = 3, column = 1, padx=10, pady=10)
# Button2 = Button(root, text="2", command = lambda:btnPress(2), borderwidth=1, relief=SOLID)
# Button2.grid(row = 3, column = 2, padx=10, pady=10)


# Plus = Button(root, text="+", command = lambda:btnPress("+1"), borderwidth=1, relief=SOLID)
# Plus.grid(row = 3, column = 4, padx=10, pady=10)


# Minus = Button(root, text="-", command = lambda:btnPress("-"), borderwidth=1, relief=SOLID)
# Minus.grid(row = 4, column = 4, padx=10, pady=10)


# Equal = Button(root, text="=", command = EqualPress, borderwidth=1, relief=SOLID)
# Equal.grid(row=6, column=3, padx=10, pady=10)


# Clear = Button(root, text="C", command = ClearPress, borderwidth=1, relief=SOLID)
# Clear.grid(row = 6, column = 1, padx=10, pady=10)
 
# root.mainloop()
