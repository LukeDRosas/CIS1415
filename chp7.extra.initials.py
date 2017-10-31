#Luke Dought-ROsas

fullName = input('Enter your full name:')
initials = []
count = 0

fullName = fullName.split()
for name in fullName:
    name = name[0]
    initials.append(name)

print('%s. %s. %s.' % (initials[0], initials[1], initials[2]))
