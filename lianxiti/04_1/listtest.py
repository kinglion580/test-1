import sys

mo, le = [], []
for i in sys.argv[1:]:
    if len(i) > 3:
        mo.append(i)
    else:
        le.append(i)

if le:
    print(' '.join(le))
if mo:
    print(' '.join(mo))
