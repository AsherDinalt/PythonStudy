def test(a,b,c):
    print('a={} b={} c={}'.format(a,b,c))

def test_return(a,b):
    return a+b, a-b, a*b, a/b

def maker(n):
    def act(x):
        return x**n
    return act

def maker1(n):
    return lambda x: x**n

# (x,y,z) = (12.5, [3,4],"LOL")
# test(x,y,z)

my_list = test_return(4,2)
_, *my_list = test_return(8,2)
x, *my_list = test_return(16,4)

# my_fun = maker(3)
# print(my_fun(2))
# print(my_fun(3))
# print(my_fun(5))

# my_fun = maker1(4)
# print(my_fun(2))
# print(my_fun(3))
# print(my_fun(5))

def my_sum(*a):
    s = 0
    for i in a:
        s+=i
    return s

print(my_sum(1,2,3,4,5))