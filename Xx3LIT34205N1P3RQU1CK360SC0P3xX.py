

def startTelescope(eventList):
    DP = []  # vector<stack<time>> DP
    DP.append(0)

    for i in range(len(eventList)):
        DP.append([])   #append empty list to make a 2d list
    path = telescope(0,0, eventList, DP)
    return (path)#, traceback(path, eventList))

def telescope(time, position, eventList, DP):
    PATH = []            # stack Path<time>;
    for eventTime in range(time+1,len(eventList)):
        if ((abs(position - eventList[eventTime]) <= eventTime-time)):
            telescope(eventTime, eventList[eventTime], eventList, DP)
            if len(DP[eventTime]) > len(PATH):
                PATH = DP[eventTime]
    # if (time != 0):  # start is not an event
    DP[time] = PATH
    DP[time].append(time)
    print("DP at time: ", time, " --> ", DP[time])
    return DP[time]

def traceback(eventList, times):
    moves = "{" # init empty string
    cur_pos, time = 0,0  # initial position & time == 0
    times.pop() # pop out the 0
    while (len(times) != 0):
        eventTime = times.pop()

        while cur_pos < eventList[eventTime]:
            moves += "+1, "
            cur_pos += 1
            time += 1
        while cur_pos > eventList[eventTime]:
            moves += "-1, "
            cur_pos -= 1
        while (time != eventTime):
            moves += "0, "
            time += 1
        # times.pop()
    moves += "}"
    return moves

eventList = [0, 1,-4,-1,4,5,-4,6,7,-2]
path = startTelescope(eventList)
print(len(path))
print(path)
print(traceback(eventList, path))
