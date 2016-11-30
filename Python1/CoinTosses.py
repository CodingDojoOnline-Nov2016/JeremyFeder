# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
def coin_toss ():
    heads = 0
    tails = 0
    for attempt in range (1, 5000+1):
        import random
        random_num = random.random()
        rounded_num = round(random_num)
        if rounded_num == 1:
            heads += 1
            print "Attempt #", attempt, ":", "  Throwing a coin... It's a head! ... Got ", heads, "head(s) so far and ", tails, "tail(s) so far."
            attempt += 1
        else:
            tails += 1
            print "Attempt #", attempt, ":", "  Throwing a coin... It's a tail! ... Got ", heads, "head(s) so far and ", tails, "tail(s) so far."
            attempt += 1
coin_toss()

# Yeah!!!  That works, SOLID =)
