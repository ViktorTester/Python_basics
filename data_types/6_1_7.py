dog_age = float(input())
human_years = 0
if 0 < dog_age <=2:
    human_years = dog_age * 10.5
elif dog_age > 2:
    human_years = dog_age * 4 + 13
print(human_years)

# The program displays the dog's age in human years.
# For the first two years, a dog year is 10.5 human years.
# After that, each year of the dog is equal to 4 human years.