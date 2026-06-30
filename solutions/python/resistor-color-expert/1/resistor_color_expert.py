RESISTORS_DICT = {
    'black': (0, ''),
    'brown': (1, '1'),
    'red': (2, '2'),
    'orange': (3, ''),
    'yellow': (4, ''),
    'green': (5, '0.5'),
    'blue': (6, '0.25'),
    'violet': (7, '0.1'),
    'grey': (8, '0.05'),
    'white': (9, ''),
    'gold': (0, '5'),
    'silver': (0, '10'),
}
UNITS = ["ohms", "kiloohms", "megaohms"]
def resistor_label(colors: list[str]) -> str:
    if colors == ["black"]:
        return "0 ohms"
    if len(colors) > 3:
        *values, multiplier, tolerance = colors
    else:
        values, multiplier, tolerance = colors, RESISTORS_DICT['black'][0], None
    val = 0.0
    for value in values:
        val = val * 10 + RESISTORS_DICT[value][0]
    val *= 10 ** RESISTORS_DICT[multiplier][0]
    # Shift numbers over to get the proper prefix.
    power = 0
    while val > 1000:
        val /= 1000
        power += 1
    # Add a tolerance, if one is supplied.
    result = f"{val:n} {UNITS[power]}"
    print(result)
    if tolerance:
        result += f" ±{RESISTORS_DICT[tolerance][1]}%"
    return result
