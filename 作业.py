# def ran(rows):
#     if rows % 2 == 0:
#         print("行数一定是奇数!")
#     for i in range(1, (rows + 1) // 2 + 1):
#         for l in range((rows + 1) // 2 - i):
#             print(" ", end="")
#         for k in range(1, i * 2):
#             print("*", end="")
#         print("\n")

#     for m in range((rows - 1) // 2, 0, -1):
#         for n in range((rows + 1) // 2 - m):
#             print(" ", end="")
#         for x in range(1, m * 2):
#             print("*", end="")
#         print("\n")
# ran(5)

sum_t = 0
for i in range(1, 1001):
    if i == 1:
        continue
    number_special = 1
    for m in range(2, int(i * 0.5) + 1):
        if i % m == 0:
            number_special += m
    if number_special == i:
        sum_t += i
print(sum_t)
                        





    

