from __future__ import print_function
wff = input("Enter SL sentence: ")

# for each connective
two_place_conns = ['>', 'v', '&']
one_place_conn = '-'

f = open("tenOperators.txt", "w+")

# returns index of wff
def findConnective(wff, indexes):                             
    for i, char in enumerate(wff):                      # looping through all chars in wff
        if set([i]) & set(indexes):                     # if operator has already been used
            continue
        else:                                           # if operator has not been usedl
            if char in two_place_conns or char in one_place_conn:                     # if the wff contains the connective
                indexes.append(i)                       # keeps track of which operators have already been used
                return i

# returns number of two_place_conns
def numTwoPlaceConns(wff):
    count = 0
    for c in wff:
        if c in two_place_conns:
            count += 1
    return count

# returns num one_place_conns
def numOnePlaceConns(wff):
    count = 0
    for c in wff:
        if c == one_place_conn:
            count += 1
    return count

# returns num 1 and 2-place connectives 
def numConnectives(numOnePlaceConns, numTwoPlaceConns):
    return numOnePlaceConns + numTwoPlaceConns

# returns what's on left of operator
def createLeft(wff, opIndex):
    return wff[:opIndex]

# returns what's on right of operator
def createRight(wff, opIndex):
    return wff[opIndex+1:]

# recursive algorithm
def rec(wff):
    ind = []                                        # storing indexes of operators used
    if len(wff) == 1 and wff not in one_place_conn:
        yield wff
        return
    if len(wff) == 2 and one_place_conn in wff and (wff[0] and wff[1] not in one_place_conn):  # in the case 1-place operator
        yield wff
        return 
    else:
        for i in range(numConnectives(numOnePlaceConns(wff), numTwoPlaceConns(wff))):        # loop through all of the operators
            opIndex = findConnective(wff, ind)      # index where the operator is at
            right   = createRight(wff, opIndex)     # formula to the right of the operator
            left    = createLeft(wff, opIndex)      # formula to the left of the operator
            if (wff[opIndex] == one_place_conn):
                if (len(left) > 0):
                    for left_subexpr in rec(left):
                        for right_subexpr in rec(right):
                            yield "(" + left_subexpr + ")" + wff[opIndex] + "(" + right_subexpr + ")"
                else:
                    if (len(right)>1):
                        for right_subexpr in rec(right):
                            yield wff[opIndex] + "(" + right_subexpr + ")"
                    else:
                        break
            else:
                for left_subexpr in rec(left):
                    for right_subexpr in rec(right):
                        yield "(" + left_subexpr + ")" + wff[opIndex] + "(" + right_subexpr + ")"

result = rec(wff)

print("---------------All possible well-formed formulas---------------")

for index, x in enumerate(result):
    print(index+1, x)