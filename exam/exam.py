class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def celsius_to_fahrenheit(self):
        return self.temperature * 9 / 5 + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5 / 9

    def set_temperature(self, temperature: float):
        if temperature < -273.15:
            raise ValueError('Temperatura ne mozye byti nizshe absolytnogo nylya')

try:
    priclad = Temperature(66)
    priclad2 = Temperature(777)
    print('Farengeiti:', priclad.celsius_to_fahrenheit())
    print('Celyisiya:', priclad2.fahrenheit_to_celsius())
    priclad.set_temperature(-1000)

except ValueError as e:
    print('Pomilka:', e)


