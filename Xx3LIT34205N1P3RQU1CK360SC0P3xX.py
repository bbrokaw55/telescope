def startTelescope(eventList[])
    vector<stack<time>> DP
    DP.at(0) = null
    For i in range eventlist
        DP.append(new stack<time>)
    Path = telescope(0,0, eventList[], DP)
    return (path.size, path, traceback(path, eventList[])

def telescope(time, position, eventList[], DP<stack<time>>)
    stack Path<time>;
    For i in range time+1:size(eventList)
        If (abs(position) - abs(eventPos) <= eventTime-time):
            telescope(i, event.position, eventList[])
            If DP.at(i).size > path.size
            Path = DP.at(i)
    If (time != 0) { // start is not an event
        DP.at(time) = path
        DP.at(time).push(time)

def traceback(eventList[], times/*stack of positions visited in order*/)
    String moves = “”
    Int cur_pos
    Int time = 0
    While !times.empty
        While cur_pos < eventList[times.top]
            moves.append(+1)
            Cur_pos += 1
            Time += 1
        While cur_pos > eventList[times.top]
            moves.append(-1)
            Cur_pos -= 1
        While time != times.top
            moves.append(0)
            Time += 1
        Times.pop()
    return moves
