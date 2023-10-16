from digital_analog_converter import DAC

converter = DAC(3, 10, 5)
print(converter.to_digital())

converter.set_digital_value(0b10011)
print(converter.get_voltage())