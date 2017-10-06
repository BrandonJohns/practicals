from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)drive\n>>>"
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]


def display_taxis():
    count = 0
    for taxi in TAXIS:
        print(count, "-", taxi)
        count += 1


def menu():
    menu_selection = input(MENU).upper()
    while menu_selection not in list("QCD"):
        print("Invalid input please choose from the menu:")
        menu_selection = input(MENU).upper()
    return menu_selection


def main():
    default_taxi = TAXIS[0]
    print("Let's drive!")
    menu_selection = menu()
    taxi_selection = default_taxi
    current_bill = 0

    while menu_selection != "Q":
        if menu_selection == "C":
            display_taxis()
            taxi_selection = TAXIS[int(input("Choose taxi: "))]

        if menu_selection == "D":
            distance_to_drive = int(input("Drive how far? "))
            taxi_selection.drive(distance_to_drive)
            taxi_name = taxi_selection.name
            print("Your {} trip cost you ${:.2f}".format(taxi_name, taxi_selection.get_fare()))

        current_bill = taxi_selection.get_fare() + current_bill
        print("bill to date: ${:.2f}".format(current_bill))
        menu_selection = menu()

    print("Total trip cost: ${:.2f}".format(current_bill))
    print("Taxis are now:")
    display_taxis()

main()
