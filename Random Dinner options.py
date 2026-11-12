import random


def choose_dinner_option(dinner_options: list) -> str:

    return random.choice(dinner_options)
    #  Write code here
    pass


dinner_options = ["Steak", "Fish", "Soup", "Lamb"]


dinner_options = random.choice(dinner_options)
print(f"Your dinner is: {dinner_options} /n")