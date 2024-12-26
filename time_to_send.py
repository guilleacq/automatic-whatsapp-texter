import datetime

class TimeToSend:
    def __init__(self, priority, hour, minute):
        self.priority = priority
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Priority {self.priority}: {self.hour:02d}:{self.minute:02d}"

    def is_time_to_send(self, current_time):
        # Checks if it's time to send a message
        return current_time.hour == self.hour and current_time.minute == self.minute