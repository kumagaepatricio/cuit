import sys


def generate_cuit(code, document):

    cuit = str(code) + document

    sequence = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    sum = check_digit = 0
    module = 11
    invalid_digit = 10

    for index, value in enumerate(sequence):
        sum += int(cuit[index]) * int(value)

    check_digit = (module - (sum % module))

    if (check_digit == invalid_digit):
        code = int(code) + 1

        check_digit = self.generate_cuit(code, document)

        return str(check_digit)

    if (check_digit == module):
        check_digit = 0

    return str(code) + str(document) + str(check_digit)


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    print generate_cuit(a, b)
