#ECommerce System
""" 
It consists of two sides(traders, customers), traders must log in to do actions
Main functions:
- Log in
- Display products
    - One by one
    - As list

For customers:
- Shopping bag
- Buy product

For traders:
- Create product
- Update product

"""

from user import User, Trader, users
from res import *

user = None

while user is None:
    option = input(
        '''
        What do want?
        [1] Login
        [2] Register
        [2] Info
        :''')
    if option is '1':
        username = input('Enter username: ')
        for loopUser in users:
            if loopUser.username == username:
                user = loopUser
        if user is None:
            print(p('There is no such user :( Try again'))
    if option is '2':
        #Register user by saving info to data.json
        username = input(p('Enter username: '))
        newUser = User()
            
print(p(f'Welcome {user.username}!'))

userOption = input(p(
    f'''
    What do you want me to do?
    [1] Display products
    [2] Display shopping bag
    [3] Display your account
    '''))

if(userOption is '1'):
    pass
elif(userOption is '2'):
    pass
elif(userOption is '3'):
    print(p(
            f'''
            Username: {user.username}
            UserID: {user.id}
            '''
        ))