def findResistance(a, b, c, d):
    # Hash-map to store the values
    # of the color-digits
    color_digit = {'black': '0',
                   'brown': '1',
                   'red': '2',
                   'orange': '3',
                   'yellow': '4',
                   'green': '5',
                   'blue': '6',
                   'violet': '7',
                   'grey': '8',
                   'white': '9'}

    multiplier = {'black': '0',
                  'brown': '10',
                  'red': '100',
                  'orange': '1000',
                  'yellow': '10000',
                  'green': '100000',
                  'blue': '1000000',
                  'violet': '10000000',
                  'grey': '100000000',
                  'white': '1000000000'}

    tolerance = {'brown': '+/- 1 %',
                 'red': '+/- 2 %',
                 'green': "+/- 0.5 %",
                 'blue': '+/- 0.25 %',
                 'violet': '+/- 0.1 %',
                 'gold': '+/- 5 %',
                 'silver': '+/- 10 %',
                 'none': '+/-20 %'}

    x = color_digit.get(a)
    xval = int(x) * int(multiplier.get(a))
    y = color_digit.get(b)
    yval = int(y) * int(multiplier.get(b))
    z = color_digit.get(c)
    zval = int(z) * int(multiplier.get(c))
    aa = tolerance.get(d)
    print("Resistance = " + str(xval + yval + zval) + " ohms " + " tolerance: %" + aa)


# Driver Code
if __name__ == "__main__":
    a = input("enter 1st color: ")
    b = input("enter 2nd color: ")
    c = input("enter 3rd color: ")
    d = input("enter 4th color: ")

    # Function Call
    findResistance(a, b, c, d)