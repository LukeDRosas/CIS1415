#Luke Doughty-Rosas

# Variables
menuOpt = ''
jList = []
teamRoster = {}
players = 0
count = 1
menuPrompt = '''MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit

Choose an option:\n'''

# Player input
while players < 5:
    jersey = int(input("Enter player %d's jersey number:\n" % count))
    rating = int(input("Enter player %d's rating:\n" % count))
    print('')
    count += 1
    players += 1

    teamRoster.update({jersey: rating})
    jList.append(jersey)

#Player output(sorted)
jList.sort()
print('ROSTER')
for jersey in jList:
    print('Jersey number: %d, Rating: %d' % (jersey, teamRoster[jersey]))

#Menu
print('')
while menuOpt != 'q':
    menuOpt = input(menuPrompt)
    menuOpt.lower()
    if menuOpt == 'a':
        jersey = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))

        teamRoster.update({jersey: rating})
        jList.append(jersey)

        print('')
    elif menuOpt == 'd':
        deleteJ = int(input('Enter a jersey number:\n'))
        jList.remove(deleteJ)
        teamRoster.pop(deleteJ)
        
    elif menuOpt == 'u':
        jersey = int(input("Enter a jersey number:\n"))
        rating = int(input("Enter a new rating for player:\n"))

        teamRoster.update({jersey: rating})
        
    elif menuOpt == 'r':
        aboveR = int(input('Enter a rating:\n'))
        print('\nABOVE %d' % aboveR)
        for jersey in jList:
            if teamRoster[jersey] > aboveR:
                print('Jersey number: %d, Rating: %d' % (jersey, teamRoster[jersey]))
        print('')
        
    elif menuOpt == 'o':
        jList.sort()
        print('ROSTER')
        for jersey in jList:
            print('Jersey number: %d, Rating: %d' % (jersey, teamRoster[jersey]))
        print('')


