from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    hummer1 = SilverServiceTaxi("Hummer", 200, 2)
    print(hummer1)
    hummer1.drive(18)
    print("${:.2f}".format(hummer1.get_fare()))


main()
