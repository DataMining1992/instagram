#coding=utf-8
#!/usr/bin/python
def log(level, *args, **kvargs):
    def inner(func):

#*无名参数
#**有名参数
        def wrapper(*args, **kvargs):
            print level, 'before calling ', func.__name__
            print 'args', args
            func(*args, **kvargs)
            print level,'kvargs', kvargs
            print level,'end calling ', func.__name__
        return wrapper
    return inner
@log(level='INFO')
def hello(name, age):
    print 'hello', name, age

if __name__=='__main__':
    hello ('wangqi',5)