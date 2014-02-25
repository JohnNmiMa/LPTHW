class B:
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B, C, D]:
    try:
        raise c()
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"
print'*'*10
for c in [B, C, D]:
    try:
        raise c()
    except B:
        print "B"
    except D:
        print "D"
    except C:
        print "C"
