import time
from queue import Queue

def rate_limiter(max_calls, interval):
    def decorator(func):
        call_times = Queue(maxsize=max_calls)

        def wrapper(*args, **kwargs):
            if call_times.full():
                oldest_call_time = call_times.get()
                time_diff = time.time() - oldest_call_time
                if time_diff < interval:
                    time.sleep(interval - time_diff)

            call_times.put(time.time())
            return func(*args, **kwargs)

        return wrapper

    return decorator
