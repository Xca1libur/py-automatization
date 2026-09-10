# def number(a):
#     if a <= 0:
#         return "The number is not positive"
#     return "The number is positive"

# result = number(-5)
# print(f"For now i show u value of result: {result}") 

# def describe_pet(animal_type, *args):
    # print(f"I have two {animal_type}")

    # if len(args) == 2:
    #     print(f"His name is {args[0]} and {args[1]} is a {animal_type}")
    # elif len(args) == 1:
    #     print(f"His name is {args[0]} he is a {animal_type}")
    # else:
    #     names = ""
    #     for name in args:
    #         if name == args[-1]: 
    #             names = names + "and " + name
    #         else:
    #             names = names + name + ", "
    #     print(f"His name are {names}")

    # describe_pet("cat", "Leva", "Nusha", "Liza", "Dora", "Marsik")
    # describe_pet("cat", "Leva")
    # describe_pet("cat", "Leva")
    # describe_pet("cat", "Leva", "Nusha", "Liza")


# def check_number(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"

# result = check_number(123123124351421321)

# if result == "Positive":
#         print(f"The number is Positive")

# print(result)

# def analyze_number(number):
#     if number > 0 and number % 2 == 0:
#         return "positive even"
#     elif number > 0 and number % 2 !=0:
#         return "positive odd"
#     elif number < 0 and number % 2 == 0:
#         return "negative even"
#     elif number < 0 and number % 2 != 0:
#         return "negative odd"
#     else:
#         return "zero"


# print(analyze_number(8))
# print(analyze_number(7))
# print(analyze_number(-4))
# print(analyze_number(-5))
# print(analyze_number(0))

def triangle_type(a, b, c):
    if not (a + b > c and a + c > b and c + b > a):
        return "not a triangle"
    elif a == b and b == c:
        return "equilateral"
    elif a == b or a == c or c == b:
        return "isosceles"
    else:
        return "scalene"

print(triangle_type(9, 7, 6))