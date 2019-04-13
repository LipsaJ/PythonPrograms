# import BlackJack  # this directly executes the code we dont want that
from BlackJack import *  # it imports everything except _deal_card that ways python knows that protected shouldnt
# be imported

# for x in globals():
#     print(x)

# the above code doesnt work
g = sorted(globals())
for x in g:
    print(x)

# so now when we run import test it  doesnt execute the blackjack, we put a __main__ statement in blackjack program
# BlackJack.play()
# print(__name__)
# print(BlackJack.cards)

# underscores in python:
# for example from is a keyword in python so you can create from_

# python has got no concept of private and protected variables so its possible to do things which you shouldnt be doing
# in a module

# by convention in python a variable starting with _ is meant to be protected that means not to be used outside module
# for example we can change deal_card to _deal_card using re-factor, after using refactor deal_cards is modifies every
# place including in our new code import_test

# BlackJack._deal_card()  # so here python gives a warning that it a protected member so shouldnt be used

# Anything starting and ending with two __ shouldnt be changed for example "__name__"

personal_details = {"Lipsa", 27, "India"}
name, _, country = personal_details
print(name, country)
print(_)  # so only a single _ declares a throwaway variable, for example here we are not intrested in age so we just
# execute the first print(name, country) even though print(_) works but _ is mostly used for some useless thing which
# you are not intrested in

# so in tthe above tupple its neccessary for the column age so that others columns are prited/extracted correctly thats
# why we have use a throwable variable _ because its a necessity
