def get_message(inp):
    a, e = '', ''
    for y1 in hello:
        if inp.lower() == y1:
            a = "Hello! :) \nTry Rock paper scisors \nAsk the date or time\nSay toss to do a toss"
            break
    for y2 in bye:
        if inp.lower() == y2:
            a = "Bye"
            break
    for y3 in HAU:
        if inp.lower() == y3:
            a = "I'm fine, What about you?"
            break
    for y4 in time:
        if inp.lower() == y4:
            k = str(datetime.time(datetime.now()))
            a = "The time is " + k
            break
    for y5 in date:
        if inp.lower() == y5:
            k = str(datetime.date(datetime.now()))
            a = "The date is " + k
            break
    for y6 in RPS:
        if inp.lower() == y6:
            bm = random.choice(RPS)
            a = bm
            if (((inp.lower() == 'rock') and bm == 'scissor') or (inp.lower() == 'paper' and bm == 'rock') or (
                    inp.lower() == 'scissor' and bm == 'paper')):
                a = bm + ',' + "You win"
            elif inp.lower() == bm:
                a = bm + ',' + "It's a tie!"
            else:
                a = bm + ',' + "I win"
            break

    for y6 in toss:
        if inp.lower() == y6:
            bm = random.choice(TOSS)
            a = bm
            break
        for y in info:
            if inp.lower() == y:
                a = "Chat Bot Test is an expertimental chat bot deployed on Facebook Messenger by Siddhant Saoji \nThis bot is currently in devlpoment phase"
                break

    if a == '':
        e = "Sorry this is not supported yet"
    ans = a + e
    print(ans)
    return ans
