import asyncio
import time

def async_rate_limiter_decorator(max_calls, interval):
    def decorator(func):
        call_times = asyncio.Queue(maxsize=max_calls)

        async def wrapper(*args, **kwargs):
            if call_times.full():
                oldest_call_time = await call_times.get()
                time_diff = time.time() - oldest_call_time
                if time_diff < interval:
                    await asyncio.sleep(interval - time_diff)

            await call_times.put(time.time())
            return await func(*args, **kwargs)

        return wrapper

    return decorator