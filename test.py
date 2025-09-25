""" x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values[6])
 """

""" answer1 = input("what's your name?")
input("hello")
answer4 = input("would you like to answer a quick servey? yes or no?")
correct_answers = ["yes", "ok","sure","okay"]
if answer4 in correct_answers:
    print("great!")
else:
    print("too bad you don't get a choice")

answer2 = input("what's your favorite ice cream flavor?")
if answer2 == "coffee":
    print("yes")
else:
    print("incorrect")    

answer3 = input("what is the worst flavor of ice cream?")
if answer3 == "coffee":
    print("you little liar everyone loves coffee. youre going to get tickled")
else:
    print("spared; congratulations. you have great taste.")

print("okay, next survey")
 """
""" answer5 = input("what's your name?")
answer6 = input("what's your favorite day of the week?")
if answer6 == "saturday" or answer6 == "Saturday":
    print("")
else:
    print("how does it feel to be wrong?")
answer7 = input("what's your favorite number?")
answer8 = input("what's your favorite animal?")

print(f"{answer5} was casually skipping down the streets, merry as ever on a fine {answer6}. Little did {answer5} know that they were going to get ambushed by a pack of rats. as they tried to shoo them away, {answer7} rats pounced on them and started breakdancing around her, seemingly beckoning them into their cult. Just as they thought all hope was lost, the {answer8} king appeared, summoning a gang of birds to excrete on the rats. Eventually, {answer5} left unscathed, but had ptsd from the {answer8}s and had to get therapy for their schizophrenia that made them hallucinate about becoming one witht the rats. Thus, inevitably, {answer5} now lives in the sewers and commands a rat army to pounce on other unsuspecting strangers, creating a loop of demise and terror.")
 """
""" def odd_or_even(x):
    if x % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
        x = any
odd_or_even(125)

hw = False

def movies():
    if not hw:
        print("movie time")
    else: 
        print("finish you work first you little microorganism")
    
movies() """

""" bill = int(input("how much was your bill?"))
values = ["great","good","okay","bad","horrendous"]
values = input("how was your meal? choose from the following: great, good, okay, bad, horrendous")
def total():
    if values == "great":
        print(bill * 1.25)
    if values == "good":
        print(bill * 1.20)
    if values == "okay":
        print(bill * 1.15)
    if values == "bad":
        print(bill)
    if values == "horrendous":
        print(bill * 0.9)
total() """

""" factors = int(input("give me a whole number"))
def number(x):
    list = []
    for i in range(1, x + 1):
        if x % i == 0:
            list.append(i)
    return(list)

print(number(factors))

gcf = int(input("give me two whole numbers, one at a time"))
def common(x):
    list = []
    for i in range(1, x + 1):
        if x % i == 0:
            list.append(i)
    return(list)
def common(y):
    list = []
    for i in range(1, y + 1):
        if y % i == 0:
            list.append(i)
    return(list)
print(common(gcf)) """

""" x = input("what do you want to buy (y/n)")
while x != "n":
    item = input("what dy want to buy")
print("thank you for your purchase")
 """

gcf = int(input("give me one whole number"))
gcf2 = int(input("give me another whole number"))
def common(x,y):
    list = []
    for i in range(1,x):
        if x % i == 0 and y % i == 0:
            list.append(i)    
    return(list)
print(common(gcf,gcf2))
