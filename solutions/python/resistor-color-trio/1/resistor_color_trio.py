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


def label(colors):
    band_values = [resistors_dict[colors[i].lower()] for i in range(3)]
    resistor_value = (band_values[0]*10 + band_values[1]) * 10**band_values[2]
    if resistor_value % 10**9 == 0 and resistor_value !=0 :
        return str(resistor_value // 10**9) + " gigaohms"
    if resistor_value % 10**6 == 0 and resistor_value !=0 :
        return str(resistor_value // 10**6) + " megaohms"
    if resistor_value % 10**3 == 0 and resistor_value !=0 :
        return str(resistor_value // 10**3) + " kiloohms"
    return str(resistor_value) + " ohms"