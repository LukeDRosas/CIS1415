#Luke Doughty-Rosas

def encrypt(userString):
    encryptionD = {
        'A': '0', 'B': '9', 'C': '8',
        'D': '7', 'E': '6', 'F': '5',
        'G': '4', 'H': '3', 'I': '2',
        'J': '1', 'K': '@', 'L': '#',
        'M': '$', 'N': '^', 'O': '&',
        'P': '*', 'Q': '%', 'R': '(',
        'S': ')', 'T': 'A', 'U': 'Z',
        'V': 'B', 'W': 'Y', 'X': 'K',
        'Y': 'F', 'Z': 'P', 'a': 'l',
        'b': 'm', 'c': 'n', 'd': 'o',
        'e': 'p', 'f': 'q', 'g': 'r',
        'h': 's', 'i': 't', 'j': 'u',
        'k': 'v', 'l': 'k', 'm': 'j',
        'n': 'i', 'o': 'h', 'p': 'g',
        'q': 'f', 'r': 'e', 's': 'd',
        't': 'c', 'u': 'b', 'v': 'a',
        'w': 'y', 'x': 'z', 'y': 'w',
        'z': 'x'}
    encrypted = []
    encrypted = list(userString)
    i = 0
    for each in encrypted:
        if each in encryptionD:
            encrypted[i] = encryptionD[each]
            
        i += 1
    encryptedF = ''.join(encrypted)
    print(encryptedF)

def unencrypt(userString):
    encryptionD = {
        'A': '0', 'B': '9', 'C': '8',
        'D': '7', 'E': '6', 'F': '5',
        'G': '4', 'H': '3', 'I': '2',
        'J': '1', 'K': '@', 'L': '#',
        'M': '$', 'N': '^', 'O': '&',
        'P': '*', 'Q': '%', 'R': '(',
        'S': ')', 'T': 'A', 'U': 'Z',
        'V': 'B', 'W': 'Y', 'X': 'K',
        'Y': 'F', 'Z': 'P', 'a': 'l',
        'b': 'm', 'c': 'n', 'd': 'o',
        'e': 'p', 'f': 'q', 'g': 'r',
        'h': 's', 'i': 't', 'j': 'u',
        'k': 'v', 'l': 'k', 'm': 'j',
        'n': 'i', 'o': 'h', 'p': 'g',
        'q': 'f', 'r': 'e', 's': 'd',
        't': 'c', 'u': 'b', 'v': 'a',
        'w': 'y', 'x': 'z', 'y': 'w',
        'z': 'x'}
    unencryptionD = dict((v,k) for k,v in encryptionD.items())
    unencrypt = []
    unencrypt = list(userString)
    i = 0
    for each in unencrypt:
        if each in unencryptionD:
            unencrypt[i] = unencryptionD[each]
 
        i += 1
    unencryptedF = ''.join(unencrypt)
   
    print(unencryptedF)
        

userString = encrypt(input('Enter string to encrypt:\n'))
userString = unencrypt(input('Enter string to unencrypt:\n'))
