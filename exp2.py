from database import db, cursor
import time
import timeit



start0 = time.time()
for _ in range(10000):
    start = timeit.default_timer()
    cursor.execute(
        """
        select first_name from sakila.actor where actor_id=1
        """
    )
    cursor.fetchall()
    end = timeit.default_timer()
    print(end-start)
end0 = time.time()

print(end0- start0)