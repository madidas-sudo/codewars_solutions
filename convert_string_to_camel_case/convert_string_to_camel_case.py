from re import split
def to_camel_case(a):
    a = split("-|\_", a)
    for i, j in enumerate(a):
            if i != 0:
                a[i] = a[i].capitalize()
    return "".join(a)