# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 07:55:32 2019
@author: Jonathan

From Introduction to Computation and Programming Using Python, p. 47

Shows implementation of recursion in the helper method isPal(word).
Includes example of base cases, here 0, 1. When met stops program reaching
    recursive part of implementation.

This implementation of recursion is an example of the divide-and-conquer
    problem solving principle; i.e. conquer hard problem by decomposing, and:
    1. subproblems easier to solve than original
    (whether shorter string is a palindrome by comparing chars).
    2. solutions of subproblems can be combined to solve the problem
    (using and: if all compared chars are equal, string palindome, isn't).
    
This implementation of recursion demonstrates the use of global variables,
    NumCalls, used to track times recursion occurs in determining if
    word is a palindrome.
"""

NumCalls = 0


def isPalindrome(word):
    """
    Assumes word is str type object.

    Returns True if characters of word make up palindrome,
    Returns False otherwise. Non-letters, capitalisation, ignored.

    Helper Methods
    --------------
    toChars(word) converts input string to lower-case english characters.

    isPal(word) check equality in outer word chars recursively moving inwards.
    """

    # HELPER METHOD 1: convert input word to lower-case char array
    def toChars(word):

        global NumCalls
        alphabet_english = "abcdefghijklmnopqrstuvwxyz"
        word = word.lower()
        letters = ""

        for character in word:
            if character in alphabet_english:
                letters += character
        return letters

    # HELPER METHOD 2: check if first, last chars in word match;
    # if so check next-inner pair recursively until gone through all chars
    def isPal(word):

        global NumCalls
        # recursive base cases: strings of length 0, 1
        if len(word) <= 1:
            NumCalls += 1
            print("Word:", word, "word[0]", word[0], "word[-1]", word[-1])
            print(NumCalls, "Length of word 1: RECURSION COMPLETE")
            NumCalls = 0
            return True
        else:
            NumCalls += 1
            print("Word:", word, "word[0]", word[0], "word[-1]", word[-1])
            print(NumCalls, "Length of word > 1: RECURSION...")
            # if chars same and word minus these chars is palidrome
            return word[0] == word[-1] and isPal(word[1:-1])

    print("Numcalls reset to 0, is", NumCalls)

    return isPal(toChars(word))


def testIsPalindrome():
    test_word_palindrome = "racecar"
    test_word_palindrome_not = "racxecar"

    print("Checking:", test_word_palindrome)
    print(test_word_palindrome, " palindrome:",
          isPalindrome(test_word_palindrome))
    print("")
    print("Checking:", test_word_palindrome_not)
    print(test_word_palindrome_not, "palindrome:",
          isPalindrome(test_word_palindrome_not))


testIsPalindrome()
