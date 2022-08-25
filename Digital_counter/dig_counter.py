class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.start = start
        self.end = end
        self.current = current if current is not None else start

    def increase(self):
        if self.current < self.end:
            self.current += 1
            return self.current

    @property
    def current_value(self):
        return self.current


if __name__ == '__main__':
    dig_counter = DigitalCounter(current=88)
    print(dig_counter.current_value)
    dig_counter.increase()
    print(dig_counter.current_value)
