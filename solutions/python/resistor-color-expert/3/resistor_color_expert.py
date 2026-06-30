RESISTORS_VALUES = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
TOLERANCES = {'brown': 1, 'red': 2, 'gold': 5, 'silver': 10, 'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5}
UNITS = ['ohms', 'kiloohms', 'megaohms']


def resistor_label(colors: list[str]) -> str:
    if colors == ['black']:
        return '0 ohms'
    *values, multiplier, tolerance = colors
    val = 0.0
    for value in values:
        val = val * 10 + RESISTORS_VALUES.index(value)
    val *= 10 **  RESISTORS_VALUES.index(multiplier)
    power = 0
    while val >= 1000:
        val /= 1000
        power += 1
    return f'{val:n} {UNITS[power]} ±{TOLERANCES[tolerance]}%'