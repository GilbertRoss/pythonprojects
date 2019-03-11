import random
import string
import re
import time
alphabetLower = list(string.ascii_lowercase)
alphabetUpper = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)
boolean = True
print("Secure password generator\n")
while boolean:
    lowercaseword = ""
    uppercaseword = ""
    number = ""
    symbol = ""
    for x in range(1):
        uppercaseword = random.choice(alphabetUpper)
    for x in range(5):
        lowercaseword += random.choice(alphabetLower)
    for x in range(2):
        number += random.choice(digits)
    for x in range(1):
        symbol = random.choice(punctuation)
    pw = uppercaseword+lowercaseword+number+symbol
    pwToLowerCase = pw.lower()
    pwArray = list(pwToLowerCase)
    string = ""
    print("Here is your password:")
    print(pw)
    print("")
    print("This words will help you to remember your password:")
    with open('data.txt', 'r') as myfile:
        data=myfile.read().replace('\n', ' ')
        data = re.sub(r'[^\w\s]','',data)
        data = re.sub('\d', '%d', data)
    for i in pwArray:
        for x in data.split():
            if x.startswith(' '.join(i)):
                string += x + " "
                break
    print(string + " " + number + " " + symbol)
    print("")
    noAns = True
    time.sleep(2)
    while noAns:
          answer = input("Do you want to generate a new password? (y/n)")
          if answer == "y":
              noAns = False
          else:
              noAns = False
              boolean = False
print("")          
    
