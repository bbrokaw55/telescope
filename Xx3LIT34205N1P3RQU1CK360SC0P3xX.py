

def startTelescope(eventList):
    DP = []  # vector<stack<time>> DP
    DP.append([])   # start event

    for i in range(len(eventList)):
        DP.append([])   #append empty list to make a 2d list
    path = telescope(0 ,0, eventList, DP)
    # path.pop()   # pop out the 0
    # for num in path:
        # print(DP[num])
    print(len(path))
    print(path)
    print(traceback(eventList, path))

def telescope(time, position, eventList, DP):

    if(len(DP[time]) != 0): return DP[time]
    PATH = []  # stack Path<time>;
    for eventTime in range(time+1,len(eventList)+1):
        eventPosition = eventList[eventTime-1]
        if time == 0 : eventPosition -= 1
        if (abs(position - eventPosition) <= eventTime-time):

            # if(len(DP[eventTime]) == 0) :
            telescope(eventTime, eventPosition, eventList, DP)
            if len(DP[eventTime]) > len(PATH):

                PATH = DP[eventTime].copy()
    DP[time] = PATH.copy()

    if (time != 0):  # start is not an event
        DP[time].append(time)
    print(DP)
    # print("DP at time: ", time, " --> ", DP[time])

    return DP[time]

def traceback(eventList, times):
    moves = "{" # init empty string
    cur_pos = 0
    time = 0  # initial position & time == 0

    while (len(times) != 0):
        eventTime = times.pop()
        eventPosition = eventList[eventTime - 1]
        while cur_pos < eventPosition:
            moves += "+1, "
            cur_pos += 1
            time += 1

        while cur_pos > eventPosition:
            moves += "-1, "
            cur_pos -= 1
            time += 1

        while (time != eventTime):
            moves += "0, "
            time += 1

    moves += "}"
    return(moves)

eventList =  [ 1,-4,-1, 4, 5, -4, 6, 7,-2]
eventList2 = [ 0, 0, 0, 4, 3, 3, 8, -1, 6, 8]

startTelescope(eventList)
