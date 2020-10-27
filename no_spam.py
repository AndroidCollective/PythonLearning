menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" in meal:
        b = list(filter(lambda a: a != "spam", meal))
        a = list(filter(("spam").__ne__, meal))
        #meal.remove("spam")
        print(", ".join(b))

for meal in menu:
    for s in meal:
        if s != "spam":
            print(s,end=', ')
    print()