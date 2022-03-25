def fib_memo(n, storage):
    if(n==0 or n==1):
        return n
    
    if storage[n]!=0:
        return storage[n]
    
    fnm1 = fib_memo(n-1, storage)
    fnm2 = fib_memo(n-2, storage)
    fn = fnm1 + fnm2
    
    storage[n] = fn
    return fn

n = int(input())
storage = [0]*(n+1)
print(fib_memo(n, storage))