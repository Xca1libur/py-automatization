# def number(a):
#     if a <= 0:
#         return "The number is not positive"
#     return "The number is positive"

# result = number(-5)
# print(f"For now i show u value of result: {result}") 

def describe_pet(animal_type, *args):
    print(f"I have two {animal_type}")

    if len(args) == 2:
        print(f"His name is {args[0]} and {args[1]} is a {animal_type}")
    elif len(args) == 1:
        print(f"His name is {args[0]} and {args[0]} is a {animal_type}")
    else:
        names = ""
        for name in args:
            if name == args[-1]: 
                names = names + name
            else:
                names = names + name + " and "
        print(f"His name are {names}")

describe_pet("cat", "Leva", "Nusha", "Liza", "Dora", "Marsik")
# describe_pet("cat", "Leva", "Liza")
# describe_pet("cat", "Leva")
