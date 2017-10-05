from prac_08.unreliable_car import UnreliableCar


def main():
    ford_falcon = UnreliableCar("Ford Falcon", 100, 60)
    ford_falcon.drive(100)
    print(ford_falcon)

main()
