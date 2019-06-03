from __future__ import print_function
wff = "a>bvc>d>e"

# for each connective
connectives = ['>', 'v']

f = open("tenOperators.txt", "w+")

# returns index of wff
def findConnective(wff, indexes):                             
    for i, char in enumerate(wff):                      # looping through all chars in wff
        if set([i]) & set(indexes):                     # if operator has already been used
            continue
        else:                                           # if operator has not been usedl
            if char in connectives:                     # if the wff contains the connective
                indexes.append(i)                       # keeps track of which operators have already been used
                return i

# returns number of connectives
def numConnectives(wff):
    count = 0
    for c in wff:
        if c in connectives:
            count += 1
    return count

# returns what's on left of operator
def createLeft(wff, opIndex):
    return wff[:opIndex]

# returns what's on right of operator
def createRight(wff, opIndex):
    return wff[opIndex+1:]

# recursive algorithm
def rec(wff):
    ind = []                                        # storing indexes of operators used
    if len(wff) == 1:
        yield wff
        return 
    else:
        for i in range(numConnectives(wff)):        # loop through all of the operators
            opIndex = findConnective(wff, ind)      # index where the operator is at
            right   = createRight(wff, opIndex)     # formula to the right of the operator
            left    = createLeft(wff, opIndex)      # formula to the left of the operator
            for left_subexpr in rec(left):
                for right_subexpr in rec(right):
                    yield "(" + left_subexpr + ")" + wff[opIndex] + "(" + right_subexpr + ")"

result = rec(wff)
for index, x in enumerate(result):
    print(index, x)
