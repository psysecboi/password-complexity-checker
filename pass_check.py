import string

# taking user input
password = input("Password: ")


# checking diversity of character types
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special_char = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special_char, digits]
length = len(password)

score = 0

# using a common wordlist to scan presence of password
with open("common.txt", "r") as f:
    common = f.read().splitlines()

if password in common:
    print("Your password was found in a common list.\n Score: 0/7 ")
    exit()

# evaluating password by length
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 16:
    score += 1
if length > 20:
    score += 1
print(f"the length of your password is {length};(Adding {str(score)} points to the score)")

# evaluating password by diversity of type of characters
if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1
print(f"Your password has {str(sum(characters))} different character types;(Adding {str(sum(characters)-1)} points to the score)")

# calculating final score
if score < 4:
    print(f"Overall password complexity is very weak!\nScore: {str(score)}/7")
elif score == 4:
    print(f"Overall password complexity is good!\nScore: {str(score)}/7")
elif score > 4 and score <= 6:
    print(f"Overall password complexity is strong!\nScore: {str(score)}/7")
elif score > 6:
    print(f"Overall password complexity is very strong!\nScore: {str(score)}/7")
