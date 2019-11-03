import random

def startTelescope(eventList):
    DP = []  # vector<stack<time>> DP
    DP.append([])   # start event
    for i in range(len(eventList)):
        DP.append([])   #append empty list to make a 2d list
    path = telescope(0 ,0, eventList, DP) # Call on inital position and time

    # print out results
    print("Maximum Observable Events: ", len(path))
    print("Events Seen: ", path)
    print("Path", traceback(eventList, path))

    return path

def telescope(time, position, eventList, DP):

    PATH = []  # stack Path<time>;

    # loop through all following events
    for eventTime in range(time+1,len(eventList)+1):
        eventPosition = eventList[eventTime-1] # time-1 to match array position
        if time == 0 : eventPosition -= 1       # to account for observing the event

        reachable = abs(position - eventPosition) <= eventTime-time
        n_reachable = abs(eventPosition - eventList[-1]) <= len(eventList) - eventTime

        if (reachable and n_reachable): # if reachable

            if (len(DP[eventTime]) == 0):   # only call telescope if that event is unvisited
                telescope(eventTime, eventPosition, eventList, DP)

            if (len(DP[eventTime]) > len(PATH)):  # if the best path so far
                PATH = DP[eventTime].copy()     # copy to temp PATH holder

    DP[time] = PATH.copy() #copy best path into DP array
    if (time != 0):             # start is not an event
        DP[time].append(time)   # so we do not add to DP

    return DP[time] # return the best path

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
eventList3 = [random.randint(-10,10) for i in range(100)]
startTelescope(eventList2)
