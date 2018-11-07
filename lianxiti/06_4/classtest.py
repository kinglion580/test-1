#!/usr/bin/env python3

class UserData:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.id, self.name)

class NewUser(UserData):
    group = 'shiyanlou-louplus'

    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(id, name):
        return '{}\'s id is {}'.format(name, id)

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
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))
