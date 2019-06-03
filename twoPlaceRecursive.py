from __future__ import print_function
wff = "a>b>c>d"
# wff = "a"
wff2 = "a"

# for each connective
connectives = '>'

f = open("tenOperators.txt", "w+")

# returns index of wff
def findConnective(wff, indexes):
    if len(wff) == None:
        return -1
    if (len(wff) <= 1):
        return -1                                   # it's an atomic

    for i in range(len(wff)):                       # looping through all chars in wff
        # print("we're inside")
        if set([i]) & set(indexes):                     # if operator has already been used
            continue
        else:                                           # if operator has not been usedl
            for j in range(len(connectives)):           # looping through all of the connectives
                if wff[i] == connectives[j]:            # if the wff contains the connective
                    indexes.append(i)                   # keeps track of which operators have already been used
                    return i

# returns number of connectives
def numConnectives(wff):
    count = 0
    for c in wff:
        if c == connectives:
            count += 1
    return count

# for i in range(numConnectives(wff)):

# returns what's on left of operator
def createLeft(wff, opIndex):
    if opIndex == -1:
        return wff          # return the atomic
    else:
        return wff[:opIndex]

# returns what's on right of operator
def createRight(wff, opIndex):
    if opIndex == -1:
        return wff          # return the atomic
    else:
        return wff[opIndex+1:]

def rec(wff):
    ind = []                                        # list storing indexes of operators used
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

count = 0
for index, x in enumerate(result):
    count += 1

    print(str(index+1).ljust(4) + "  " + x + "\n")
print(count)