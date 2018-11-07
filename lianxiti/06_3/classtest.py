#!/usr/bin/env python3

class UserData:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.id, self.name)

class NewUser(UserData):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        if len(n) < 4:
            print('ERROR')
        else:
            self._name = n

    def __repr__(self):
        return '{}\'s id is {}'.format(self._name, self.id)

if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)
