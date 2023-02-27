import redis
import time, timeit

r = redis.Redis(host='localhost', port=6379)

start0 = time.time()
for _ in range(2000):
    start = timeit.default_timer()
    r.set('1','44')
    val = r.get('1')
    end = timeit.default_timer()
    print(end-start)
end0 = time.time()

print(end0- start0)