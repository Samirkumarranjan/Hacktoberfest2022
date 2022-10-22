print("Enter Two Numbers: ", end="")

try:

    nOne = int(input())

    try:

        nTwo = int(input())

        if nOne > nTwo:

            lcm = nOne

        else:

            lcm = nTwo

        while True:

            if lcm % nOne == 0 and lcm % nTwo == 0:

                break

            else:

                lcm = lcm + 1

        print("\nLCM (" + str(nOne) + ", " + str(nTwo)+") = ", lcm)

    except ValueError:

        print("\nInvalid Input!")

except ValueError:

    print("\nInvalid Input!")
