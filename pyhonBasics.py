x,y  = 1, 2
text1, text2 = "hagay", "Eli"

RandomList = ["item1", "item2",3,4,5]
del RandomList[4]

Dict = {"hagay":1, "Eli":2}

#tupels = list that cant be updated
tup = ('item3', 'item4')
"""
print ("Hello world %s %s %d %d" % (text1, text2, x, y))
print (RandomList)
print (Dict)

#conditional cases
if (5 > 3):
    print("true")
else:
    print("false")

for i in range(0,4,2): #go from 0 to 4 in jumps of 2
    for item in RandomList:
        print (item)
"""
try:
    while y < 1:
        break
except:
    print("error")

def Add(num1, num2): # function
    return (num1 + num2)
dir ("hello") # all the functions i can use on this data type

# eval / exec = runs a string as a python code
# conver between data types: str(1)= '1'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print(self.name)
    def getAge(self):
        print (self.age)

"""
hagay = Person ("hagay", 27)
hagay.getName()
hagay.getAge()
"""

class Parent(Person):
    def __init__(self, name, age, dad):
        super().__init__(name, age)
        self.dad = dad
    def whosYorDaddy(self):
        print(self.dad)

hagay = Parent ("hagay", 27, "ami")
hagay.getName()
hagay.getAge()
hagay.whosYorDaddy()