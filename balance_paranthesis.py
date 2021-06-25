"""
Given a string of paranthesis check if it is balanced or not.

For every opening of a paranthesis one needs to have a closing paranthesis for it
to be considered as balanced.

Ex: (())() is balanced
"""

if __name__ == "__main__":
    STRING = input().strip()
    SYMBOL = list(STRING)
    lcount, rcount = 0, 0

    for sym in SYMBOL:
        if sym == "(":
            lcount += 1
        else:
            rcount += 1

    if lcount != rcount:
        print("Unbalanced")
    else:
        print("Balanced")
