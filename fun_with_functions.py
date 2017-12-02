def odd_even():

    for n in range (1, 2001):
        count = 0;
        if n%2==0:
            print "The number is",n, "This is an even number."
        else:
            print "The number is", n, "This is an odd number."
odd_even()



def multiply(a,b):

    new=[]
    for n in a:

        new.append(n*b)
    return new

multiply([2, 4, 10, 16],5)
print (multiply([2, 4, 10, 16],5))

print (multiply([2,4,5],3))


def challenge(func, first, second):
    answer = []
    multiplied=func(first,second)
    for val in multiplied:
        ones=[]
        for n in range(0, val):
            ones.append(1)
        answer.append(ones)
    return(answer)

print (challenge(multiply, [2,4,5],3))
