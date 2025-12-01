def fun2(*args, **kwargs):
    print(args)
    print(kwargs)

fun2(1, 2, 3, 4, 5, id=101, name='ABC')