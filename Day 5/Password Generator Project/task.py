import string
import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

dictionary=string.digits+string.ascii_letters+string.punctuation
password_total_length = nr_letters + nr_symbols + nr_numbers

pass1="".join(random.choice(string.digits)for _ in range(nr_numbers))
pass2="".join(random.choice(string.ascii_letters)for _ in range(nr_letters))
pass3="".join(random.choice(string.punctuation)for _ in range(nr_symbols))

pass_gen = list(pass1 + pass2 + pass3)

random.shuffle(pass_gen)
print("Your generated password is: "+ "".join(pass_gen))
