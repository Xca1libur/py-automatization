# def number(a):
#     if a <= 0:
#         return "The number is not positive"
#     return "The number is positive"

# result = number(-5)
# print(f"For now i show u value of result: {result}") 

# def describe_pet(animal_type, *args):
#     print(f"I have two {animal_type}")

#     if len(args) == 2:
#         print(f"His name is {args[0]} and {args[1]} is a {animal_type}")
#     elif len(args) == 1:
#         print(f"His name is {args[0]} he is a {animal_type}")
#     else:
#         names = ""
#         for name in args:
#             if name == args[-1]: 
#                 names = names + "and " + name
#             else:
#                 names = names + name + ", "
#         print(f"His name are {names}")

#     describe_pet("cat", "Leva", "Nusha", "Liza", "Dora", "Marsik")
#     describe_pet("cat", "Leva")
#     describe_pet("cat", "Leva")
#     describe_pet("cat", "Leva", "Nusha", "Liza")


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

# def triangle_type(a, b, c):
#     if not (a + b > c and a + c > b and c + b > a):
#         return "not a triangle"
#     elif a == b and b == c:
#         return "equilateral"
#     elif a == b or a == c or c == b:
#         return "isosceles"
#     else:
#         return "scalene"

# print(triangle_type(9, 7, 6))


# def sum_only_even(limit):
#     num = 1
#     sum_even = 0

#     while num <= limit:
#         if num % 2 == 0:
#             sum_even = sum_even + num

#         num = num + 1

#     return sum_even

# print(sum_only_even(10))

# def is_prime(number):
#     if number < 2:
#         return False
    
#     divisors = True

#     for divisor in range(2, number):
#         if number % divisor == 0:
#             divisors = False
#             break
        
#     return divisors

# print(is_prime(15))



# def find_devisors(number):
#     devisors = []

#     for devisor in range(1, number + 1):
#         if number % devisor == 0:
#             devisors.append(devisor)

#     return devisors

# print(find_devisors(4050))

def find(number):
    spi = []

    for divisor in range(2, number + 1):
        while number % divisor == 0:
            spi.append(divisor)
            number = number // divisor
        
    return spi


def count(n):
    number = 1
    i = []

    while number < n:
        print(number)
        i.append(number)
        number += 1

    return i 

print(count(10))
