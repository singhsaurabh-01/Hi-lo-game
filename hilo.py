low = 1
high = 1000
guesses = 1
while low != high:
    guess = low + (high - low) // 2
    print("\tNow I am guessing in the range of {} and {}".format(low, high))
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Press h or l, or c if my guess is correct: "
                     .format(guess).casefold())
    if high_low == 'h':
        # Set high_low value 1 less then guess if the value was guessed higher then expected
        low = guess + 1
    elif high_low == 'l':
        # set high_low value 1 greater then guessed value if it was guessed lower then expected
        high = guess - 1
    elif high_low == 'c':
        print("I guessed it right in {} attempts".format(guesses))
        break
    else:
        print("please enter h, l or c")

    # guesses = guesses + 1
    guesses += 1 # This is augmented assignment

else:
    print("The only Guess left is now {}".format(low))
    print("I guessed it in {} attempts".format(guesses))
