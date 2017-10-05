from prac_07.guitar import Guitar

def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Kmart special", 2016, 25.99)
    print("Expected 95. got",guitar1.get_age())
    print("Expected True. got",guitar1.is_vintage())
    print("Expected False. got", guitar2.is_vintage())
    print(guitar1)
    print(guitar2)
main()