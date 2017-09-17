# 3! = 3 * 2 * 1

def factorial(num):

    if num <= 1:
        return 1
    else:
        result = num * factorial(num-1)
        return result


print "4! =", factorial(4)

# 1st time that factorial is called the result = 4 * factorial(3)
# 2nd result = 3 * factorial(2)
# 3rd result = 2 * factorial(1)
# Then it runs back with 2*1, 3*2, 4*6 = 24


