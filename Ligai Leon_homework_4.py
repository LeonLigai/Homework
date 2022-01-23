class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds

    def time(self):
        day = self.seconds // 86400
        hour = (self.seconds - day * 86400) // 3600
        minute = (self.seconds - day * 86400 - hour * 3600) // 60
        second = (self.seconds - day * 86400 - hour * 3600 - minute * 60)
        print(f"{day} день,{hour} часов {minute} минут и {second} секунда")

time_1 = TimeDesk(86401)
print(time_1.time())


