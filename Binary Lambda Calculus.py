
def wheredoeswffstop(bitvector, start):
    d91 = False
    focus = start
    OK = True
    vertical = 0
    stack = []
    while OK and (focus < len(bitvector)):
        DEBUG(d91, f"\n9. focus = {focus}")
        if bitvector[focus] == 1:
            stack.append(1)
            focus += 1
            vertical += 1
            DEBUG(d91, f"14. stack = {stack}\nfocus = {focus}\nvertical = {vertical}")
        elif bitvector[focus] == 0:
            stack.append(0)
            focus += 2
            OK2 = True
            while OK2:
                if stack[-1] == 0:
                    if (len(stack) >= 2) and (stack[-2] == 0):
                        if (len(stack) >= 3) and (stack[-3] == 1):
                            stack.pop()
                            stack.pop()
                            stack.pop()
                            stack.append(0)
                            vertical -= 1
                        else:
                            OK2 = False
                    else:
                        OK2 = False
                else:
                    OK2 = False
            DEBUG(d91, f"34. stack = {stack}\nfocus = {focus}\nvertical = {vertical}")
            if vertical < 0:
                #focus -= 1
                OK = False
            if vertical == 0:
                OK = False
    if vertical == 0:
        return focus - 1
    else:
        return False

"Note: vertical could instead be obtained by counting the quantity of 1s in the stack."

"Example: wheredoeswffstop([1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], 0)"

def isbitvectorwellformed(bitvector):
    wherestop = wheredoeswffstop(bitvector, 0)
    if wherestop == len(bitvector) - 1:
        return True
    else:
        return False

def rewritewff(bitvector):
    d135 = False
    focus = 0
    while focus < len(bitvector):
        if bitvector[focus] == 1:
            DEBUG(d135, f"61. focus = {focus}")
            stopswhere = wheredoeswffstop(bitvector, focus)
            DEBUG(d135, f"63. stopswhere = {stopswhere}")
            if type(stopswhere) is type(5):
                if ((focus + 1) < len(bitvector)) and (bitvector[focus + 1] == 1):
                    if ((focus + 2) < len(bitvector)) and (bitvector[focus + 2] == 0):
                        if ((focus + 3) < len(bitvector)) and (bitvector[focus + 3] == 0):
                            startx = focus + 4
                            DEBUG(d135, f"69. startx = {startx}")
                            if (startx < len(bitvector)):
                                stopx = wheredoeswffstop(bitvector, startx)
                                starty = stopx + 1
                                DEBUG(d135, f"73. starty = {starty}")
                                if (starty < len(bitvector)):
                                    stopy = wheredoeswffstop(bitvector, starty)
                                    x = bitvector[startx:stopx + 1]
                                    DEBUG(d135, f"77. x = {x}")
                                    leftcontext = bitvector[:focus]
                                    rightcontext = bitvector[stopy + 1:]
                                    DEBUG(d135, f"81. leftcontext = {leftcontext}")
                                    DEBUG(d135, f"82. rightcontext = {rightcontext}")
                                    return leftcontext + x + rightcontext
                    elif ((focus + 2) < len(bitvector)) and (bitvector[focus + 2] == 1):
                        if ((focus + 3) < len(bitvector)) and (bitvector[focus + 3] == 0):
                            if ((focus + 4) < len(bitvector)) and (bitvector[focus + 4] == 1):
                                startx = focus + 5
                                if startx < len(bitvector):
                                    stopx = wheredoeswffstop(bitvector, startx)
                                    starty = stopx + 1
                                    if starty < len(bitvector):
                                        stopy = wheredoeswffstop(bitvector, starty)
                                        startz = stopy + 1
                                        if startz < len(bitvector):
                                            stopz = wheredoeswffstop(bitvector, startz)
                                            x = bitvector[startx:stopx + 1]
                                            y = bitvector[starty:stopy + 1]
                                            z = bitvector[startz:stopz + 1]
                                            leftcontext = bitvector[:focus]
                                            rightcontext = bitvector[stopz + 1:]
                                            return leftcontext + [1,1] + x + z + [1] + y + z + rightcontext
        focus += 1
    DEBUG(d135, "103. No change.")
    return bitvector

"rewritewff([1,1,1,0,1,0,0,0,0,0,1]) #=> [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]"
"rewritewff([1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]) #=> [0, 1]"
"rewritewff([1,1,0,0,1,0,1,0,0,0,0]) #=> [1, 0, 1, 0, 0]"
"rewritewff([1,1,1,0,1,0,0,1,0,1,0,0,0,0]) #=> [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]"
"rewritewff([1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]) #=> [0, 0]"
            
                            
def DEBUG(flag, msg):
    if flag:
        print(msg)
