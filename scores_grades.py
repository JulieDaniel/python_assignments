def grades():
    import random
    for n in range(0, 10, 1):
        score = random.randint(60, 100)
        if (score >= 60) and (score <= 69):
            print "Your score is:", score, "Your grade is a D."
        elif (score >=70) and (score <= 79):
            print "Your score is:", score, "Your grade is a C."
        elif (score >=80) and (score<=89):
            print "Your score is:", score, "Your grade is a B."
        elif (score >=90) and (score<=100):
            print "Your score is:", score, "Your grade is an A."
        else:
            print "That's all the grades."

grades()