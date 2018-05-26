def copy_and_reverse(original_text, reversed_text):
    with open(original_text) as original:
        text = original.read()
        
    with open(reversed_text, "w") as to_write:
        to_write.write(text[::-1])
