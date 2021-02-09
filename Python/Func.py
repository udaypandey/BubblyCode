def say(message, times = 1):
    print(message * times)

say('Hello', 4)
say('World', 4)


def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3)
func(3, c=13)


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

a = maximum(2, 3) + 5
print(a)

