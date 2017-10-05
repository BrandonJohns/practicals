from prac_07.guitar import Guitar


def main():
    name = "name"
    guitars = []
    while name != "":  # figure out a better way of doing while loops
        name = input("Name: ")
        if name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(guitar, "added.")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage = guitar.is_vintage()
        if vintage is True:
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1,
            guitar.name, guitar.year, guitar.cost, vintage_string))


main()
