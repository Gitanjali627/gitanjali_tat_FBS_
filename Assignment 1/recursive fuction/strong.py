def fact(num):
    if(num == 0):
        return 1
    else:
        return num * fact(num - 1)

def strong(num):
    if(num <= 0):
        return 0
    else:
        d = num % 10
        f = fact(d)
        return f + strong(num // 10)

def chkStrong(num):
    if(num == strong(num)):
        return f'{num} is a strong number.'
    else:
        return f'{num} is not strong number.'

num = 145
print(strong(num))
