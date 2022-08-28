import random


print("Generate a password")

alphalower = 'abcdefghijklmnopqrstuvwxyz'
alphaupper = alphalower.upper()
spchar = '~!@#$%^&*()_+=-{}[],./?|'
nums = '123456789'
chars = alphalower + alphaupper + nums + spchar

# print(chars)

length = int(input('Length of characters to generate password: '))
password = ''

for pwd in range(length):
    password += random.choice(chars)

print(password)
