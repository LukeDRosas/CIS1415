#Luke Doughty-Rosas

tasks = []
prompt = ''
menuPrompt = '''Daily tasks
a - add task
c - completed task
f - amend task
l - list tasks
q - quit

Make a selection
'''
i = 0

while prompt != 'q':
    prompt = input(menuPrompt)
    if prompt == 'a':
        task = (input('Enter a new task:\n'))
        tasks.append(task)
        i += 1
        print('Current tasks:\n', tasks)
    elif prompt == 'c':
        complete = int(input('Completed task to remove? (1 - %d)\n' % i)) - 1
        tasks.pop(complete)
        i -= 1
        print('Current tasks:\n', tasks)
    elif prompt == 'f':
        fix = int(input('Task to amend? (1 - %d)\n' % i)) - 1
        task = (input('Amend:\n'))
        tasks.pop(fix)
        tasks.insert((fix), task)
        print('Current tasks:\n', tasks)
    elif prompt == 'l':
        print('Current tasks:\n', tasks)

