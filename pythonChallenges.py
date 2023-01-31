# def first_function():
#     pass
# result = first_function()
# print(result)


# 1 calculator 
def add(*args):
    result = 0
    for num in args: 
        result += num
    print(result)

def sub(a,b):
    return a - b
def compute(a,b,op):
    return op(a,b)

userInput = input("What calculation would you like to do? ({add}, {sub}, mult, div)")
# if userInput == "add":
#     break
# 2 reverse string

# 3 bank transaction

# 4 sort a string

#5 print contacts

#6 print contacts 