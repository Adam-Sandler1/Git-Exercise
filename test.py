from digital_analog_converter import DAC

converter = DAC(3)
print(converter.to_digital())

converter.set_digital_value(0b1100100001)
print(converter.get_voltage())