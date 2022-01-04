import datetime
def gettime():
    return datetime.datetime.now()

"""Log Start here"""
def l(name):
    c=int(input(f"you chose to log data for {name} ,Please choose 1 for health and 2 for diet: "))
    if c==1:
        health(name)
    else:
        diet(name)

def health(name):
    with open(f"{name}Health.txt",'a') as f:
        f.write(str(str(gettime()))+':'+str(input(f"Please log health data for {name} here :")+"\n"))

def diet(name):
    with open(f"{name}Diet.txt",'a') as fd:
        fd.write(str(str(gettime()))+':'+str(input(f"Please log Diet data for {name} here :")+"\n"))

"""Log end here"""


"""get start here"""
def health2(name):
    print(f" Health Data of {name}")
    with open(f"{name}Health.txt") as f:
        content = f.read()
        print(content)

def diet2(name):
    print(f" Diet Data of {name}")
    with open(f"{name}Diet.txt") as fd:
        content=fd.read()
        print(content)

def g(name):
    c = int(input(f"you chose to retrieve data for {name} ,Please choose 1 for health and 2 for diet: "))
    if c == 1:
        health2(name)
    else:
        diet2(name)


"""get end here"""


"""Main starting from Here"""

what=int(input('For Log 1 for Retrieve 2 :'))
if what ==1:
    name1=int(input('You chose to log data, Enter 1 for Zeba 2 for Sherry 3 for Ram: '))
    name= "Zeba" if name1 == 1 else "Sherry" if name1 == 2 else "Ram"
    l(name)
else:
    name1 = int(input('You chose to retrieve data, Enter 1 for Zeba 2 for Sherry 3 for Ram: '))
    name = "Zeba" if name1 == 1 else "Sherry" if name1 == 2 else "Ram"
    g(name)