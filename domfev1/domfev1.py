#####################1
def mu_1():
    return "“Don't compare yourself with anyone in this world…\n if you do so, you are insulting yourself.“ \n\t\t\t\t\t\t\t                 Bill Gates"
print(mu_1())

################2 четные

# def mu_2(a, b):
#
#     print(f"между числами {a} и {b}, содержатся следующие нечетные числа ")
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             print(i, end=" ")
#
# mu_2(1, 10)
#
# num = int(input("enter num"))
#
# num_1 = int(input("enter num"))
#
# mu_2(num, num_1)

#########################3

# def mu_3(chis, simv, pravda):
#    for i in range(chis):
#        for j in range(chis):
#            if pravda or i == 0 or j == 0 or i == chis - 1 or j == chis - 1:
#                print(simv, end=' ')
#            else:
#                print(' ', end=' ')
#        print()
# mu_3(10, '#', True)
# mu_3(10, '#', False)

#######################4

# def as_4(a, b, c, d, e):
#     return min(a, b, c, d, e)
# print (as_4(1, 5, 7, 8, 0))

#################5

# def mu_5():
#
#     a = int(input("первое значение"))
#     b = int(input("второе значение"))
#     prois1 = 1
#     for i in range(a, b + 1):
#         prois1 *= i
#     for j in range(b, a + 1):
#         prois1 *= j
#     return prois1
# print(mu_5())

###############6
# def mu_6():
#     a = int(input("количество чисел: "))
#     c = 0
#     while a != 0:
#         c += 1
#         a //= 10
#     return c
# print(mu_6())

#################7
def mu_7():
    a = int(input("является ли число палиндром: "))
    num1 = str(a)
    return num1 == num1[::-1]
print(mu_7())
