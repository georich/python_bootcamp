#raise ValueError("Invalid value")

def colorize(text, color):
    colors = ("red", "blue", "green")
    if type(text) is not str:
        raise TypeError("text must be a string")
    if color not in colors:
        raise ValueError("color is an invalid color")
    print(f"Printed {text} in {color}")

colorize("hello", "red")
#colorize(2, "red")
colorize("hello", "yellow")
