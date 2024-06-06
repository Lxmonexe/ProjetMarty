def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb_color

def is_within_uncertainty(value, central_value, uncertainty):
    lower_bound = central_value - uncertainty
    upper_bound = central_value + uncertainty
    return lower_bound <= value <= upper_bound