def validate_int(inp_number: int = None):
    """
    Inputs a number and returns -1 if it is not a integer
    :param inp_number:
    :return: The number as int or -1 if not int
    """

    # None-type?
    if type(inp_number) is type(None):
        return -1

    try:
        inp_number_integer = int(inp_number)
        return inp_number_integer
    except ValueError:
        print("validate_int() · The provided value is not an integer")
        return -1
