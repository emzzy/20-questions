
def concatenate_string():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    year_of_birth = 2025 - age

    print(f"Welcome, {first_name} {last_name} born ({year_of_birth}).")
    gender = input("What is your gender?\nEnter Male/Female or Other: ").lower()

    if gender == 'male':
        role = 'son'
    elif gender == 'female':
        role = 'daughter'
    print(f"Welcome, {first_name} {role} of {last_name} {year_of_birth}.")

concatenate_string()