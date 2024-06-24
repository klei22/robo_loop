import sys
import re

def scale_value(value, min_input, max_input, min_output, max_output):
    """ Scale the input value from the input range to the output range. """
    return (value - min_input) * (max_output - min_output) / (max_input - min_input) + min_output

def map_to_ascii(value):
    """ Map grayscale values to ASCII characters. """
    ascii_chars = " .:-=+*#%@"
    return ascii_chars[int(scale_value(value, 0, 255, 0, len(ascii_chars) - 1))]

def process_image_data(data, width, height, new_width, new_height):
    """ Convert grayscale image data to ASCII art. """
    ascii_image = []
    scale_x = width // new_width
    scale_y = height // new_height

    for y in range(new_height):
        line = ''
        for x in range(new_width):
            avg_value = 0
            for dy in range(scale_y):
                for dx in range(scale_x):
                    index = (y * scale_y + dy) * width + (x * scale_x + dx)
                    avg_value += data[index]
            avg_value //= (scale_x * scale_y)
            line += map_to_ascii(avg_value)
        ascii_image.append(line)

    return ascii_image

def read_grayscale_values_from_file(file_path):
    """ Read grayscale values from a file. """
    with open(file_path, "r") as file:
        content = file.read()
        numbers = re.findall(r'\d+', content)
        return [int(num) for num in numbers]

def main():
    # Read data from file
    data = read_grayscale_values_from_file("image.txt")
    print(len(data))
    width, height = 640, 480  # Original dimensions
    new_width, new_height = 64, 48  # ASCII dimensions
    
    ascii_art = process_image_data(data, width, height, new_width, new_height)
    
    with open("ascii.txt", "w") as f:
        for line in ascii_art:
            print(line)
            f.write(line + "\n")

if __name__ == "__main__":
    main()

