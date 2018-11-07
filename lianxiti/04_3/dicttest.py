import sys

for i in sys.argv[1:]:
    print('ID:{} Name:{}'.format(*i.split(':')))
