def fib_rec(n):
    if n ==0 or n==1:
        return n
    fnm1 = fib_rec(n-1)
    fnm2 = fib_rec(n-2)
    fn = fnm1 + fnm2
    return fn

n = int(input())
print(fib_rec(n))