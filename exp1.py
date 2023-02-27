import redis
import timeit
import time

r = redis.Redis(host='10.60.16.53', port=6379)
start0 = time.time()
for _ in range(2000):
    start = timeit.default_timer()
    r.set('1','44')
    val = r.get('test')
    end = timeit.default_timer()
    print(end-start)
end0 = time.time()

print(end0- start0)