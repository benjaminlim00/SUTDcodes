class Time:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    def get_time(self):
        return self._hours * 60 * 60 + self._minutes * 60 + self._seconds
    def set_time(self, x):
        while x > 86400:
            x -= 86400
        
        minutes = x//60
        hours = minutes // 60
        secleft = x - hours * 3600
        minutes = secleft // 60
        seconds = secleft % 60
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        
    elapsed_time = property(get_time, set_time)
    def __str__(self):
        return "Time: {}:{}:{}".format(self._hours, self._minutes, self._seconds)
    
    
t = Time(10, 19, 10)
print(t.elapsed_time)
t.elapsed_time = 555550
print(t.elapsed_time)
print(t)
