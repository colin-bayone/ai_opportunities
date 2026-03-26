# function to generate random colors based upon user input

import random
def generate_random_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
    return colors
# Example usage:
num_colors = 5
random_colors = generate_random_colors(num_colors)
print(random_colors)