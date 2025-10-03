import random

secret_num = []

#input("Press any key. ")
for num in range(3):
    secret_num.append(random.randrange(0, 10))

counter = secret_num.count(7)
if counter >= 2:
    print("Congratulations")
elif sum(num % 2 == 0 for num in secret_num) >= 3:
    print("Congratulations")
elif sum(num % 2 != 0 for num in secret_num) >= 3:
    print("Congratulations")

else:
    print("Try again! Better luck next time.")

print(secret_num)

