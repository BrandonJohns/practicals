def main():
    number_of_rows = int(input("Please enter number of rows for the pyramid: "))
    get_number_of_blocks(number_of_rows)
    recursive(number_of_rows, 0)


def get_number_of_blocks(number_of_rows):
    number_of_blocks = 0
    for i in range(number_of_rows):
        number_of_blocks += number_of_rows - i

    print("the number of blocks for n rows is", number_of_blocks)


def recursive(number_of_rows, number_of_blocks):
    if number_of_rows > 0:
        number_of_blocks += number_of_rows
        recursive(number_of_rows-1, number_of_blocks)
    else:
        print(number_of_blocks)


main()
