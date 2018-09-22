"""
cryptography.py
Author: Andrew Chen
Credit: https://github.com/chenmasterandrew/Cryptography

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
def keymaster(keyindex, numkey):
    if keyindex > numkey:
        keyindex = 0
    return keyindex

def crypt(opt, message, key):
    nummessage = []
    numkey = []
    index = 0
    keyindex = 0
    output = ""
    for char in message:
        nummessage.append(associations.find(char))
    for char in key:
        numkey.append(associations.find(char))
    for x in range(0,len(nummessage)):
        
        keyindex = keymaster(keyindex, len(numkey)-1)
        if opt == "e":
            nummessage[index] += numkey[keyindex]
            if nummessage[index] > 84:
                nummessage[index] -= 85
        else:
            nummessage[index] -= numkey[keyindex]
        index += 1
        keyindex += 1
    for num in nummessage:
        output += associations[num]
    print (output)
    chooseopt()

def chooseopt():
    opt = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if opt == "e" or opt == "d":
        message = str(input("Message: "))
        key = str(input("Key: "))
        crypt(opt, message, key)
    elif opt == "q":
        print ("Goodbye!")
    else:
      print ("Did not understand command, try again.")
      chooseopt()
chooseopt()