MAX_VOLTAGE = 5
N_O_BITS = 10
MAX_NUMBER = 2**N_O_BITS - 1

class DAC:
    def __init__(self, voltage):
        self.volt = voltage

    def to_digital(self):
        number = (MAX_NUMBER * self.volt) / MAX_VOLTAGE
        digital_number = round(min(max(0, number), MAX_NUMBER))
        return bin(digital_number)

    def set_digital_value(self, value):
        self.volt = (value * MAX_VOLTAGE) / MAX_NUMBER

    def get_voltage(self):
        return self.volt