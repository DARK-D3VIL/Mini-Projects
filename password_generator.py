import string
import random
from typing_extensions import Self
LengthOfPassword = int(input("how many characters do you want in your password?\n"))
letter_length = random.randint(0,LengthOfPassword)
number_length = LengthOfPassword - letter_length
Random_letters = "".join(random.choice(string.ascii_letters)for i in range (letter_length))
Random_numbers = "".join(random.choice(string.digits)for i in range (number_length))
Random_string = Random_letters + Random_numbers
print(Random_string)
