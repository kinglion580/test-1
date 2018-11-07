import copy

def compute(base, value):
    base = copy.copy(base)
    base.append(value)
    result = sum(base)
    print(result)

if __name__ == '__main__':
    testlist = [10, 20, 30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)
