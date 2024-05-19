###################### Is it a triangle? ######################
def triangleTest(a, b, c) -> bool:
    smallSides = [a, b, c]; smallSides.remove(max(a,b,c))
    return sum(smallSides) > max(a,b,c)

###################### Greetings ######################
def greet(hour: int, name: str) -> None:
    if 0 <= hour <= 12:
        print("Good morning,", name)
    elif 13 <= hour <= 17:
        print("Good afternoon,", name)
    elif 18 <= hour <= 23:
        print("Good evening,", name)

name = input("What is your name?\n>> ")
hour = int(input("What time is it?\n>> ").split(":")[0])
greet(hour, name)

###################### Even Numbers ######################
numlist = [1,2,3,4,5,6,7,8,9]

def getEven(numlist: list) -> list:
    return [item for item in numlist if item % 2 == 0]

print(getEven(numlist))
