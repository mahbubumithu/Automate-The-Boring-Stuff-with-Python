while True:
    print('Who are you')
    name = input()
    if name != 'Mithu':
        continue
    print('Hello Mithu. What is your password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')