import random

characters_range = range(33, 127)
password = ''

while True:
    pass_length = int(input("How long should the password be? (Can not be shorter than 8 signs)"))
    if pass_length < 8:
        print("Sorry, password has to be at least 8 signs long.")
        continue
    else:
        break

for i in range(pass_length):
    password += chr(random.choice(characters_range))

print("Your password is: ", password)