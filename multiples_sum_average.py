#iterate through 1 to 1000 by 2s to print odds.
x =0
for x in range(1, 1000, 2):
    print x

#iterate through 5 to 1,000,000 by 5s.
x=5
for x in range(5, 1000001, 5):
    print x


#goes through list and creates sum by adding all items.
a = [1, 2, 5, 10, 255, 3]
sum=0
for n in a:
    sum += n
    print sum
#creates average of list
    avg=sum/len(a)
    print avg

