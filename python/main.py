#!/usr/bin/env python3

def to_dict(initial_data=None):
    if initial_data is None:
        initial_data = {}
    pair_dict = initial_data

    print("This program seeks to know which institutions were used to pursue a field of study")
    while True:
        usr_input = input("Enter items followed by a comma (institution, field of study):\n")
        item_list = usr_input.split(", ")
        # result_str = ' '.join(item_list)

        if len(item_list) < 2:
            print("Invalid input. Format: institution, field of study")
            continue

        institution, field = item_list[0], ', '.join(item_list[1:])
        pair_dict[institution] = field

        # ask if the user wants to enter more items
        continue_input = input("Do you want to add other items? (yes/no): ").lower()
        if continue_input != 'yes':
            break
    return pair_dict

def main():
    initial_data = {}
    result_data = to_dict(initial_data)

    # print the resulting dictionary
    print("\nSchool and field of study:")
    for key, value in result_data.items():
        print(f"{key.title()}: {value.title()}")

if __name__ == "__main__":
    main()
