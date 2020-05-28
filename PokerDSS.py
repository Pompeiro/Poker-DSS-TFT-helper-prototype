# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:19:42 2020

@author: Janusz
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:33:23 2020

@author: Janusz
"""



import tkinter as tk
import random
from functools import partial


import collections
from enum import IntEnum
import operator




SHIFTBETWEENCARDS = 8
SHIFTADJUSTMENT = 1
PADXBETWEENCARDNAMES = 20


RANDOMLYPICKEDCARDCOUNTER = 0



############ CREATING FULL DECK

FROMCARDOFFSET = 9
NUMBEROFCARDSINFULLDECK = 24
FULLDECK =[0] * NUMBEROFCARDSINFULLDECK
CARDSCOUNTER = 0 ########## TO CREATE FULLDECK AS LIST



############ CARDS AS VALUES

J=11
Q=12
K=13
A=14




############# CARDS AS NAMEDTUPLE WITH Cardname.rank and Cardname.suit



Suits = IntEnum("Suits", "spades hearts clubs diamonds")
Ranks = IntEnum("Ranks", "x two three four five six seven eight nine ten jack queen king ace")

Card = collections.namedtuple("Card", "rank suit")






for i in  range(1,len(Suits)+1,1): ### + 1 BECAUSE IntEnum starts from 1 not 0
    for j in range(FROMCARDOFFSET, A+1,1): ### from offset card to Ace
        # print(j,Suits(i))
        # print(Card(Ranks(j),Suits(i)))
        FULLDECK[CARDSCOUNTER] = Card(Ranks(j),Suits(i))
        CARDSCOUNTER=CARDSCOUNTER+1









































############### PREPARING CARDS IN DECK CARDS TO REMOVE ETC

#### HEARTS $$$$$$$$$ THEN TILES ^^^^^^^^^^^^ THEN CLOVERS &&&&&&&&& THEN PINKES ***********

#### MEABY I WILL CHANGE VALUES IN THE FUTURE


CARDDICTH = {"H9":"H9", "H10":"H10", "HJ":"HJ", "HQ":"HQ", "HK":"HK", "HA":"HA"}

CARDDICTT = {"T9":"T9", "T10":"T10", "TJ":"TJ", "TQ":"TQ", "TK":"TK", "TA":"TA"}


CARDDICTC = {"C9":"C9", "C10":"C10", "CJ":"CJ", "CQ":"CQ", "CK":"CK", "CA":"CA"}


CARDDICTP = {"P9":"P9", "P10":"P10", "PJ":"PJ", "PQ":"PQ", "PK":"PK", "PA":"PA"}


LISTAKART = [9, 10, J, Q, K, A]




######################## FULL DECK
FULLDECKSTRING = [CARDDICTH["H9"], CARDDICTH["H10"], CARDDICTH["HJ"], CARDDICTH["HQ"], CARDDICTH["HK"], CARDDICTH["HA"],
            CARDDICTT["T9"], CARDDICTT["T10"], CARDDICTT["TJ"], CARDDICTT["TQ"], CARDDICTT["TK"], CARDDICTT["TA"],
            CARDDICTC["C9"], CARDDICTC["C10"], CARDDICTC["CJ"], CARDDICTC["CQ"], CARDDICTC["CK"], CARDDICTC["CA"],
            CARDDICTP["P9"], CARDDICTP["P10"], CARDDICTP["PJ"], CARDDICTP["PQ"], CARDDICTP["PK"], CARDDICTP["PA"]]





MainWindow = tk.Tk()
MainWindow.geometry('1200x800')
MainWindow.title('Advanced DSS card game calculator')
number1 = tk.StringVar()


equa = ""
equation = tk.StringVar()
x=tk.IntVar()


############### LICZNIKI AKTUALNA LICZBA KART HEARTS $$$$$$$$$$$$$$$$$$
counterH9=tk.IntVar()
counterH10=tk.IntVar()
counterHJ=tk.IntVar()
counterHQ=tk.IntVar()
counterHK=tk.IntVar()
counterHA=tk.IntVar()




############### LICZNIKI AKTUALNA LICZBA KART TILES $$$$$$$$$$$$$$$$$$
counterT9=tk.IntVar()
counterT10=tk.IntVar()
counterTJ=tk.IntVar()
counterTQ=tk.IntVar()
counterTK=tk.IntVar()
counterTA=tk.IntVar()



############### LICZNIKI AKTUALNA LICZBA KART CLOVERS &&&&&&&&&&&&&&&&&&&&&
counterC9=tk.IntVar()
counterC10=tk.IntVar()
counterCJ=tk.IntVar()
counterCQ=tk.IntVar()
counterCK=tk.IntVar()
counterCA=tk.IntVar()




############### LICZNIKI AKTUALNA LICZBA KART PIKES *********************8
counterP9=tk.IntVar()
counterP10=tk.IntVar()
counterPJ=tk.IntVar()
counterPQ=tk.IntVar()
counterPK=tk.IntVar()
counterPA=tk.IntVar()









lookup = {CARDDICTH["H9"]: counterH9, CARDDICTH["H10"]: counterH10, CARDDICTH["HJ"]: counterHJ,
          CARDDICTH["HQ"]: counterHQ, CARDDICTH["HK"]: counterHK, CARDDICTH["HA"]: counterHA,
          
          CARDDICTT["T9"]: counterT9, CARDDICTT["T10"]: counterT10, CARDDICTT["TJ"]: counterTJ,
          CARDDICTT["TQ"]: counterTQ, CARDDICTT["TK"]: counterTK, CARDDICTT["TA"]: counterTA,
          
          CARDDICTC["C9"]: counterC9, CARDDICTC["C10"]: counterC10, CARDDICTC["CJ"]: counterCJ,
          CARDDICTC["CQ"]: counterCQ, CARDDICTC["CK"]: counterCK, CARDDICTC["CA"]: counterCA,
          
          CARDDICTP["P9"]: counterP9, CARDDICTP["P10"]: counterP10, CARDDICTP["PJ"]: counterPJ,
          CARDDICTP["PQ"]: counterPQ, CARDDICTP["PK"]: counterPK, CARDDICTP["PA"]: counterPA,}





def select_counter(cardleft): ### like cardleft convert to counter
    # print("Card left input to select counter is:", cardleft)
    obj = lookup.get(cardleft)
    if obj:
        # print("Output is:", obj)
        return obj
    







hand = []

def update_hand():
    for i in range(0,len(FULLDECK),1):
        if lookup[FULLDECKSTRING[i]].get() == 1:
            hand.append(FULLDECK[i])
    print(hand)
    return

def is_pair(hand):
    ranks = collections.Counter(map(operator.attrgetter("rank"), hand))
    return ranks.most_common(1)[0][1] == 2


def is_two_pair(hand):
    ranks = collections.Counter(map(operator.attrgetter("rank"), hand))
    pairs = ranks.most_common(2)
    return pairs[0][1] == 2 and pairs[1][1] == 2


def is_three_of_kind(hand):
    ranks = collections.Counter(map(operator.attrgetter("rank"), hand))
    return ranks.most_common(1)[0][1] == 3


def is_straight(hand):
    hand.sort(key=operator.attrgetter("rank"))
    start = hand[0].rank
    straight = [Card(r, None) for r in range(start, start+6)]
    print(straight)
    return all(got.rank == want.rank for got,want in zip(hand, straight))


def is_flush(hand):
    the_suit = hand[0].suit
    return all(c.suit == the_suit for c in hand)


def is_full_house(hand):
    ranks = collections.Counter(map(operator.attrgetter("rank"), hand))
    triplet, pair = ranks.most_common(2)
    return triplet[1] == 3 and pair[1] == 2

def is_four_of_kind(hand):
    ranks = collections.Counter(map(operator.attrgetter("rank"), hand))
    return ranks.most_common(1)[0][1] == 4


def is_straightflush(hand):
    return is_straight(hand) and is_flush(hand)

def is_royalflush(hand):
    s = hand[0].suit
    royal = [Card(Ranks(r), s) for r in range(10, A+1)]
    return royal == sorted(hand, key=operator.attrgetter("rank"))












####### CHECK CARDS ON TABLE AND EVALUATE CARDS LEFT IN DECK

cardsLeft = FULLDECK

cardsToRemove = []

cardsLeftString = []

def check_left_cards_in_deck(cardsLeft):
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


def show_cards_left_buttons(cardsLeft):
    for i in range(0,len(cardsLeft),1):
        select_counter(cardsLeft[i])
        buttonCal = tk.Button(MainWindow, text=cardsLeft[i], command=lambda i = i:add(select_counter(cardsLeft[i]))).grid(row=13, column=i)
    return


def pick_random_card_from_left_cards(cardsLeft):
    global RANDOMLYPICKEDCARDCOUNTER
    RANDOMLYPICKEDCARDCOUNTER =  RANDOMLYPICKEDCARDCOUNTER + 1
    Random_card_from_left_cards = cardsLeft[random.randint(0, (len(cardsLeft)-1))]
    buttonCal = tk.Button(MainWindow, text=Random_card_from_left_cards, command=lambda:add(select_counter(Random_card_from_left_cards))).grid(row=15, column=RANDOMLYPICKEDCARDCOUNTER)
    return






#############3 POINTS
SINGLE9 = 10
SINGLE10 = 20
SINGLEJ = 30
SINGLEQ = 40
SINGLEK = 50
SINGLEA = 60

SINGLE_MULTIPLIER_LIST = [SINGLE9, SINGLE10, SINGLEJ, SINGLEQ, SINGLEK, SINGLEA]


############## PAIR POINTS

PAIRsingleMULTIPLIER = 20

PAIR9 = SINGLE9 * PAIRsingleMULTIPLIER
PAIR10 = SINGLE10 * PAIRsingleMULTIPLIER
PAIRJ = SINGLEJ * PAIRsingleMULTIPLIER
PAIRQ = SINGLEQ * PAIRsingleMULTIPLIER
PAIRK = SINGLEK * PAIRsingleMULTIPLIER
PAIRA = SINGLEA * PAIRsingleMULTIPLIER


PAIR_MULTIPLIER_LIST = [PAIR9, PAIR10, PAIRJ, PAIRQ, PAIRK, PAIRA]


######### Double pair points

DOUBLEPAIRsingleMULTIPLIER = 20

DOUBLEPAIR9 = SINGLE9 * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIR10 = SINGLE10 * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIRJ = SINGLEJ * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIRQ = SINGLEQ * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIRK = SINGLEK * DOUBLEPAIRsingleMULTIPLIER
DOUBLEPAIRA = SINGLEA * DOUBLEPAIRsingleMULTIPLIER

DOUBLEPAIR_MULTIPLIER_LIST = [DOUBLEPAIR9, DOUBLEPAIR10, DOUBLEPAIRJ, DOUBLEPAIRQ, DOUBLEPAIRK, DOUBLEPAIRA]




######### Trio cards points

TRIOsingleMULTIPLIER = 50*3 ########## *3 because best score for AA + KK is 4400
                            ########## and 999 is now 4500

TRIO9 = SINGLE9 * TRIOsingleMULTIPLIER
TRIO10 = SINGLE10 * TRIOsingleMULTIPLIER
TRIOJ = SINGLEJ * TRIOsingleMULTIPLIER
TRIOQ = SINGLEQ * TRIOsingleMULTIPLIER
TRIOK = SINGLEK * TRIOsingleMULTIPLIER
TRIOA = SINGLEA * TRIOsingleMULTIPLIER

TRIO_MULTIPLIER_LIST = [TRIO9, TRIO10, TRIOJ, TRIOQ, TRIOK, TRIOA]











###################### POINTS MEASURE

def calculate_single_points(label_result,hand):
    suma = 0
    for i in range(0,len(hand),1):
        suma = suma + int(hand[i][0])
    print("Single points: ",suma)
    label_result.config(text="Result from single points %d" %suma)
    return


def calculate_pair_points(label_result):
    pairsum = 0
    for i in range(0,len(box_counter),1):
        if box_counter[i].get() == 2:
            pairsum = pairsum + box_counter[i].get() * PAIR_MULTIPLIER_LIST[i%6] 
    print(pairsum)
    label_result.config(text="Result from pair points %d" %pairsum)
    return



def calculate_double_pair_points(label_result):
    doublepairsum = 0
    SINGLEORDOUBLE = 0
    for i in range(0,len(box_counter),1):
        if box_counter[i].get() == 2:
            doublepairsum = doublepairsum + box_counter[i].get() * DOUBLEPAIR_MULTIPLIER_LIST[i%6] 
            SINGLEORDOUBLE = SINGLEORDOUBLE + 1
    if SINGLEORDOUBLE < 2: ############ if 0 or 1 pair then sum = 0
        doublepairsum = 0
            
    print(doublepairsum)
    label_result.config(text="Result from doublepair points %d" %doublepairsum)
    return

def calculate_trio_points(label_result):
    triosum = 0
    for i in range(0,len(box_counter),1):
        if box_counter[i].get() == 3:
            triosum = triosum + box_counter[i].get() * TRIO_MULTIPLIER_LIST[i%6] 
    print(triosum)
    label_result.config(text="Result from trio points %d" %triosum)
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
    
    
























box_counter = [counterH9, counterH10, counterHJ, counterHQ, counterHK, counterHA,
               counterT9, counterT10, counterTJ, counterTQ, counterTK, counterTA,
               counterC9, counterC10, counterCJ, counterCQ, counterCK, counterCA,
               counterP9, counterP10, counterPJ, counterPQ, counterPK, counterPA,]


## tekst na ekranie oznaczenia kart HEARTS $$$$$$$$$$$$$$$$$$$

labelTitle = tk.Label(MainWindow, text="Hearts").grid(row=0, column=2)


labelNum9 = tk.Label(MainWindow, text="9").grid(row=1, column=0)
nineEntry = tk.Entry(MainWindow)

labelNum10 = tk.Label(MainWindow, text="10").grid(row=2, column=0)
HtenEntry = tk.Entry(MainWindow)

labelNumJ = tk.Label(MainWindow, text="J").grid(row=3, column=0)
HjackEntry = tk.Entry(MainWindow)

labelNumQ = tk.Label(MainWindow, text="Q").grid(row=4, column=0)
HquuenEntry = tk.Entry(MainWindow)

labelNumK = tk.Label(MainWindow, text="K").grid(row=5, column=0)
HkingEntry = tk.Entry(MainWindow)

labelNumA = tk.Label(MainWindow, text="A").grid(row=6, column=0)
HaceEntry = tk.Entry(MainWindow)


##############################




## tekst na ekranie oznaczenia kart TILES ^^^^^^^^^^^^^^^^^^

labelTitle = tk.Label(MainWindow, text="TILES").grid(row=0, column=2 + SHIFTBETWEENCARDS)


labelNum9 = tk.Label(MainWindow, text="9").grid(row=1, column=0 + SHIFTBETWEENCARDS + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
TnineEntry = tk.Entry(MainWindow)

labelNum10 = tk.Label(MainWindow, text="10").grid(row=2, column=0 + SHIFTBETWEENCARDS + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES )
TtenEntry = tk.Entry(MainWindow)

labelNumJ = tk.Label(MainWindow, text="J").grid(row=3, column=0 + SHIFTBETWEENCARDS + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES) 
TjackEntry = tk.Entry(MainWindow)

labelNumQ = tk.Label(MainWindow, text="Q").grid(row=4, column=0 + SHIFTBETWEENCARDS + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
TquuenEntry = tk.Entry(MainWindow)

labelNumK = tk.Label(MainWindow, text="K").grid(row=5, column=0 + SHIFTBETWEENCARDS + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
TkingEntry = tk.Entry(MainWindow)

labelNumA = tk.Label(MainWindow, text="A").grid(row=6, column=0 + SHIFTBETWEENCARDS + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
TaceEntry = tk.Entry(MainWindow)


##############################






## tekst na ekranie oznaczenia kart CLOVERS &&&&&&&&&&&&&&&&&&&

labelTitle = tk.Label(MainWindow, text="CLOVERS").grid(row=0, column=2 + SHIFTBETWEENCARDS * 2)


labelNum9 = tk.Label(MainWindow, text="9").grid(row=1, column=0 + SHIFTBETWEENCARDS * 2 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CnineEntry = tk.Entry(MainWindow)

labelNum10 = tk.Label(MainWindow, text="10").grid(row=2, column=0 + SHIFTBETWEENCARDS * 2 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CtenEntry = tk.Entry(MainWindow)

labelNumJ = tk.Label(MainWindow, text="J").grid(row=3, column=0 + SHIFTBETWEENCARDS * 2 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES) 
CjackEntry = tk.Entry(MainWindow)

labelNumQ = tk.Label(MainWindow, text="Q").grid(row=4, column=0 + SHIFTBETWEENCARDS * 2 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CquuenEntry = tk.Entry(MainWindow)

labelNumK = tk.Label(MainWindow, text="K").grid(row=5, column=0 + SHIFTBETWEENCARDS * 2 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CkingEntry = tk.Entry(MainWindow)

labelNumA = tk.Label(MainWindow, text="A").grid(row=6, column=0 + SHIFTBETWEENCARDS * 2 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CaceEntry = tk.Entry(MainWindow)


##############################



## tekst na ekranie oznaczenia kart PIKES **********************

labelTitle = tk.Label(MainWindow, text="PIKES").grid(row=0, column=2 + SHIFTBETWEENCARDS * 3)


labelNum9 = tk.Label(MainWindow, text="9").grid(row=1, column=0 + SHIFTBETWEENCARDS * 3 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
nineEntry = tk.Entry(MainWindow)



labelNum10 = tk.Label(MainWindow, text="10").grid(row=2, column=0 + SHIFTBETWEENCARDS * 3 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CtenEntry = tk.Entry(MainWindow)

labelNumJ = tk.Label(MainWindow, text="J").grid(row=3, column=0 + SHIFTBETWEENCARDS * 3 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES) 
CjackEntry = tk.Entry(MainWindow)

labelNumQ = tk.Label(MainWindow, text="Q").grid(row=4, column=0 + SHIFTBETWEENCARDS * 3 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CquuenEntry = tk.Entry(MainWindow)

labelNumK = tk.Label(MainWindow, text="K").grid(row=5, column=0 + SHIFTBETWEENCARDS * 3 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CkingEntry = tk.Entry(MainWindow)

labelNumA = tk.Label(MainWindow, text="A").grid(row=6, column=0 + SHIFTBETWEENCARDS * 3 + SHIFTADJUSTMENT, padx = PADXBETWEENCARDNAMES)
CaceEntry = tk.Entry(MainWindow)


##############################




















## pasek do wpisywania zmiennych HEARTS $$$$$$$$$$$$

entryNumH9 = tk.Entry(MainWindow, textvariable=counterH9, width = 4).grid(row=1, column=2)
entryNumH10 = tk.Entry(MainWindow, textvariable=counterH10, width = 4).grid(row=2, column=2)
entryNumHJ = tk.Entry(MainWindow, textvariable=counterHJ, width = 4).grid(row=3, column=2)
entryNumHQ = tk.Entry(MainWindow, textvariable=counterHQ, width = 4).grid(row=4, column=2)
entryNumHK = tk.Entry(MainWindow, textvariable=counterHK, width = 4).grid(row=5, column=2)
entryNumHA = tk.Entry(MainWindow, textvariable=counterHA, width = 4).grid(row=6, column=2)


##


## pasek do wpisywania zmiennych TILES ^^^^^^^^^^^^^^^^^

entryNumT9 = tk.Entry(MainWindow, textvariable=counterT9, width = 4).grid(row=1, column=2 + SHIFTBETWEENCARDS)
entryNumT10 = tk.Entry(MainWindow, textvariable=counterT10, width = 4).grid(row=2, column=2 + SHIFTBETWEENCARDS)
entryNumTJ = tk.Entry(MainWindow, textvariable=counterTJ, width = 4).grid(row=3, column=2 + SHIFTBETWEENCARDS)
entryNumTQ = tk.Entry(MainWindow, textvariable=counterTQ, width = 4).grid(row=4, column=2 + SHIFTBETWEENCARDS)
entryNumTK = tk.Entry(MainWindow, textvariable=counterTK, width = 4).grid(row=5, column=2 + SHIFTBETWEENCARDS)
entryNumTA = tk.Entry(MainWindow, textvariable=counterTA, width = 4).grid(row=6, column=2 + SHIFTBETWEENCARDS)


##



## pasek do wpisywania zmiennych CLOVERS &&&&&&&&&&&&&&&&&&&

entryNumC9 = tk.Entry(MainWindow, textvariable=counterC9, width = 4).grid(row=1, column=2 + SHIFTBETWEENCARDS * 2)
entryNumC10 = tk.Entry(MainWindow, textvariable=counterC10, width = 4).grid(row=2, column=2 + SHIFTBETWEENCARDS * 2)
entryNumCJ = tk.Entry(MainWindow, textvariable=counterCJ, width = 4).grid(row=3, column=2 + SHIFTBETWEENCARDS * 2)
entryNumCQ = tk.Entry(MainWindow, textvariable=counterCQ, width = 4).grid(row=4, column=2 + SHIFTBETWEENCARDS * 2)
entryNumCK = tk.Entry(MainWindow, textvariable=counterCK, width = 4).grid(row=5, column=2 + SHIFTBETWEENCARDS * 2)
entryNumCA = tk.Entry(MainWindow, textvariable=counterCA, width = 4).grid(row=6, column=2 + SHIFTBETWEENCARDS * 2)


##



## pasek do wpisywania zmiennych PIKES **********************

entryNumP9 = tk.Entry(MainWindow, textvariable=counterP9, width = 4).grid(row=1, column=2 + SHIFTBETWEENCARDS * 3)
entryNumP10 = tk.Entry(MainWindow, textvariable=counterP10, width = 4).grid(row=2, column=2 + SHIFTBETWEENCARDS * 3)
entryNumPJ = tk.Entry(MainWindow, textvariable=counterPJ, width = 4).grid(row=3, column=2 + SHIFTBETWEENCARDS * 3)
entryNumPQ = tk.Entry(MainWindow, textvariable=counterPQ, width = 4).grid(row=4, column=2 + SHIFTBETWEENCARDS * 3)
entryNumPK = tk.Entry(MainWindow, textvariable=counterPK, width = 4).grid(row=5, column=2 + SHIFTBETWEENCARDS * 3)
entryNumPA = tk.Entry(MainWindow, textvariable=counterPA, width = 4).grid(row=6, column=2 + SHIFTBETWEENCARDS * 3)


##









##### PRZYCISKI do zmiany wartosci HEARTS $$$$$$$$$$$$$$$$$$$$$

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterH9)).grid(row=1, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterH9)).grid(row=1, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterH10)).grid(row=2, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterH10)).grid(row=2, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterHJ)).grid(row=3, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterHJ)).grid(row=3, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterHQ)).grid(row=4, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterHQ)).grid(row=4, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterHK)).grid(row=5, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterHK)).grid(row=5, column=4)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterHA)).grid(row=6, column=3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterHA)).grid(row=6, column=4)



#######


##### PRZYCISKI do zmiany wartosci TILES ^^^^^^^^^^^^^^^^^^^^^^^^

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterT9)).grid(row=1, column=3 + SHIFTBETWEENCARDS)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterT9)).grid(row=1, column=4 + SHIFTBETWEENCARDS)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterT10)).grid(row=2, column=3 + SHIFTBETWEENCARDS)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterT10)).grid(row=2, column=4 + SHIFTBETWEENCARDS)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterTJ)).grid(row=3, column=3 + SHIFTBETWEENCARDS)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterTJ)).grid(row=3, column=4 + SHIFTBETWEENCARDS)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterTQ)).grid(row=4, column=3 + SHIFTBETWEENCARDS)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterTQ)).grid(row=4, column=4 + SHIFTBETWEENCARDS)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterTK)).grid(row=5, column=3 + SHIFTBETWEENCARDS)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterTK)).grid(row=5, column=4 + SHIFTBETWEENCARDS)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterTA)).grid(row=6, column=3 + SHIFTBETWEENCARDS)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterTA)).grid(row=6, column=4 + SHIFTBETWEENCARDS)



##### PRZYCISKI do zmiany wartosci CLOVERS &&&&&&&&&&&&&&&&&&&&&&&

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterC9)).grid(row=1, column=3 + SHIFTBETWEENCARDS * 2)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterC9)).grid(row=1, column=4 + SHIFTBETWEENCARDS * 2)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterC10)).grid(row=2, column=3 + SHIFTBETWEENCARDS * 2)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterC10)).grid(row=2, column=4 + SHIFTBETWEENCARDS * 2)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterCJ)).grid(row=3, column=3 + SHIFTBETWEENCARDS * 2)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterCJ)).grid(row=3, column=4 + SHIFTBETWEENCARDS * 2)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterCQ)).grid(row=4, column=3 + SHIFTBETWEENCARDS * 2)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterCQ)).grid(row=4, column=4 + SHIFTBETWEENCARDS * 2)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterCK)).grid(row=5, column=3 + SHIFTBETWEENCARDS * 2)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterCK)).grid(row=5, column=4 + SHIFTBETWEENCARDS * 2)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterCA)).grid(row=6, column=3 + SHIFTBETWEENCARDS * 2)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterCA)).grid(row=6, column=4 + SHIFTBETWEENCARDS * 2)




##### PRZYCISKI do zmiany wartosci PIKES **************************

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterP9)).grid(row=1, column=3 + SHIFTBETWEENCARDS * 3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterP9)).grid(row=1, column=4 + SHIFTBETWEENCARDS * 3)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterP10)).grid(row=2, column=3 + SHIFTBETWEENCARDS * 3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterP10)).grid(row=2, column=4 + SHIFTBETWEENCARDS * 3)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterPJ)).grid(row=3, column=3 + SHIFTBETWEENCARDS * 3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterPJ)).grid(row=3, column=4 + SHIFTBETWEENCARDS * 3)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterPQ)).grid(row=4, column=3 + SHIFTBETWEENCARDS * 3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterPQ)).grid(row=4, column=4 + SHIFTBETWEENCARDS * 3)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterPK)).grid(row=5, column=3 + SHIFTBETWEENCARDS * 3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterPK)).grid(row=5, column=4 + SHIFTBETWEENCARDS * 3)

buttonCal = tk.Button(MainWindow, text="+", command=lambda:add(counterPA)).grid(row=6, column=3 + SHIFTBETWEENCARDS * 3)
buttonCal = tk.Button(MainWindow, text="-", command=lambda:sub(counterPA)).grid(row=6, column=4 + SHIFTBETWEENCARDS * 3)








#######


##### wynik pod buttonami

singleResultLabel = tk.Label(MainWindow)
singleResultLabel.grid(row=7, column=2)

pairResultLabel = tk.Label(MainWindow)
pairResultLabel.grid(row=8, column=2)


doublepairResultLabel = tk.Label(MainWindow)
doublepairResultLabel.grid(row=9, column=2)

trioResultLabel = tk.Label(MainWindow)
trioResultLabel.grid(row=10, column=2)


#######
label = tk.Label(MainWindow, textvariable=x)
label.grid(row=8, column=0)








### funkcje liczone przez partial musza byc przed buttonami!!!!!!!!!!!!!

call_result = partial(call_result, singleResultLabel, number1)
substract_one = partial(substract_one, singleResultLabel, equation)

check_value = partial(check_value, singleResultLabel, number1)
calculate_single_points = partial(calculate_single_points, singleResultLabel, hand)

calculate_pair_points = partial(calculate_pair_points, pairResultLabel)

calculate_double_pair_points = partial(calculate_double_pair_points, doublepairResultLabel)

calculate_trio_points = partial(calculate_trio_points, trioResultLabel)

show_cards_left_buttons = partial(show_cards_left_buttons, cardsLeft)


check_left_cards_in_deck = partial(check_left_cards_in_deck, cardsLeft)

pick_random_card_from_left_cards = partial(pick_random_card_from_left_cards, cardsLeft)

# for karta in LISTAKART:
#     add[karta]=partial(add,karta)
#     print(karta)
# add=partial(add,x)

























########### PRZYCISKI ZWIAZANE Z LOGIKA I PUNKTACJA



buttonCal = tk.Button(MainWindow, text="single", command=calculate_single_points).grid(row=9, column=0)

buttonCal = tk.Button(MainWindow, text="pair", command=calculate_pair_points).grid(row=9, column=3)


buttonCal = tk.Button(MainWindow, text="doublepair", command=calculate_double_pair_points).grid(row=9, column=10)

buttonCal = tk.Button(MainWindow, text="trio", command=calculate_trio_points).grid(row=10, column=10)



buttonCal = tk.Button(MainWindow, text="checkcard", command=check_left_cards_in_deck).grid(row=11, column=10)

buttonCal = tk.Button(MainWindow, text="Show left cards", command=show_cards_left_buttons).grid(row=11, column=14)



buttonCal = tk.Button(MainWindow, text="Pick random card", command=pick_random_card_from_left_cards).grid(row=11, column=17)


buttonCal = tk.Button(MainWindow, text="Update hand", command=update_hand).grid(row=11, column=20)











MainWindow.mainloop()


