age = input()

# Calculating the number of weeks left to live 
total_weeks = 52 * 90
age_in_weeks = int(age) * 52
weeks_left = total_weeks - age_in_weeks


print(f"You have {weeks_left} weeks left.")
