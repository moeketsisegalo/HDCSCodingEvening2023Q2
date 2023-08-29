def rgb_to_hex(red, green, blue):
    #Store thee original RGB values in separate variables for colot red, green, and blue 
    rgb_red = red 
    rgb_green = green 
    rgb_blue = blue
    
    # ensuring that the modified values are in the valid RGB range (0-255)
    modified_red = max(0, min(255, rgb_red))
    modified_green = max(0, min(255, rgb_green))
    modified_blue = max(0, min(255, rgb_blue))
    
    # Convert the modified RGB values to HEX format
    hex_value = "#"  # Start the HEX value
    
    # Convert each modified RGB component to its HEX equivalent and append to the HEX value
    hex_value += f"{modified_red:02X}"
    hex_value += f"{modified_green:02X}"
    hex_value += f"{modified_blue:02X}"
    return hex_value

# Test cases
print(rgb_to_hex(255, 255, 255))   
print(rgb_to_hex(255, 255, 255))  
print(rgb_to_hex(0, 0, 0))    
