resistors_dict = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}
metric_prefix = {
    "gigaohms": 1_000_000_000,
    "megaohms": 1_000_000,
    "kiloohms": 1_000,
    "ohms": 1,
}
def label(colors):
    band_values = [resistors_dict[colors[i].lower()] for i in range(3)]
    resistor_value = (band_values[0]*10 + band_values[1]) * 10**band_values[2]
    for prefix, factor in metric_prefix.items():
        if resistor_value == 0:
            return "0 ohms"
        if not resistor_value % factor:
            return f"{resistor_value//factor} {prefix}"