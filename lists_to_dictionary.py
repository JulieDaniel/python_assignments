name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    for n in range(0, len(list1)):
        new_dict[list1[n]]=list2[n]
    return new_dict
print (make_dict(name, favorite_animal))