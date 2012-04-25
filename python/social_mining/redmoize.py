# see:
# http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
# http://www.artima.com/weblogs/viewpost.jsp?thread=240808

import redis
import functools

class memoize(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned 
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            print self.func.__name__, "caching!"
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            return self.func(*args)
    
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

class redmoize(object):
    '''Decorator. Caches a function's return value each time it is called 
    in a Redis store. It passes the data through a marshalling function before
    saving it if one is given.
    '''
    def __init__(self, redis, marsh=None):
        self.redis = redis
        self.marsh = marsh
        
    def __call__(self, f):
        def wrapped(*args):
            if self.redis.hexists(f.__name__, hash(args)):
                return self.redis.hget(f.__name__, hash(args))
            else:
                value = f(*args)
                if self.marsh: value = self.marsh(value)
                self.redis.hset(f.__name__, hash(args), value)
                return value
        return wrapped
    
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
            



