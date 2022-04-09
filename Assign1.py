print(7**4)

s="Hi there Sam!"
l=s.split()
l[-1]="dad!"
print(l)

planet="Earth"
diameter=12742
print("The diameter of {} is {} kilometers".format(planet,diameter))

lst=[1,2,[3,4],[5,[100,200,["hello"]],23,11],1,7]
print(lst[3][1][2][0])

d={'k1':[1,2,3,{'tricky':['oh', 'man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

print("Tuples are immutable and values can't be alttered within it and Lists are mutable")

def domain(a):
    return a.split("@")[-1]
print(domain("user@domain.com"))

def fun(a):
    return True if "dog" in a else False
print(fun("dog"))

def fun(a):
    return a.count("dog")
print(fun("dot"))

def ticket(speed,bod):
    if bod:
        speed-=5
    if speed>80:
        return "Big Ticket"
    elif speed>60:
        return "Small Ticket"
    else:
        return "No Ticket"
print(ticket(70,True))
print(ticket(90,False))