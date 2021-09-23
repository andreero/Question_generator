from math import ceil, floor
from random import randint
from functools import reduce

male_names = ['Leon', 'Ben', 'Noah', 'Finn', 'Paul', 'Elias', 'Luis',
              'Henry', 'Luca', 'Emil', 'Anton', 'Oskar', 'Theo', 'Leo']

female_names = ['Mia', 'Emilia', 'Sofia', 'Hanna', 'Emma', 'Mila',
                'Lea', 'Luisa', 'Clara', 'Aintlie', 'Frieda', 'Ida', 'Lia']

weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']

measurement_units = ['mm', 'cm', 'dm', 'm', 'km']

numbersTe = {
    1: 'erste',
    2: 'zweite',
    3: 'dritte',
    4: 'vierte',
    5: 'fünfte',
    6: 'sechste',
    7: 'siebte',
    8: 'achte',
    9: 'neunte',
    10: 'zehnte',
}
numbers = {
    1: 'eins',
    2: 'zwei',
    3: 'drei',
    4: 'vier',
    5: 'fünf',
    6: 'sechs',
    7: 'sieben',
    8: 'acht',
    9: 'neun',
    10: 'zehn',
    11: 'elf',
    12: 'zwölf',
    13: 'dreizehn',
    14: 'vierzehn',
    15: 'fünfzehn',
    16: 'sechzehn',
    17: 'siebzehn',
    18: 'achtzehn',
    19: 'neunzehn',
    20: 'zwanzig',
    30: 'dreizig',
    40: 'vierzig',
    50: 'fünfzig',
    60: 'sechzig',
    70: 'siebzig',
    80: 'achtzig',
    90: 'neunzig',
    100: 'hundert',
    1000: 'tausend',
    1000000: 'Millionen',
    1000000000: 'Milliarden',
}


def get_fakultaet(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
    # return reduce(lambda x,y: x*y, range(1,1+number))

def getValueOfKey(data, key):
    return data[key] if key in data else ''

def randdecimal(low, high, step=0.1, precision=1):
    low_scaled = ceil(float(low)/step)
    high_scaled = floor(float(high)/step)
    result = round(randint(low_scaled, high_scaled) * step, precision)
    return int(result) if float(result).is_integer() else result
