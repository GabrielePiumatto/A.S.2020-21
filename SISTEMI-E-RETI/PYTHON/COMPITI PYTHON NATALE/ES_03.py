def fibonacci (fib, num, a ,b):
    if num <= 0:
        return
    else:
        fib.append(fib[a] + fib[b])
        a += 1
        b += 1
        num -= 1
        fibonacci(fib, num, a, b)



fib = [0, 1]
a = 0
b = 1
num = int(input("Quanti numeri vuoi stampare ? "))
fibonacci(fib, num, a, b)
print(fib[1:])
