# If you
import random
# then use random.randrange(2).

# If you do
from random import randrange
# then use randrange(2)
# directly.

# You could use
import random as r

# to create r as shorthand or an alias for random.
# Then do
r.randrange(2)


def blackjack_hand(player_hand, dealer_hand):
    '''Print the player wins under one case:
    the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21'''
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")
    # We can always optionally include explicitly
    # that the function should return to the point
    # of call.
    return


# blackjack_hand(13, 8)

def blackjack_hand2(player_hand, dealer_hand):
    '''Return the string 'The player wins!' under one case:
    the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.
    Otherwise, return 'Inconclusive'.'''
    if (player_hand > dealer_hand) and (player_hand <= 21):
        return "The player wins!"
    else:
        return "Inconclusive"


def exploration():
    # The returned value from blackjack_hand2 replaces
    # the function call.

    # You have to print a returned value in order to see it.
    print(blackjack_hand2(13, 8))

    # Compare our custom function that returns a value
    # to built-in functions that return values.

    # The returned value from type replaces
    # the function call.
    type("The player loses!")

    # You have to print a returned value in order to see it.
    print(type("The player loses!"))

    # The returned value from randrange replaces
    # the function call.
    r.randrange(2)

    # You have to print a returned value in order to see it.
    print(r.randrange(2))


# exploration()

# print(blackjack_hand2(10, 20))

def blackjack_hand3(player_hand, dealer_hand):
    '''Return True under one case:
    the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.
    Otherwise, return False.'''
    if (player_hand > dealer_hand) and (player_hand <= 21):
        return True
    else:
        return False


# print(blackjack_hand3(8, 21))

# print(f'The condition was met for a win: {blackjack_hand3(8, 21)}.')

# print(f'The condition was met for a win: {blackjack_hand3(13, 8)}.')


# Streamline a function that returns a boolean to avoid if-else.
def blackjack_hand4(player_hand, dealer_hand):
    '''Return whether player wins in one case:
    the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.'''
    return (player_hand > dealer_hand) and (player_hand <= 21)


# print(blackjack_hand4(8, 21))

# print(f'The condition was met for a win: {blackjack_hand4(8, 21)}.')

# print(f'The condition was met for a win: {blackjack_hand4(13, 8)}.')

def blackjack_hand5(player_hand, dealer_hand):
    '''Return whether player wins in one case:
    the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.'''
    # This x is inside the function.
    # Variables are local to the functions in which they are defined.
    x = (player_hand > dealer_hand) and (player_hand <= 21)
    return x


# print(blackjack_hand5(13, 8))
# This x is outside the function.
# The variable x is not recognized outside the function.
# print(x)

# For appropriately streamlined code, avoid the use of a temporary
# variable x to return.
# Return the value directly.
def blackjack_hand6(player_hand, dealer_hand):
    '''Return whether player wins in one case:
    the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.'''
    # This x is inside the function.
    # Variables are local to the functions in which they are defined.
    return (player_hand > dealer_hand) and (player_hand <= 21)


print(blackjack_hand6(13, 8))
