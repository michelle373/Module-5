# Michelle Patlan
# 8/13/2022
#Use random.choice to select a day of the week from a list and print that day.
import random

day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# get a random day and assign it to a variable
random_day = random.choice(day_list)

# printing random day
print("Random day is " + str(random_day))