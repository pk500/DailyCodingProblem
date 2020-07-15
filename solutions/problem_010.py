import time

def fn():
    print('hello')

def scheduler(fn,n):
    time.sleep(n/1000)
    fn()

scheduler(fn,1000)
