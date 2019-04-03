# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:12:56 2019
@author: Jonathan

(SQUARE) ROOT FINDING ALGORITHMS: 3 successively more efficient algorithms

1. Exhaustive Enumeration - LEAST efficient
2. Bisection Search (Binary Search) - MORE efficient
3. Newton Raphson (Successive approximation) - MOST efficient
"""


def squareRootExhaustiveEnumeration():
    """
    Assumes user inputs float.

    Prints approximate square root of input integer.
    Prints number of guesses (enumerations) taken to find square root.
    Fails is answer not in set of enumerated values.

    Iterates, increases answer until close enough and not too large.

    Lower epsilon value increases enumerations, accuracy.
    """
    # 1. DECLARE, INITIALISE VARIABLES
    x = float(input("Find approximate square root of: "))
    epsilon = 0.1
    step = epsilon ** 2
    numGuesses = 0
    ans = 0

    # 2. ITERATE WHILE ANS NOT CLOSE ENOUGH OR TOO LARGE
    while abs(ans ** 2 - x) >= epsilon and ans*ans <= x:
        ans += step
        numGuesses += 1

    # 3. ONCE ANS CLOSE ENOUGH OR TOO LARGE, PRINT USER OUTPUT
    if abs(ans ** 2 - x) >= epsilon:
        print("Failed on square root of", x)
    else:
        print("Espilon", epsilon, "approximate square root of", x, " is:", ans)
    print("numGuesses:", numGuesses, "ans:", ans)


def squareRootBisectionSearch():
    """
    Assumes user inputs float.

    Prints approximate square root of input integer.
    Prints number of guesses (enumerations) taken to find square root.

    Iterates, halves interval (search space) until answer close enough.

    Lower epsilon value increases enumerations, accuracy.
    """
    # 1. DECLARE, INITIALISE VARIABLES
    x = float(input("Find approximate square root of: "))
    epsilon = 0.01
    numGuesses = 0
    low = 0
    high = max(1.0, x)  # to allow finding roots of 0-1
    ans = (low + high) / 2

    # 2. ITERATE WHILE ANS TOO LARGE OR SMALL
    while abs((ans ** 2 - x)) >= epsilon:
        numGuesses += 1

    # 3. RECUCE INTERVAL (SEARCH SPACE) BY HALF EVERY GUESS
        # if guess was too low set lower boundry to guess
        if ans ** 2 < x:
            low = ans
        # if guess was too high set higher boundry to guess
        else:
            high = ans
        ans = (low + high) / 2

    # 4. PRINT USER OUTPUT
    print("Approximate square root of", x, "is", ans)
    print("numGuesses:", numGuesses)


def squareRootNewtonRaphson():
    """
    Assumes user inputs positive float (converts to absolute value).

    Prints approximate square root of input integer.
    Prints number of guesses (enumerations) taken to find square root.

    Iterates, reduces ans until ans close enough to epsilon (I don't fully
    undestand the math behind this).

    Lower epsilon value increases enumerations, accuracy.
    """
    # 1. DECLARE, INITIALISE VARIABLES
    epsilon = 0.01
    number = abs(float(input("Find square root of: ")))
    ans = number/2.0
    guesses = 0

    # 2. ITERATE WHILE ANS TOO LARGE
    while abs((ans * ans) - number) >= epsilon:
        guesses += 1
        ans = ans - (((ans ** 2) - number)/(2 * ans))

    # 3. PRINT USER OUTPUT
    print("Square root of:", number, ":", ans, "(epsilon", epsilon, ")")
    print("Guesses:", guesses)
