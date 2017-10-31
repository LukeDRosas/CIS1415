#Luke Doughty-Rosas

def vowelCount(userString):
    i = 0
    userString = userString.lower()
    
    for each in ['a','e','i','o','u']:
        if each in userString:
           i += userString.count(each)
    return int(i)
    
def conCount(userString):
    i = 0
    userString = userString.lower()
    
    for each in ['b','c','d','f','g','h','j',
                 'k','l','m','n','p','q','r',
                 's','t','v','w','x','y','z'
                 ]:
        if each in userString:
            i += userString.count(each)
    return int(i)


userString = input('Enter a sentence:')

vowels = vowelCount(userString)
consonant = conCount(userString)

print('The number of vowels is:', vowels)
print('The number of consonants is:', consonant) 
