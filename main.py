import string
import random

#Generate from different character types
chartype1 = list(string.ascii_lowercase)
chartype2 = list(string.ascii_uppercase)
chartype3 = list(string.digits)
chartype4 = list(string.punctuation)

userinput = input("State number of characters for your password: ")

#As long as user asks to generate 8 characters
while True:
    try:
        charNo = int(userinput)
        if charNo < 8:
            print("Number should be at least 8")
            userinput = input("Please enter again: ")
        else:
            break
    except:
        print("Enter numbers only.")
        userinput = input ("State number of characters for your password: ")

random.shuffle(chartype1)
random.shuffle(chartype2)
random.shuffle(chartype3)
random.shuffle(chartype4)

#Set up for generating various characters
chunk1 = round(charNo * (30/100))
chunk2 = round(charNo * (20/100))

result = []

for x in range(chunk1):
    result.append(chartype1[x])
    result.append(chartype2[x])

for x in range(chunk2):
    result.append(chartype3[x])
    result.append(chartype4[x])

#Shuffle and print
random.shuffle(result)

password = "".join(result)
print("Password: ", password)