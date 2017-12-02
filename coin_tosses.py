def cointoss():
    headcount = 0
    tailcount = 0
    import random
    for n in range(0, 5001, 1):
        toss = random.randint(1, 2)

        if toss==1:
            headcount+=1
            print "Attempt number:", n, "It's heads.", "So far there are", headcount, "heads."
        else:
            tailcount+=1
            print "Attempt number:", n, "It's tails.", "So far there are", tailcount, "tails."


cointoss()