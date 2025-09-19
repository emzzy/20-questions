import random

random_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
secret_num = []
for x in range(3):
    secret_num.append(random.randint(0, 9))
print(secret_num)
if 7 in secret_num:
    print("Congratulations")
else:
    print("Try again! Better luck next time.")

#user_action = input("Press any key ")

#print(random.sample(random_numbers, 3))