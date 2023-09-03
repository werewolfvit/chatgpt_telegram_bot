import time

class RateLimiter:
    def __init__(self, max_calls, interval):
        self.max_calls = max_calls
        self.interval = interval
        self.calls = []

    async def rate_limiter_check(self):
        current_time = time.time()

        # Remove calls made earlier than the time window
        self.calls = [call for call in self.calls if call > current_time - self.interval]

        if len(self.calls) >= self.max_calls:
            return False

        self.calls.append(current_time)
        return True
