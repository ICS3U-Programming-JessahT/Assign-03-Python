#!/usr/bin/env python3

# Created By: Jessah
# Date: Oct 24, 2022
# This program asks how many croissant the user bought and if the user has 6 or more
# The user doesn't pay tax, if any lower they pay with tax


def main():

    croissant_num = input("How many croissant did you buy?: ")

    try:
        int_num = int(croissant_num)

        total = int_num * 2.55

        subtotal = int_num * 2.55
        tax = subtotal * 0.13
        total_with_tax = subtotal + tax

        if int_num > 0:

            if int_num > 6:
                print("Since the amount is over 6, you do not have to pay tax")
                print("The total is: ${:,.2f}".format(total))

            elif int_num < 6 or int_num >= 0:
                print("Since the amount is under 6 you have to pay tax")
                print("The total with tax is:  ${:,.2f}".format(total_with_tax))

    except Exception:
        print("")
        print("That is not a valid input")

    finally:
        print("Try again?")


if __name__ == "__main__":
    main()
