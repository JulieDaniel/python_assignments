li = ['magical unicorns',19,'hello',98.98,'world']
ns=""
intsum=0
floatsum=0
hasstr=0
hasint=0
hasfloat=0



for i in li:
    el=type(i)
    if el is str:
        ns=ns + " " +i
        hasstr=1
    if el is int:
        intsum+=i
        hasint=1
    if el is float:
        floatsum+=i
        hasfloat=1
print ns
print "intsum: " + str(intsum)
print "floatsum: " + str(floatsum)

if hasstr + hasint + hasfloat >1:
    print "This has mixed types."
elif hasstr:
    print "This list is only strings."
elif hasint:
    print "This list is only intgegers."
else:
    print "This list is only floats."




