class TimeToSend:
    def __init__(self, priority, hour, minute):
        self.priority = priority
        self.hour = hour
        self.minute = minute
    
    def __repr__(self):
        return f"Priority {self.priority}: {self.hour:02d}:{self.minute:02d}"