def calibrate_yellow(marty):
    valeurHex = marty.get_color_sensor_hex("left")
    valeurRGB = hex_to_rgb(valeurHex)
    return valeurRGB
    
def calibrate_green(marty):
    valeurHex = marty.get_color_sensor_hex("left")
    valeurRGB = hex_to_rgb(valeurHex)
    return valeurRGB

def calibrate_pink(marty):
    valeurHex = marty.get_color_sensor_hex("left")
    valeurRGB = hex_to_rgb(valeurHex)
    return valeurRGB

def calibrate_red(marty):
    valeurHex = marty.get_color_sensor_hex("left")
    valeurRGB = hex_to_rgb(valeurHex)
    return valeurRGB

def calibrate_cyan(marty):
    valeurHex = marty.get_color_sensor_hex("left")
    valeurRGB = hex_to_rgb(valeurHex)
    return valeurRGB

def calibrate_blue(marty):
    valeurHex = marty.get_color_sensor_hex("left")
    valeurRGB = hex_to_rgb(valeurHex)
    return valeurRGB

def calibrate_black(marty):
    valeurHex = marty.get_color_sensor_hex("left")
    valeurRGB = hex_to_rgb(valeurHex)
    return valeurRGB

def color_sensor(yellow, green, pink, red, blue, cyan, black, marty):
    colorHEX = marty.get_color_sensor_hex("left")
    colorRGB = hex_to_rgb(colorHEX)
    if ((is_within_uncertainty(colorRGB[0], yellow[0], 10)) and (is_within_uncertainty(colorRGB[1], yellow[1], 10)) and (is_within_uncertainty(colorRGB[2], yellow[2], 10))):
        return "yellow"
    elif ((is_within_uncertainty(colorRGB[0], green[0], 10)) and (is_within_uncertainty(colorRGB[1], green[1], 10)) and (is_within_uncertainty(colorRGB[2], green[2], 10))):
        return "green"
    elif ((is_within_uncertainty(colorRGB[0], pink[0], 10)) and (is_within_uncertainty(colorRGB[1], pink[1], 10)) and (is_within_uncertainty(colorRGB[2], pink[2], 10))):
        return "pink"
    elif ((is_within_uncertainty(colorRGB[0], red[0], 10)) and (is_within_uncertainty(colorRGB[1], red[1], 10)) and (is_within_uncertainty(colorRGB[2], red[2], 10))):
        return "red"
    elif ((is_within_uncertainty(colorRGB[0], blue[0], 10)) and (is_within_uncertainty(colorRGB[1], blue[1], 10)) and (is_within_uncertainty(colorRGB[2], blue[2], 10))):
        return "blue"
    elif ((is_within_uncertainty(colorRGB[0], cyan[0], 10)) and (is_within_uncertainty(colorRGB[1], cyan[1], 10)) and (is_within_uncertainty(colorRGB[2], cyan[2], 10))):
        return "cyan"
    elif ((is_within_uncertainty(colorRGB[0], black[0], 10)) and (is_within_uncertainty(colorRGB[1], black[1], 10)) and (is_within_uncertainty(colorRGB[2], black[2], 10))):
        return "black"
    else:
        return "not defined"



def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb_color

def is_within_uncertainty(value, central_value, uncertainty):
    lower_bound = central_value - uncertainty
    upper_bound = central_value + uncertainty
    return lower_bound <= value <= upper_bound


