def calculate(**kwargs):
    if kwargs["operation"] == "add":
        answer = kwargs["first"] + kwargs["second"]
    elif kwargs["operation"] == "subtract":
        answer = kwargs["first"] - kwargs["second"]
    elif kwargs["operation"] == "multiply":
        answer = kwargs["first"] * kwargs["second"]
    else:
        answer = kwargs["first"] / kwargs["second"]
    
    if not kwargs["make_float"]:
        answer = int(answer)
    
    if kwargs.get("message") != None:
        return f"{kwargs['message']} {answer}"
    else:
        return f"The result is {answer}"

print(calculate(make_float = False, operation = "add", message = "You just added", first = 2, second = 4))
print(calculate(make_float = True, operation = "divide", first = 3.5, second = 5))
