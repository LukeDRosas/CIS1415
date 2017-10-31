#Luke Doughty-Rosas

digits = 0
i = 0

while digits != 12:
    userNumber = input('Enter 10 digit number with XXX-XXX-XXXX format:')
    digits = len(userNumber)

userNumber = userNumber.lower()

for i in ['a','b','c']:
    if i in userNumber:
        userNumber = userNumber.replace(i,'2')
for i in ['d','e','f']:
    if i in userNumber:
        userNumber = userNumber.replace(i,'3')
for i in ['g','h','i']:
    if i in userNumber:
        userNumber = userNumber.replace(i,'4')
for i in ['j','k','l']:
    if i in userNumber:
        userNumber = userNumber.replace(i,'5')
for i in ['m','n','o']:
    if i in userNumber:
        userNumber = userNumber.replace(i,'6')
for i in ['p','q','r','s']:
    if i in userNumber:
        userNumber = userNumber.replace(i,'7')
for i in ['t','u','v']:
    if i in userNumber:
        userNumber = userNumber.replace(i,'8')
for i in ['w','x','y','z']:
    if i in userNumber:
        userNumber = userNumber.replace(i,'9')

print(userNumber)
    


