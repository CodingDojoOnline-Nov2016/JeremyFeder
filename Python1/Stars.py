
x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(list):
    for stars in list:
        print stars * "*"
draw_stars(x)


x2 = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(list):
    for stars in list:
        if type(stars) == int:
            print stars * "*"
        elif type(stars) == str:
            first_init = stars[0].lower()
            print first_init * len(stars)
draw_stars(x2)
