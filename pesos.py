import time
import random

while True:
    time.sleep(3)

    var = open("currency.txt", 'r')
    var_line = var.readline()
    var.close()

    if var_line == 'pesos' or var_line == 'MX$':
        var = open("converter.txt", 'r')
        var_line_2 = var.readline()
        var.close()

        placeh = open('currency.txt', 'w')
        placeh.write('placeholder')
        placeh.close()

        new_var = float(var_line_2)

        converted_value = new_var * 18.65

        converted_value_2 = str(converted_value)

        var = open("converter.txt", 'w')
        var.write(converted_value_2)
        var.close()