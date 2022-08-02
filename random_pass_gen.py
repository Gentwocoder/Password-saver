import random as rd

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
special_char = "@#$%&*_"
all_pass = list(caps + small + nums + special_char)


def pass_gen(length_of_password):
    rd.shuffle(all_pass)
    password = []
    for i in range(length_of_password):
        password.append(rd.choice(all_pass))

    rd.shuffle(password)

    return "".join(password)


# while True:
#     # length_of_password = int(input("Enter length of password: "))
#     pass_gen(length_of_password)
#
#     if length_of_password == 0:
#         print("Password length cannot be '0'")
#         break
