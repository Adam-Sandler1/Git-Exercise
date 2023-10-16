class DAC:
    def __init__(self, voltage, max_volt, bits):
        self.volt = voltage
        self.max_volt = max_volt
        self.bits = bits
        self.max_number = 2**bits - 1

    def to_digital(self):
        number = (self.max_number * self.volt) / self.max_volt
        digital_number = round(min(max(0, number), self.max_number))
        return bin(digital_number)

    def set_digital_value(self, value):
        self.volt = (value * self.max_volt) / self.max_number

    def get_voltage(self):
        return self.volt