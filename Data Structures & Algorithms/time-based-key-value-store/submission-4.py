import bisect
class TimeMap:

    def __init__(self):
        self.times = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = [(timestamp, value)]
        else:
            self.times[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        ind = bisect.bisect_right(self.times[key], timestamp, key = lambda x:x[0])
        if ind == 0:
            return ""
        return self.times[key][ind - 1][1]
