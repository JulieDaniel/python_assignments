#draw number of stars for number in list.
def draw_stars():
    a = [4, 6, 1, 3, 5, 7, 25]

    for n in a:
        print ("*")*n

draw_stars()

#part two. Draw stars, or first lowercase letter of string, as many times as characters are in string, within the list.
def draw_starsplus():
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


    for n in x:
        if type(n) is int:
            print ("*")*n
        elif type(n) is str:
            newstr=""
            for i in range(0, len(n)):
                newstr+=(n[0]).lower();
            print newstr

draw_starsplus()
