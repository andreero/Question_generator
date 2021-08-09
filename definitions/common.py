from math import ceil, floor
from random import randint

male_names = ['Leon', 'Ben', 'Noah', 'Finn', 'Paul', 'Elias', 'Luis',
              'Henry', 'Luca', 'Emil', 'Anton', 'Oskar', 'Theo', 'Leo']

female_names = ['Mia', 'Emilia', 'Sofia', 'Hanna', 'Emma', 'Mila',
                'Lea', 'Luisa', 'Clara', 'Aintlie', 'Frieda', 'Ida', 'Lia']


def randdecimal(low, high, step=0.1, precision=1):
    low_scaled = ceil(float(low)/step)
    high_scaled = floor(float(high)/step)
    result = round(randint(low_scaled, high_scaled) * step, precision)
    return int(result) if float(result).is_integer() else result
