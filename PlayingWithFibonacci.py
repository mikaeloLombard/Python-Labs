## Playing with Fibonacci
# 1, 1, 2, 3, 5, 8, 13
# Fn = Fn-1 + Fn-2
# Where F0-1 + Fn-2

def FiboNum (Fn):

    if Fn == 0:
        return 0

    elif Fn == 1:
        return 1
    else:
        result = FiboNum(Fn-1) + FiboNum(Fn-2)
        return result

print FiboNum(3)

print FiboNum(4)

print FiboNum(5)

print FiboNum(16)







